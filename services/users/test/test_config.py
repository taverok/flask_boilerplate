import unittest

from project import create_app


class ConfigTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()

    def test_config(self):
        self.assertTrue(self.app.config.get('TESTING'))
        self.assertIsNotNone(self.app.config.get('SQLALCHEMY_DATABASE_URI'))
        self.assertIsNotNone(self.app.config.get('SECRET_KEY'))
