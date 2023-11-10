#!/usr/bin/python3
"""import cmd model
    import sys for non-interactive mode
    import User
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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
                Ex: all BaseModel or $ all.
        update:  Updates an instance based on the class name
                and id by adding or updating attribute
                (save the change into the JSON file). Ex:
                update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        CheckType: a function that check type value of attribute
                in update method
        PrintErr: a function that handle error and check input
                from console.
    """
    prompt = ""
    if (sys.stdin.isatty() and sys.stdout.isatty()):
        prompt = "(hbnb) "

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
        if self.PrintErr(args, False, False):
            if args[0] == "BaseModel":
                new_obj = BaseModel()
            elif args[0] == "User":
                new_obj = User()
            elif args[0] == "Place":
                new_obj = Place()
            elif args[0] == "State":
                new_obj = State()
            elif args[0] == "City":
                new_obj = City()
            elif args[0] == "Amenity":
                new_obj = Amenity()
            elif args[0] == "Review":
                new_obj = Review()
            print(new_obj.id)
            new_obj.save()

    def do_show(self, line):
        """Prints the string representation of an instance
                based on the class name and id
        """
        args = line.split(" ")
        if self.PrintErr(args, True, False):
            key = f"{args[0]}.{args[1]}"
            print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(" ")
        if self.PrintErr(args, True, False):
            key = f"{args[0]}.{args[1]}"
            del storage.all()[key]
            storage.save()

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

    def do_update(self, line):
        """Updates an instance based on the class name
                and id by adding or updating attribute
                (save the change into the JSON file)
            Usage: update <className> <id> <attrName> "<attrValue>"
        """
        args = line.split(" ")
        if self.PrintErr(args, True, True):
            key = f"{args[0]}.{args[1]}"
            value = self.CheckType(args[3])
            setattr(storage.all()[key], args[2], value)
            storage.save()

    def CheckType(self, value):
        """method that check type of value [str, int, float]"""
        if "'" in value or '"' in value:
            Value = str(value)[1:-1]
        elif "." in value:
            Value = float(value)
        else:
            Value = int(value)
        return Value

    def PrintErr(self, args, check_id, check_att_value):
        """this method for handling error"""
        # print(args)
        NumArg = len(args)
        IsKey = False
        Classes = {"BaseModel", "User", "Place",
                   "State", "City", "Amenity", "Review"}
        # check id and name class
        try:
            key = f"{args[0]}.{args[1]}"
            keys = storage.all().keys()
            if key in keys:
                IsKey = True
        except Exception:
            pass
        #  print(NumArg)
        if NumArg == 1 and len(args[0]) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in Classes:
            print("** class doesn't exist **")
            return False
        elif check_id and NumArg < 2:
            print("** instance id missing **")
            return False
        elif check_id and not IsKey:
            print("** no instance found **")
            return False
        elif check_att_value and NumArg < 3:
            print("** attribute name missing **")
            return False
        elif check_att_value and NumArg < 4:
            print("** value missing **")
            return False
        return True

    def default(self, line):
        """This methods execute all instances by class name"""
        class_name = line.split(".")[0]
        command = line.split("(")[0].split(".")[1]
        _id = line.split("(")[1].split(")")[0]

        # print(class_name, command)
        if command == "all":
            self.do_all(class_name)

        if command == "all":
            self.do_all(class_name)
        elif command == "count":
            count = 0
            all_obj = storage.all()
            for cls_id in all_obj.keys():
                if class_name == cls_id.split(".")[0]:
                    count += 1
            print(count)
        elif command == "show":
            new_line = f"{class_name} {_id}"
            # print(new_line)
            self.do_show(new_line)
        elif command == "destroy":
            new_line = f"{class_name} {_id}"
            self.do_destroy(new_line)


# Make kay by using args: f"{args[0]}.{args[1]}"
if __name__ == '__main__':
    HBNBCommand().cmdloop()
