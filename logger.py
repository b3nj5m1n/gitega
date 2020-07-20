from colorama import init as cinit
from colorama import Fore, Back, Style


class logger:
    def __init__(self):
        cinit()

    @staticmethod
    def log(message, type="info"):
        print(Fore.RED + message)

