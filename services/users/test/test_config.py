import unittest

from project import app


class ConfigTest(unittest.TestCase):
    def test_config(self):
        self.assertTrue(app.config.get('TESTING'))
        self.assertIsNotNone(app.config.get('SQLALCHEMY_DATABASE_URI'))
        self.assertIsNotNone(app.config.get('SECRET_KEY'))
