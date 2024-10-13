from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import os
from googleapiclient.errors import HttpError
from httplib2 import Response

class MockHttpError(HttpError):
    """
    Custom mock HttpError class to simulate API errors.
    """
    def __init__(self, status_code):
        self.resp = self._make_response(status_code)
        self.content = b'{}'

    @staticmethod
    def _make_response(status_code):
        response = Response({'status': status_code})
        response.reason = 'Mocked reason'
        return response
    
class GenerateSummaryTests(TestCase):
    """
    Test suite for the generate_summary view.
    """

    def setUp(self):
        """
        Set up method that runs before every test method.
        Initializes the test client and sets the URL for the view.
        """
        self.client = Client()
        # Get the URL for the summarizer view by its name
        self.url = reverse('summariser')
        # Mock the API key for testing
        os.environ['GEMINI_API_KEY'] = 'fake_api_key_for_testing'

    # @patch -> pretend generative model works

    @patch('google.generativeai.GenerativeModel')
    def test_transcript_not_found(self, mock_model):
        """
        Test case: no transcript provided.
        Expect a 404 status code and a specific error message.
        """
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Transcript not found")

    @patch('google.generativeai.GenerativeModel')
    def test_safe_transcript(self, mock_model):
        """
        Test case: a normal transcript is provided.
        Expect a 200 status code and a valid summary in the response.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.return_value = mock_response("This is a safe summary.", {})

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.json())
        self.assertEqual(response.json()['summary'], "This is a safe summary.")

    @patch('google.generativeai.GenerativeModel')
    def test_transcript_with_swear_word(self, mock_model):
        """
        Test case: a transcript with inappropriate text.
        Expect a 511 status code and a specific error message indicating unsafe content.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.return_value = mock_response("This transcript contains inappropriate content.", {"block_reason": "Hate Speech"})

        response = self.client.post(self.url, {'transcript': 'This is a damn test transcript.'})
        self.assertEqual(response.status_code, 511)
        self.assertEqual(response.content.decode(), "Unsafe transcript provided")

    @patch('google.generativeai.GenerativeModel')
    def test_transcript_with_sensitive_information(self, mock_model):
        """
        Test case: a transcript with sensitive information.
        Expect a 200 status code and the sensitive information should not be present in the summary.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.return_value = mock_response("This summary does not contain sensitive information.", {})

        response = self.client.post(self.url, {'transcript': 'The password is 12345.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.json())
        self.assertNotIn('12345', response.json()['summary'])

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_400(self, mock_model):
        """
        Test case: API returns a 400 error.
        Expect a 400 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(400)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Invalid request. Please check the request format and try again.")

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_403(self, mock_model):
        """
        Test case: API returns a 403 error.
        Expect a 403 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(403)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.content.decode(), "Permission denied. Please check your API key and permissions.")

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_404(self, mock_model):
        """
        Test case: API returns a 404 error.
        Expect a 404 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(404)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Resource not found. Please check the request URL and try again.")

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_429(self, mock_model):
        """
        Test case: API returns a 429 error.
        Expect a 429 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(429)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.content.decode(), "Rate limit exceeded. Please wait and try again later.")

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_500(self, mock_model):
        """
        Test case: API returns a 500 error.
        Expect a 500 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(500)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode(), "Internal server error. Please try again later.")

    @patch('google.generativeai.GenerativeModel')
    def test_api_error_503(self, mock_model):
        """
        Test case: API returns a 503 error.
        Expect a 503 status code and a specific error message.
        """
        mock_model_instance = mock_model.return_value
        mock_model_instance.generate_content.side_effect = MockHttpError(503)

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.content.decode(), "Service unavailable. Please try again later.")

    @patch('google.generativeai.GenerativeModel')
    def test_title_generation_failure(self, mock_model):
        """
        Test case: Title generation fails.
        Expect a 511 status code and a specific error message indicating unsafe content.
        """
        mock_model_instance = mock_model.return_value
        # Simulate a blocked response for the title generation
        mock_model_instance.generate_content.side_effect = [mock_response("Blocked Title", {"block_reason": "Unsafe content"}), mock_response("This is a valid summary.", {})]

        response = self.client.post(self.url, {'transcript': 'This is a test transcript.'})
        self.assertEqual(response.status_code, 511)
        self.assertEqual(response.content.decode(), "Unsafe transcript provided")


def mock_response(text, feedback):
    """
    Helper function to create a mock response object.
    Simulates the response structure from the generative AI model.
    """
    class MockResponse:
        def __init__(self, text, feedback):
            self.text = text
            self.prompt_feedback = feedback
            self.finishReason = 'complete'

    return MockResponse(text, feedback)
