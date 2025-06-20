import shutil
from actions.init import steps
from modules.util import *

def printUsage():
    print(f"{make_green("USAGE:")} mvcs destroy")

def counter(steps: int, messager, callback):
    for i in range(steps):
        print('\r', str(messager(i)), end = '')
        callback(i)
    print("")

def main(args):
    """
    Destroys the mvcs repository in the current directory.
    """

    check_for_repo()
    
    answer = input(make_red("Are you sure you want to destroy the working mvcs repository? (y/n): "))
    if answer.lower() != "y":
        return print_error("Aborted destroy.")
    
    reverseSteps = steps["dirs"].copy()
    reverseSteps.reverse()

    reverseStepsL = len(reverseSteps)
    
    counter(
        reverseStepsL,
        lambda i: f"Destroying directories... [{i + 1}/{reverseStepsL}]",
        lambda i: shutil.rmtree(reverseSteps[i])
    )

    print(make_green("Successfully destroyed working mvcs repository."))