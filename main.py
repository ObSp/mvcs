from actions.Actions import Actions
import modules.user as user
import sys

from modules.util import make_green, print_error


def main():
    args = sys.argv[1:]
    command = args[0] if args else "home"

    #check if user exists before anything else
    if user.findUser() is None and command != "user":
        print("Welcome to mvcs! Please run 'mvcs user init' to create your user.")
        return

    other_args = args[1:]

    if not command in Actions.actionList:
        return print_error(f"mvcs '{command}' is not a mvcs command. See '{make_green("mvcs help")}'.")
    
    Actions.actionList[command].main(other_args)


if __name__ == "__main__": 
    main()