import modules.repo as repo

def main(args):
    message = len(args) >= 1 and args[0] or None
    if message is None:
        message = input("Enter commit message: ")
    
    print(f"Starting commit '{message}'")
    repo.createCommit(message, True)