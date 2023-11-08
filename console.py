#!/usr/bin/python3
"""import cmd model
    import sys for non-interactive mode 
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

"""model HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """This file represent console by using HBNBCommand class

    Public class attribute:
        prompte (str): prompte should print.

    Public class Methodes:
        EOF: command to exit the program.
        quit: command to exit the program
        emptyline: "an empty line + ENTER" shouldn't execute anything
        create: command to Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id.
        show: Prints the string representation of an instance
                based on the class name and id.
        destroy: Deletes an instance based on the class name and id
                (save the change into the JSON file).
        all:  Prints all string representation of all instances
                based or not on the class name.
                Ex: $ all BaseModel or $ all.
        update:  Updates an instance based on the class name
                and id by adding or updating attribute 
                (save the change into the JSON file). Ex: 
                $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
    """
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
        """an empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        args = line.split(" ")
        # test argumment of command create
        # for i in range(0, len(args)):
        #     print(args[i])
        # print(args[0])
        if self.PrintErr(args, False, False):
            new_obj = BaseModel()
            print(new_obj.id)
            new_obj.save()
        # else:
        #     if len(args[0]):
        #         print("** class doesn't exist **")
        #     else:
        #         print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
                based on the class name and id
        """
        args = line.split(" ")
        if self.PrintErr(args, True, False):
            for key in storage.all().keys():
                my_id = key.split(".")[-1]
                if args[1] == my_id:
                    print(storage.all()[key])
                    return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(" ")
        if self.PrintErr(args, True, False):
            for key in storage.all().keys():
                my_id = key.split(".")[-1]
                if args[1] == my_id:
                    del storage.all()[key]
                    storage.save()
                    return

    def do_all(self, line):
        """Prints all string representation of all instances
                based or not on the class name
        """
        args = line.split(" ")
        ListObj = []
        if len(args[0]) == 0:
            for key in storage.all().keys():
                ListObj.append(str(storage.all()[key]))
            print(ListObj)
        elif self.PrintErr(args, False, False):
            for key in storage.all().keys():
                if args[0] == key.split(".")[0]:
                    ListObj.append(str(storage.all()[key]))
            print(ListObj)
        # else:
        #     print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name 
                and id by adding or updating attribute
                (save the change into the JSON file)
            Usage: update <className> <id> <attrName> "<attrValue>"
        """
        args = line.split(" ")
        if self.PrintErr(args, True, True):
            for key in storage.all().keys():
                my_id = key.split(".")[-1]
                if args[1] == my_id:
                    value = self.CheckType(args[3])
                    setattr(storage.all()[key], args[2], value)
                    storage.save()
                    break

    def CheckType(self, value):
        """method that check type of value [str, int, float]"""
        if "'" in value or '"' in value:
            Value = str(value).strip("'\"")
        elif "." in value:
            Value = float(value)
        else:
            Value = int(value)
        return Value

    def PrintErr(self, args, _id, att_value):
        """this method for handling error"""
        # print(args)
        NumArg = len(args)
        IsId = False
        # check id
        try:
            for key in storage.all().keys():
                if args[1] == key.split(".")[-1]:
                    IsId = True
        except Exception:
            pass
        #  print(NumArg)
        if NumArg == 1 and len(args[0]) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif _id and NumArg < 2:
            print("** instance id missing **")
            return False
        elif _id and not IsId:
            print("** no instance found **")
            return False
        elif att_value and NumArg < 3:
            print("** attribute name missing **")
            return False
        elif att_value and NumArg < 4:
            print("** value missing **")
            return False
        return True


# make kay: f"{args[0]}.{args[1]}"
if __name__ == '__main__':
    HBNBCommand().cmdloop()
