import unittest
import subprocess
from context import CodeforcesCLI

class TestRun(unittest.TestCase):

    def test_608a_correct_cplusplus(self):
        obj = CodeforcesCLI("608a.cpp")
        subprocess.call(["cp", "./test_programs/608a_correct", "./a.out"])
        obj.test_cases = [['3 7\n2 1\n3 8\n5 2\n', '11\n'], ['5 10\n2 77\n3 33\n8 21\n9 12\n10 64\n', '79\n']]
        self.assertEqual(obj.run_all_test_cases(), 0)
        subprocess.call(["rm", "./a.out"])

    def test_608a_incorrect_cplusplus(self):
        obj = CodeforcesCLI("608a.cpp")
        subprocess.call(["cp", "./test_programs/608a_incorrect", "./a.out"])
        obj.test_cases = [['3 7\n2 1\n3 8\n5 2\n', '11\n'], ['5 10\n2 77\n3 33\n8 21\n9 12\n10 64\n', '79\n']]
        self.assertNotEqual(obj.run_all_test_cases(), 0)
        subprocess.call(["rm", "./a.out"])

if __name__ == "__main__":
    unittest.main()
