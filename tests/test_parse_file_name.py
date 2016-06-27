import unittest

from context import CodeforcesCLI

class TestParseFileName(unittest.TestCase):

    def test_608a_cplusplus(self):
        obj = CodeforcesCLI("g++", "test_programs/608a.cpp")
        obj.parse_file_name()
        self.assertEqual(obj.file_name, "608a")
        self.assertEqual(obj.file_extn, "cpp")

    def test_raise_exception(self):
        obj = CodeforcesCLI("g++", "test_programs/608.cpp")
        self.assertRaises(RuntimeError, obj.parse_file_name)

        obj = CodeforcesCLI("g++", "test_programs/608a")
        self.assertRaises(RuntimeError, obj.parse_file_name)

if __name__ == "__main__":
    unittest.main()
