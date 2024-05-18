#!/usr/bin/python3
"""console.py"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """defines hbnb console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = globals()[arg]()
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        try:
            obj = storage.all()[f"{cls_name}.{cls_id}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        try:
            del storage.all()[f"{cls_name}.{cls_id}"]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist ")

    def do_all(self, arg):
        """prints all string representation of all instances"""
        if arg:
            try:
                class_name = globals([arg])
                objs = [str(obj) for obj in storage.all().values()
                        if isinstance(obj, class_name)]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_update(self, arg):
        """updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        cls_name, cls_id, attr_name, attr_value = args
        try:
            obj = storage.all()[f"{cls_name}.{cls_id}"]
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(attr_value))
            else:
                setattr(obj, attr_name, attr_value)
            obj.save()
        except KeyError:
            print("** no instance found")
        except Exception:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
