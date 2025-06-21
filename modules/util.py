import os

from colorama import Fore, Style

def print_error(message: str):
    print(f"{Fore.RED + Style.BRIGHT}ERROR: {Style.RESET_ALL}{message}")

def make_red(message: str):
    return f"{Fore.RED + Style.BRIGHT}{message}{Style.RESET_ALL}"

def make_green(message: str):
    return f"{Fore.GREEN + Style.BRIGHT}{message}{Style.RESET_ALL}"

def make_white(message: str):
    return f"{Fore.WHITE + Style.BRIGHT}{message}{Style.RESET_ALL}"

def check_for_repo():
    if os.path.exists(".mvcs"): return

    print_error("You must initialize a mvcs repository before using this command.")
    print(make_green("TO INITIALIZE: ") + "mvcs init")
    exit()