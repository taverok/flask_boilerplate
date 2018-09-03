import unittest

from . import cli


@cli.command()
def test_all():
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    return 0 if result.wasSuccessful() else 1
