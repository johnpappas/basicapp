from unittest import TestCase

import basicapp

class TestIcelandicReadingStatement(TestCase):
    def test_icelandic_reading_statement_string(self):
        s = basicapp.reading()
        self.assertTrue(isinstance(s, basestring))