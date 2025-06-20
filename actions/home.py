from colorama import Fore, Style

def main(args):
    print(f"{Style.BRIGHT + Fore.LIGHTBLUE_EX}Welcome to the mvcs CLI.{Style.RESET_ALL}")
    print("To use mvcs, run one of the following commands: \n")

    print(f"{Fore.WHITE + Style.BRIGHT}start a working area: ")
    print(f"     {Fore.GREEN + Style.BRIGHT}clone <url> <destination>{Style.RESET_ALL} - Clone a repository from the given URL to the specified destination.")
    print(f"     {Fore.GREEN + Style.BRIGHT}init{Style.RESET_ALL} - Initializes an mvcs repository in the current directory.")

    print(f"\nTo get help, run {Fore.GREEN + Style.BRIGHT}mvcs help{Style.RESET_ALL} to get an overview of mvcs or run {Fore.GREEN + Style.BRIGHT}mvcs help <command>{Style.RESET_ALL} to get help on a specific command.")