#Requires colorama; install with pip
from colorama import init, Fore, Style
#Initiation colorama
init(autoreset = True)
#demonstration of using the pacage
print(Fore.GREEN + "Success! The colorama package is working correctly.")
print(Fore.CYAN + Style.BRIGHT + "This is a styled and colored console output.")
