import modules.user as user
import modules.mvcsconfig as mvcsconfigMod

def main(args):
    """
    Creates a user in the current directory.
    """
    
    command = len(args) >= 1 and args[0] or None

    if command is None:
        print("Current user: ", user.findUser())
        print("Usage: 'mvcs user <init|set>'")
        
    elif command == "init":
        if user.findUser() is not None:
            return print("error: user already exists.")
        
        name = input("Enter your name: ")
        
        mvcsconfigMod.findOrCreateMvcsConfig()

        user.setUser(name)
        print(f"Successfully created user '{name}'.")

    elif command == "set":
        if user.findUser() is None:
            return print("error: user not found. create a user with 'mvcs user init'.")
        
        name = input("Enter your name: ")
        
        user.setUser(name)
        print(f"Successfully set user to '{name}'.")