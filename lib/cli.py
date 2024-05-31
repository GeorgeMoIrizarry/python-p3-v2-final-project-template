# lib/cli.py
from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.car import Car
from models.company import Company
import os
import time

from helpers import (  
    log_in,
    sign_up,
    log_out
)  
def main():  
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        login()
        choice = input("> ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            log_in()
        elif choice == "2":
            print("WARNING: Password CANNOT be changed, employee is recommended to store password information in a safe place")
            os.system('cls' if os.name == 'nt' else 'clear')
            sign_up()
        elif choice == "3":
            log_out()
        else:
            print("Invalid choice")


def login():
    print("Hello! And Welcome To Version 1.01 Of The Official JUNK Terminal For G.I. Junking Corperation!")
    print("If You're An Employee At One Of Our Divisions With An Authorized Established Account, Then Please Log in!")
    print("Otherwise, Please Sign Up!")
    print("To Select Options, Type In Selection Numbers Unless Otherwise Specified")
    print("1. Log In")
    print("2. Sign Up")
    print("3. Exit")


if __name__ == "__main__":
    main()
