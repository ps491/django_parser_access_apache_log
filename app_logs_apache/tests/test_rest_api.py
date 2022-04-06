from django.test import Client, TestCase


class SimpleTest(TestCase):
        
    def test_details(self):
        # Issue a GET request.
        self.client = Client()
        response = self.client.get('/api/apache_logs/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


