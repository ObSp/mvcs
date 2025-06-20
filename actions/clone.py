import requests
import modules.util as util

def tryGetFromList(list, index):
    """
    Tries to get an element from a list at the specified index.
    If the index is out of range, returns None.
    """
    try:
        return list[index]
    except IndexError:
        return None
    
def printUsage():
    print(f"{util.make_green("USAGE:")} mvcs clone <repository_link> <destination>")

def main(args):
    util.check_for_repo()

    link = tryGetFromList(args, 0)
    dest = tryGetFromList(args, 1)

    if link is None:
        util.print_error("You must provide a repository link.")
        printUsage()
        return
    
    if dest is None:
        util.print_error("You must provide a destination to clone the repository to.")
        printUsage()
        return


    print(f"Fetching {link}...")
    mvcsFile = requests.get(link).json()