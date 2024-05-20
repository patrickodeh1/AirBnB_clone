#!/usr/bin/python3
"""console.py"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """defines hbnb console"""

    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

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
        if not arg:
            print("** class name missing **")
            return
        if arg not in models.storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = models.storage.classes()[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Retrieve all instances of a class by using: <class name>.all()"""
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        instances = [str(obj) for key, obj in all_objects.items(
            ) if key.startswith(class_name + '.')]
        print(instances)

    def do_count(self, class_name):
        """Retrieve the number of instances of a class by using:
            <class name>.count()"""
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        count = sum(1 for key in all_objects if key.startswith(
            class_name + '.'))
        print(count)

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = models.storage.all()[key]
        if hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            attribute_value = attribute_type(attribute_value)
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def default(self, line):
        """Override the default method to handle class-specific commands."""
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1].strip('()')

            if command == 'all':
                self.do_all(class_name)
            elif command == 'count':
                self.do_count(class_name)
            else:
                print(f"*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
