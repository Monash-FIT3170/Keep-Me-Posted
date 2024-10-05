from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai
import os
from dotenv import load_dotenv
from googleapiclient.errors import HttpError

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create your views here.W

def generate_title_and_summary(transcript):
    """Generates a title and summary for the meeting transcript."""
    
    # No transcript provided
    if not transcript.strip():
        return None, "No summary can be generated without a transcript."

    # Title generation prompt
    title_prompt = (
        "Create a concise and relevant title for a meeting summary based on the following transcript: "
        f"{transcript}"
    )

    # Summary generation prompt
    summary_prompt = """The user will give you a meeting transcript. You are an expert in concisely summarising meeting transcripts so that people wanting to review what happened in the meeting can read this summary and understand the key details of what was discussed and any important outcomes. They should be able to understand what tasks have been assigned, when it is due, and the people that have been assigned to it. This should be done in a professional manner, so you must ensure that any profanity or slurs encountered is omitted from the final output. Ensure to NOT include sensitive information such as banking information, passwords, addresses. Quote what someone said with their name if their names are included in the summary. Below is the structure you should follow to generate a summary. Using the following headings take note of the additional information I have included to guide what you include under each heading.
    1. Start with a suitable title for the summary
    2. Meeting Agenda: Start with what the meeting’s purpose was and what was the overarching agenda. Include progress on previous tasks if this has been discussed. If the tasks are not completed, state the estimated time it will take to complete if provided and the reason for the delay if provided.
    3. Key Discussion Points: What were the key things that were debated on or considered, in dot points? Include important information from the meeting relating to the main topic, and if there is information about who said it, include their names as well. List these in full sentences starting with the name of the person (if applicable) and then what was said.
    4. Final Outcome(s): Summarise the finalised, key decisions that were made during the meeting, in dot points.
    5. Action items: Summarise what needs to be done and by whom, including deadlines if provided, in dot points. Include the date and time of the next meeting, if it is mentioned."""
    try:
        # Create the model instance
        model = genai.GenerativeModel('gemini-pro')

        # Generate title
        title_response = model.generate_content(
            [title_prompt],
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            }
        )

        # Generate summary
        summary_response = model.generate_content(
            [f"{summary_prompt} Here is the transcript you need to summarise: {transcript}"],
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            }
        )

        # Check for prompt feedback in title generation
        title_feedback = title_response.prompt_feedback
        if title_feedback and "block_reason" in title_feedback:
            return None, None

        # Check for prompt feedback in summary generation
        summary_feedback = summary_response.prompt_feedback
        if summary_feedback and "block_reason" in summary_feedback:
            return None, None

        # Extract and return title and summary
        title = title_response.text.strip()
        summary = summary_response.text.strip()

        return title, summary
    except HttpError as error:
        return handle_api_error(error)


def generate_summary(request):
    """Handles the request to generate or regenerate the meeting summary and title."""
    try:
        transcript = request.POST.get("transcript")
        if transcript == "" or transcript is None:
            return HttpResponse("Transcript not found", status=404)

        title, summary = generate_title_and_summary(transcript)

        #if an HttpResonse is given, return that HttpResponse
        if isinstance(summary, HttpResponse):
            return summary
        
        if title is None or summary is None:
            return 400,HttpResponse("An unexpected error occurred. Please try again later.", status=400)

        response_data = {
            "title": title,
            "summary": summary
        }
        return JsonResponse(response_data, status=200)
    except HttpError as error:
        return handle_api_error(error)

def handle_api_error(error):
    """Handles any error codes that Gemini may return."""
    error_responses = {
        400: HttpResponse("Invalid request. Please check the request format and try again.", status=400),
        403: HttpResponse("Permission denied. Please check your API key and permissions.", status=403),
        404: HttpResponse("Resource not found. Please check the request URL and try again.", status=404),
        429: HttpResponse("Rate limit exceeded. Please wait and try again later.", status=429),
        500: HttpResponse("Internal server error. Please try again later.", status=500),
        503: HttpResponse("Service unavailable. Please try again later.", status=503),
    }
    #return the error, if the error is not in the list of error responses, return a generic response
    return error.status_code,error_responses.get(error.status_code, HttpResponse("An unexpected error occurred. Please try again later.", status=500))