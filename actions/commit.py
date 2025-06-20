import modules.repo as repo
from modules.util import check_for_repo

def main(args):
    check_for_repo()

    message = len(args) >= 1 and args[0] or None
    if message is None:
        message = input("Enter commit message: ")
    
    print(f"Starting commit '{message}'")
    repo.createCommit(message, True)