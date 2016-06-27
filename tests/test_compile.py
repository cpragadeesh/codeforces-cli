import unittest
import subprocess

from context import CodeforcesCLI

class TestCompile(unittest.TestCase):
    """Tests to test compile method"""
    def test_cplusplus_without_options(self):
        obj = CodeforcesCLI("g++", "test_programs/test_program.cpp")
        obj.file_output_name = "test_program.out"
        obj.file_output_extn = ".out"
        self.assertEqual(obj.compile(), 0)
        subprocess.call(["rm", "test_program.out"])

    def test_cplusplus_with_options(self):
        obj = CodeforcesCLI("g++", "test_programs/test_program.cpp", "-std=c++14")
        obj.file_output_name = "test_program.out"
        obj.file_output_extn = ".out"
        self.assertEqual(obj.compile(), 0)
        subprocess.call(["rm", "test_program.out"])

    def test_raise_exception(self):
        obj = CodeforcesCLI("g++", "test_programs/test_program.cpp", "-std=c+")
        obj.file_output_name = "test_program.out"
        obj.file_output_extn = ".out"
        self.assertRaises(RuntimeError, obj.compile)

        obj = CodeforcesCLI("g++", "test_programs/test_program", "-std=c++14")
        obj.file_output_name = "test_program.out"
        obj.file_output_extn = ".out"
        self.assertRaises(RuntimeError, obj.compile)

if __name__ == "__main__":
    unittest.main()
