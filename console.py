import cmd
import sys
from models.base_model import BaseModel
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
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[args[0] + "." + args[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except NameError:
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
        try:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist ")

    def do_all(self, arg):
        """prints all string representation of all instances"""
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            try:
                class_name = arg.split()[0]
                if class_name not in storage.classes():
                    raise NameError
                print([str(obj) for key, obj in objs.items() if key.split('.')[0] == class_name])
            except NameError:
                print("** class doesn't exist **")

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
        try:
            obj = storage.all()[args[0] + "." + args[1]]
            setattr(obj, args[2], args[3].strip('"'))
            storage.save()
        except KeyError:
            print("** no instance found")
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
