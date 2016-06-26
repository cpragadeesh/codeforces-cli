import unittest
import subprocess

from context import CodeforcesCLI

class TestCompile(unittest.TestCase):
    """Tests to test compile method"""
    def test_cplusplus(self):
        obj = CodeforcesCLI("test_programs/test_program.cpp")
        obj.file_name = "test_program"
        obj.file_extn = ".cpp"
        obj.file_output = "test_program.out"
        subprocess.call(["rm", "test_program.out"])
        self.assertEqual(obj.compile(), 0)

if __name__ == "__main__":
    unittest.main()
