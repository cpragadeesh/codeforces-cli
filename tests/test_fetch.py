import unittest
import subprocess

from context import CodeforcesCLI

class TestFetch(unittest.TestCase):
    """Tests to test fetch_test_cases method"""
    def test_686a(self):
        obj = CodeforcesCLI("g++", "686a.cpp")

        obj.file_name = "686a"
        obj.file_extn = ".cpp"
        obj.contest_id = "686"
        obj.problem_id = "a"

        obj.fetch_test_cases()
        valid_cases = [["5 7\n+ 5\n- 10\n- 20\n+ 40\n- 20\n", "22 1\n"], ["5 17\n- 16\n- 2\n- 98\n+ 100\n- 98\n", "3 2\n"]]
        self.assertEqual(obj.test_cases, valid_cases)

    def test_661b(self):
        obj = CodeforcesCLI("g++", "661b.cpp")

        obj.file_name = "661b"
        obj.file_extn = ".cpp"
        obj.contest_id = "661"
        obj.problem_id = "b"

        obj.fetch_test_cases()
        valid_cases = [["April\n", "spring\n"], ["November\n", "autumn\n"]]
        self.assertEqual(obj.test_cases, valid_cases)

if __name__ == "__main__":
    unittest.main()
