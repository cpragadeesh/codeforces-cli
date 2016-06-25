import unittest

from context import CodeforcesCLI

class TestParseFileName(unittest.TestCase):

    def test_608a(self):
        obj = CodeforcesCLI("test_program/608a.cpp")
        obj.parse_file_name()
        self.assertEqual(obj.file_name, "608a")
        self.assertEqual(obj.file_extn, "cpp")

if __name__ == "__main__":
    unittest.main()
