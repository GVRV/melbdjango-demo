from unittest import TestCase

from thejoke import punchline

class TestJoke(TestCase):
    def test_is_string(self):
        s = punchline()
        self.assertTrue(isinstance(s, basestring))
