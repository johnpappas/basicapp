from unittest import TestCase

import basicapp

class TestJoke(TestCase):
    def test_is_german_joke_string(self):
        s = basicapp.joke()
        self.assertTrue(isinstance(s, basestring))