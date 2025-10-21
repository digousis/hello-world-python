import unittest
from unittest.mock import patch
from io import StringIO
import sys
from helloworld import execute_process


class TestHelloWorld(unittest.TestCase):

    def test_execute_process_prints_hello_world(self):
        """Test that execute_process prints 'Hello world' to stdout."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            execute_process()
            self.assertEqual(fake_out.getvalue().strip(), "Hello world")


if __name__ == "__main__":
    unittest.main()