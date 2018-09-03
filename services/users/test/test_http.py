import unittest

from project import app


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_config(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)
