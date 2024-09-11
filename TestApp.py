import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class TestApp(TestCase):

    def create_app(self):
        # Configure the application for testing
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Setup before each test
        self.client = self.app.test_client()

    def tearDown(self):
        # Cleanup after each test
        pass

    def test_index(self):
        # Test the main route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Request for index page received', response.data)

    def test_favicon(self):
        # Test the favicon route
        response = self.client.get('/favicon.ico')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/vnd.microsoft.icon')

    def test_result_no_file(self):
        # Test the result route without a file
        response = self.client.post('/result', data={})
        self.assertEqual(response.status_code, 302)  # Redirects to the main page

    def test_result_with_docx(self):
        # Test the result route with a DOCX file
        with open('test_files/test.docx', 'rb') as file:
            response = self.client.post('/result', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Request for result page received with file', response.data)

    def test_result_with_pdf(self):
        # Test the result route with a PDF file
        with open('test_files/test.pdf', 'rb') as file:
            response = self.client.post('/result', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Request for result page received with file', response.data)

    def test_result_with_txt(self):
        # Test the result route with a TXT file
        with open('test_files/test.txt', 'rb') as file:
            response = self.client.post('/result', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Request for result page received with file', response.data)

    def test_result_with_pptx(self):
        # Test the result route with a PPTX file
        with open('test_files/test.pptx', 'rb') as file:
            response = self.client.post('/result', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Request for result page received with file', response.data)

    def test_result_with_image(self):
        # Test the result route with an image file
        with open('test_files/test.jpg', 'rb') as file:
            response = self.client.post('/result', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Request for result page received with file', response.data)

    def test_handle_exception(self):
        # Test the exception handling
        with self.assertRaises(Exception):
            response = self.client.get('/nonexistent_route')
            self.assertEqual(response.status_code, 500)
            self.assertIn(b'Oops... we had a problem and could not analyze the document. Please try again later', response.data)

if __name__ == '__main__':
    unittest.main()