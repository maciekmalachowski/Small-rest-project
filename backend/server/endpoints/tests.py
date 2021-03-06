import unittest
from django.test import TestCase
from rest_framework.test import RequestsClient

class TestUrl(TestCase):
    def test_base(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_single(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_many(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/0/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
    
    def test_url_incomplite_link(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 404)

    def test_url_single_minus_value(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/-1')
        self.assertEqual(response.status_code, 400)

    def test_url_single_not_int(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/a')
        self.assertEqual(response.status_code, 400)

    def test_url_intmin_bigger_than_intmax(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/2/1')
        self.assertEqual(response.status_code, 400)
    
    def test_url_intmax_minus_value(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/1/-1')
        self.assertEqual(response.status_code, 400)

    def test_url_intmin_minus_value(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/-1/1')
        self.assertEqual(response.status_code, 400)
    
    def test_url_many_not_int(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/get-data/a/b')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()