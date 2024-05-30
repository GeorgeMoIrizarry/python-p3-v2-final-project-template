# lib/helpers.py
import os
import time
from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.car import Car
from models.company import Company

 #update row after updating instance
def log_in():
    from cli import main
    password = input("Enter Password:")
    if Employee.login_by_pass(password):
        USER = Employee.login_by_pass(password)
        if USER.is_manager == "true":
            manager(USER)
        else:
            print("You're an employee!")
    else:
        print("Wrong password, returning to main page.")
def manager(USER):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome back manager {USER.name}!")
        print("Enter a number to get started on an activity.")
        print("1. View Employee Details")
        print("2. Manage Vehicles")
        print("3. Help")
        print("4. Log Out")
        choice = input("> ")
        if choice == "1":
            employee_menu(USER)
        elif choice == "2":
            pass
        elif choice == "3":
            help(USER)
        elif choice == "4":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def employee_menu(USER):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. View All Employees Registered In JUNK")
        print(f"2. View Division {USER.division_id} Employees (Filtering options included)")
        print("3. Go back")
        print("4. Log out")
        choice = input("> ") 
        if choice == "1":
            all_employees(USER)
        elif choice == "2":
            pass
        elif choice == "3":
            manager(USER)
        elif choice == "4":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def all_employees(USER):
        os.system('cls' if os.name == 'nt' else 'clear')
        instances = Employee.find_all_employees()
        for n in instances:
            print(f"Employee name: {n.name}, Status: {'Manager' if n._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if n.division_id == 1 else 'York'}")
        print("1. Go Back")
        print("2. Log Out")
        choice = input("> ")
        if choice == "1":
            employee_menu(USER)
        elif choice == "2":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def help(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("If you need help navigating this CLI terminal, refer to the README.md file for assistance.")
    print("Report any bugs to the G.I. Junking's offical IT support team. ")
    print("1. Go Back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        manager(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def sign_up():
    print("Limitations are set for account setting, follow the instructions!")
    print("Name must not include special characters or numbers.")
    name = input("Enter Your Name:")
    
    print("Age documentation required for safety concerns. Must be a proper number.")
    age = int(input("Age:"))
    
    print("WARNING: Password cannot be changed, manager will have to delete account. Password must contain an @ symbol.")
    password = input("Enter Password:")
    
    print("WARNING: False input of manager status causes immediate termination. Enter 'true' or 'false'.")
    is_manager = input("Manager Status:")
    
    print("Enter Division ID Belonging To Your Division. Hint: Lancaster = 1, York = 2")
    division_id = int(input("Enter Division ID:"))
    
    print("Enter your total time working for the G.I. Junking family! Must be a rounded yearly number.")
    time_at_company = int(input("Enter Overall Estimated Working Time:"))
    
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print("Success! Log in with your password to get started.")
    Employee.create(name, age, password, is_manager, division_id, time_at_company)
    time.sleep(5)
def log_out():
    print(f"Logging out...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
