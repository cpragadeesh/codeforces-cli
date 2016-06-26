import unittest
import subprocess
from context import CodeforcesCLI

class TestRun(unittest.TestCase):

    def test_608a_correct_cplusplus(self):
        obj = CodeforcesCLI("test_programs/608a.cpp")

        obj.file_name = "608a"
        obj.file_output = "test_programs/608a.out"

        obj.test_cases = [['3 7\n2 1\n3 8\n5 2\n', '11\n'], ['5 10\n2 77\n3 33\n8 21\n9 12\n10 64\n', '79\n']]
        self.assertEqual(obj.run_all_test_cases(), 0)
        
    def test_608a_incorrect_cplusplus(self):
        obj = CodeforcesCLI("test_programs/608a.cpp")

        obj.file_name = "608a"
        obj.file_output = "test_programs/608a.out"

        obj.test_cases = [['3 7\n2 1\n3 8\n5 2\n', '11\n'], ['5 10\n2 77\n3 33\n8 21\n9 12\n10 64\n', '76\n']]
        self.assertEqual(obj.run_all_test_cases(), 1)

if __name__ == "__main__":
    unittest.main()
