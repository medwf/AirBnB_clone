#!/usr/bin/python3
"""import cmd model
    import sys for non-interactive mode 
"""
import cmd
import sys

"""model HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """this file represent console by using HBNBCommand class"""
    prompt = ""

    if (sys.stdin.isatty() and sys.stdout.isatty()):
        prompt = "(hbtn) "

    def do_EOF(self, line):
        """Ctrl+d To EXIT The program"""
        return True

    def do_quit(self, line):
        """quit to EXIT The program"""
        return True

    def emptyline(self):
        """    an empty line + ENTER shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

