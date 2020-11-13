import unittest
import abc181d

class TestAbc181d(unittest.TestCase):
    def test_answer(self):
        self.assertEqual("Yes", abc181d.answer("1234"))
        self.assertEqual("No", abc181d.answer("1333"))
        self.assertEqual("Yes", abc181d.answer("8"))