import requests
from time import sleep

def tryGetFromList(list, index):
    """
    Tries to get an element from a list at the specified index.
    If the index is out of range, returns None.
    """
    try:
        return list[index]
    except IndexError:
        return None

def main(args):
    link = tryGetFromList(args, 0)
    dest = tryGetFromList(args, 1)

    if link is None:
        return print("error: you must provide a link to clone a repository.")
    
    #if dest is None:
        #return print("error: you must provide a destination to clone the repository to.")


    print(f"Fetching {link}...")
    mvcsFile = requests.get(link).json()