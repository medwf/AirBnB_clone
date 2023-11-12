#!/usr/bin/python3
"""import models"""
from unittest import TestCase
from unittest.mock import patch
import unittest
from io import StringIO
from console import HBNBCommand


class Test_Console(TestCase):
    """Test console"""

    def test_Prompte(self):
        """Test promple"""
        a = HBNBCommand.prompt
        self.assertEqual("(hbnb) ", a)

        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue()
            self.assertEqual("", output)

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
            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help"))

            """test help shold't print:"""
            docer = "Undocumented commands:"
            self.assertNotIn(docer, output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue()
            """test help shold print:"""
            doc = "Creates a new instance of BaseModel, and prints the id\n"
            self.assertEqual(doc, output)

    def test_QuitCommand(self):
        """test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()

            """test help shold print:"""
            doc = "quit to EXIT The program\n"
            self.assertEqual(doc, output)

            """shold not exit program"""
            self.assertFalse(HBNBCommand().onecmd("help quit"))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))


if __name__ == "__main__":
    unittest.main()
