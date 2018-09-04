import unittest

from project import create_app


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_default_page(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)
