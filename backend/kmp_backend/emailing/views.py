from email.mime.application import MIMEApplication
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import smtplib, ssl, markdown2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from PyPDF2 import PdfReader, PdfWriter
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(request):
   
    username =  os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_API_KEY")

    message = request.POST.get('message') # get message from data
    subject = request.POST.get('subject')  
    contacts = request.POST.get('contacts')
    transcript = request.POST.get('transcript')
    user_email = request.POST.get('userEmail', 'Guest')  # Get the user's email or default to 'Guest'

    # Extract only the part before the '@' symbol if it's not 'Guest'
    if user_email != 'Guest':
        first_part_email = user_email.split('@')[0]  # Get the part before '@'
    else:
        first_part_email = 'Guest'

    if not contacts:
        raise ValueError("Contacts list is empty.")
    else:
        contacts = contacts.split(',')
        for contact in contacts:
            email = MIMEMultipart("alternative")
            email["Subject"] = subject
            email["From"] = username
            email["To"] = contact

            # If the user is not 'Guest', show both the first part and full email in the signature
            if user_email != 'Guest':
                signature = f"\n\nThis summary was generated using Keep Me Posted© on behalf of:\n\n<strong>{first_part_email} | {user_email}</strong>"
            else:
                # If the user is 'Guest', only show 'Guest'
                signature = f"\n\nThis summary was generated using Keep Me Posted© on behalf of:\n\n<strong>Guest</strong>"

            # Append the signature to the message
            message_with_signature = message + signature

            # Convert message into plain MIMEText object with signature
            part1 = MIMEText(message_with_signature, "plain")

            # Convert message into HTML MIMEText object with signature
            message_html = markdown2.markdown(message_with_signature)
            part2 = MIMEText(message_html, "html")
        

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            email.attach(part1)
            email.attach(part2)

            if transcript:  # Only attach PDF if transcript exists
                path = "emailing/static/Transcript_Template.pdf"
                transcript_pdf = create_pdf(path, transcript)
                attachment = MIMEApplication(transcript_pdf.read(), _subtype="pdf")
                attachment.add_header('Content-Disposition', 'attachment', filename='Meeting_Transcript.pdf')
                email.attach(attachment)

            try:
                # Create secure connection with server and send email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(username, password)
                    server.sendmail(
                        username, contact, email.as_string()
                    )
                
            except smtplib.SMTPHeloError as e:
                return JsonResponse({'error': f"HELO error occurred: {str(e)}"}, status=500)
            except smtplib.SMTPAuthenticationError as e:
                return JsonResponse({'error': 'Authentication failed.'}, status=500)
            except smtplib.SMTPNotSupportedError:
                return JsonResponse({'error': 'SMTP command not supported.'}, status=500)
            except smtplib.SMTPException as e:
                return JsonResponse({'error': "No suitable authentication method found."}, status=500)
    
    return JsonResponse({'details': "Emails sent successfully!"}, status=200)

def create_pdf(path, transcript):

    # Create a buffer for the new PDF with the transcript (To use memory and not temporary files)
    transcript_buffer = BytesIO()

    RIGHT_MARGIN_INCHES = 0.90
    LEFT_MARGIN_INCHES = 0.90
    TOP_MARGIN_INCHES = 1.2
    BOTTOM_MARGIN_INCHES = 1.0


    # Set up the document with margins
    doc = SimpleDocTemplate(
        transcript_buffer, 
        pagesize=letter,
        rightMargin=RIGHT_MARGIN_INCHES * inch, 
        leftMargin=LEFT_MARGIN_INCHES * inch, 
        topMargin=TOP_MARGIN_INCHES * inch, 
        bottomMargin=BOTTOM_MARGIN_INCHES * inch
    )

    # Define styles for the paragraph
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']

    # Create the content for the PDF
    elements = []
    for line in transcript.splitlines():
        elements.append(Paragraph(line, normal_style))
        elements.append(Spacer(1, 12))  # Space between lines

    # Build the PDF
    doc.build(elements)

    # Move the buffer's pointer to the beginning
    transcript_buffer.seek(0)

    # Read the existing PDF
    existing_pdf = PdfReader(path)
    transcript_pdf = PdfReader(transcript_buffer)

    # Create a PdfWriter object for the final merged PDF
    output_pdf_writer = PdfWriter()

    # Merge the transcript with the existing PDF
    for existing_page, transcript_page in zip(existing_pdf.pages, transcript_pdf.pages):
        existing_page.merge_page(transcript_page)
        output_pdf_writer.add_page(existing_page)

    # If the transcript has more pages, add those
    for page_num in range(len(existing_pdf.pages), len(transcript_pdf.pages)):
        output_pdf_writer.add_page(transcript_pdf.pages[page_num])


    # Create a buffer to hold the final merged PDF
    output_pdf = BytesIO()
    output_pdf_writer.write(output_pdf)

    # Move the buffer's pointer to the beginning
    output_pdf.seek(0)

    return output_pdf
