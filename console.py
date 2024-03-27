#!/usr/bin/python3
"""
The entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        to exit the program
        """
        return True

    def help_quit(self, arg):
        """
        default action
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        to exit the program
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
