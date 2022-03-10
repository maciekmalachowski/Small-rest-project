import unittest
from django.test import TestCase
from rest_framework.test import RequestsClient

class TestUrl(TestCase):
    def test_url_base(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_url_single(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_url_many(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/0/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

if __name__ == '__main__':
    unittest.main()