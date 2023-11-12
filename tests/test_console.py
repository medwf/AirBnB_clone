#!/usr/bin/python3
"""import models"""
from unittest import TestCase
from unittest.mock import patch
import unittest
from io import StringIO
from console import HBNBCommand


class Test_Console(TestCase):
    """Test console"""

    def test_HelpCommand(self):
        """test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Documented commands (type help <topic>):"
            doc2 = "========================================"
            doc3 = "EOF  all  count  create  destroy  help  quit  show  update"
            self.assertIn(doc, output)
            self.assertIn(doc2, output)

            """test help shold't print:"""
            docer = "Undocumented commands:"
            self.assertNotIn(docer, output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Creates a new instance of BaseModel, and prints the id\n"
            self.assertEqual(doc, output)


if __name__ == "__main__":
    unittest.main()
