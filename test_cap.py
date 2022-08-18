import unittest
import cap
class Test(unittest.TestCase):
    def test_one(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
    def test_multi(self):
        text = 'python monty'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python Monty')
if __name__=="__main__":
    unittest.main()