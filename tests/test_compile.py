import unittest
import subprocess

from context import CodeforcesCLI

class TestCompile(unittest.TestCase):
    """Tests to test compile method"""
    def test_cplusplus(self):
        obj = CodeforcesCLI("test_program.cpp")
        self.assertEqual(obj.compile(), 0)
        subprocess.call(['rm', 'a.out'])

if __name__ == "__main__":
    unittest.main()
