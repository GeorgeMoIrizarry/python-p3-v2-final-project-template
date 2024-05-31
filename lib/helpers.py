# lib/helpers.py
import os
import time
from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.car import Car, APPROVED_BRANDS, APPROVED_TYPES
from models.company import Company 

 #change all employee prints to return to employee menu
def log_in():
    from cli import main
    password = input("Enter Password: ")
    if Employee.login_by_pass(password):
        USER = Employee.login_by_pass(password)
        if USER.is_manager == "true":
            manager(USER)
        else:
            employee(USER)
    else:
        return ("Wrong password, try again!")
def employee(USER):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome back employee {USER.name}!")
        if not USER.comment == None:
            print(f"{USER.comment}")
        print("Enter a number to get started on an activity.")
        print("1. View Status")
        print("2. View Vehicle Details")
        print("3. Help")
        print("4. Log Out")
        choice = input("> ")
        if choice == "1":
            employee_status(USER)
        elif choice == "2":
            car_menu(USER)
        elif choice == "3":
            help(USER)
        elif choice == "4":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def employee_status(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Hello {USER.name}! Here is the status reports that have been logged to your JUNK account!")
    print(f"Name: {USER.name}")
    print(f"Status: {'Manager' if USER._is_manager == 'true' else 'Employee'}")
    print(f"Division: {'Lancaster' if USER.division_id == 1 else 'York'}")
    print(f"Performance: {USER.performance} vehicle(s) destroyed!")
    print(f"Keep up the good work {USER.name}!")
    print("1. Go Back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        if USER.is_manager == "true":
            manager(USER)
        else:
            employee(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def manager(USER):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome back manager {USER.name}!")
        if not USER.comment == None:
            print(f"{USER.comment}")
        print("Enter a number to get started on an activity.")
        print("1. View Status")
        print("2. View Employee Details")
        print("3. View Vehicle Details")
        print("4. Help")
        print("5. Log Out")
        choice = input("> ")
        if choice == "1":
            employee_status(USER)
        elif choice == "2":
            employee_menu(USER)
        elif choice == "3":
            car_menu(USER)
        elif choice == "4":
            help(USER)
        elif choice == "5":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def car_menu(USER):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. View All Vehicles Registered In JUNK")
        print(f"2. View Division {USER.division_id} Vehicles (Filtering options included)")
        print(f"3. Manage Vehicles")
        print("4. Go back")
        print("5. Log out")
        choice = input("> ") 
        if choice == "1":
            all_cars(USER)
        elif choice == "2":
            division_menu_cars(USER)
        elif choice == "3":
            manage_vehicles(USER)
        elif choice == "4":
            if USER.is_manager == "true":
                manager(USER)
            else:
                employee(USER)
        elif choice == "5":
            log_out() 
        else:
            print("Make sure you enter a valid choice!")
def manage_vehicles(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Bring In Vehicle")
    print("2. Destroy Vehicle")
    print("3. Go Back")
    print("4. Log Out")
    choice = input("> ")
    if choice == "1":
        creation_cars(USER)
    elif choice == "2":
        #Grab all vehicles before destroying
        destroy_vehicle(USER) 
    elif choice == "3":
        car_menu(USER)
    elif choice == "4":
        log_out() 
    else:
        print("Make sure you enter a valid choice!")
def destroy_vehicle(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("In order to both log and destroy a vehicle, a vehicle ID is required.")
    print("Would you like to see the vehicles in your division?")
    question1 = input("Yes Or No?: ")
    if question1 == "No":
        id = int(input("Enter Vehicle ID: "))
    else:
        instance = Car.fetch_all_by_name_default(USER.division_id)
        for n in instance:
            print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division, Vehicle ID: {n.id}")
        id = int(input("Enter Vehicle ID: "))
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print("Success! Vehicle Was Successfully Destroyed.")
    print(f"Good Job {USER.name}! Your Performance Increased By One! Hint: Check Status In Main Menu To View Change.")
    USER.performance += 1
    USER.update_performance()
    Car.delete_by_id(id)
    time.sleep(5)
def creation_cars(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Limitations are set for setting vehicle information, follow the instructions!")
    print("Vehicle year must be a number and between 1908 and 2025.")
    year = int(input("Enter Vehicle Year: "))
    
    print("Vehicle must be in approved lists of automotive brands.")
    print("Would you like to see approved brands?")
    question1 = input("Yes Or No?: ")
    if question1 == "No":
        brand = input("Enter Brand: ")
    else:
        brands = APPROVED_BRANDS
        for n in brands:
            print(f"{n}")
        brand = input("Enter Brand: ")
    print("Vehicle must be in approved lists of automotive vehicle types.")
    print("Would you like to see approved types?")
    question2 = input("Yes Or No?: ")
    if question2 == "No":
        type = input("Enter Type: ")
    else:
        types = APPROVED_TYPES
        for n in types:
            print(f"{n}")
        type = input("Enter Type: ")
    division_id = USER.division_id
    
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print("Success! Vehicle Was Successfully Logged")
    Car.create(year, brand, type, division_id )
    time.sleep(5)
    manage_vehicles(USER)
def division_menu_cars(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. View Division Vehicles")
    print("2. Find Vehicle By Vehicle ID Hint: IDs provided in selection 1")
    print("3. View History Of Destroyed Vehicles")
    print("4. Go Back")
    print("5. Log Out")
    choice = input("> ")
    if choice == "1":
        car_filter_menu(USER)
    elif choice == "2":
        id = input("Enter Vehicle ID: ")
        find_vehicle_by_id(USER, id) 
    elif choice == "3":
        destroyed_cars(USER)
    elif choice == "4":
        car_menu(USER) 
    elif choice == "5":
        log_out() 
    else:
        print("Make sure you enter a valid choice!")
def destroyed_cars(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    destroyed = Car.destroyed
    if len(destroyed) == 0:
        print("No Destroyed Vehicles Present!")
    else:
        for n in destroyed:
            print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belonged To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
    print("1. Go back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        division_menu_cars(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")

def find_vehicle_by_id(USER, id):
    os.system('cls' if os.name == 'nt' else 'clear')
    instance = Car.find_by_id(id)
    print(f"{instance.year} {instance.brand} Vehicle Type: {instance.type} Belongs To The {'Lancaster' if instance.division_id == 1 else 'York'} Division")
    print("1. Go back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        division_menu_cars(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")

def car_filter_menu(USER):
    while True:  
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"1. View Vehicles belonging to the {'Lancaster' if USER.division_id == 1 else 'York'} Division")
        print("2. View Vehicles Based On Vehicle Year")
        print("3. View Vehicles By Vehicle Type Hint: Selection 5 Shows Approved Vehicle Types")
        print("4. View Vehicles By Brand Hint: Selection 6 Shows Approved Brands")
        print("5. Approved Vehicle Types")
        print("6. Approved Vehicle Brands")
        print("7. Go back")
        print("8. Log Out")

        choice = input("> ")
        if choice == "1":
            car_division(USER)
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            vehicle_list_by_year(USER) 
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            vehicle_list_by_type(USER)
        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            vehicle_list_by_brand(USER)
             
        elif choice == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            types = APPROVED_TYPES
            for n in types:
                print(f"{n}")
            print("Enter One Of These Approved Types In Selection 3")
            input("Enter 'OK' To Return: ")
        elif choice == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            brands = APPROVED_BRANDS
            for n in brands:
                print(f"{n}")
            print("Enter One Of These Approved Brands In Selection 4")
            input("Enter 'OK' To Return: ")
        elif choice == "7":
            division_menu_cars(USER)
        elif choice == "8":
            log_out() 
        else:
            print("Make sure you enter a valid choice!")

def vehicle_list_by_brand(USER):
    while True:
        print("1. Grab Vehicles Based On Brand")
        print("2. Go Back")
        print("3. Log Out")
        choice = input("> ")
        if choice == "1":
            brand = input("Enter Vehicle Brand: ")
            instance = Car.find_by_brand(brand, USER.division_id)
            for n in instance:
                print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
        elif choice == "2":
            car_filter_menu(USER)
        elif choice == "3":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def vehicle_list_by_type(USER):
    while True:
        print("1. Grab Vehicles Based On Vehicle Type")
        print("2. Go Back")
        print("3. Log Out")
        choice = input("> ")
        if choice == "1":
            type = input("Enter Vehicle Type: ")
            instance = Car.find_by_type(type, USER.division_id)
            for n in instance:
                print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
        elif choice == "2":
            car_filter_menu(USER)
        elif choice == "3":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def vehicle_list_by_year(USER):
    while True:
        print("1. Grab All Vehicles With The Same Year")
        print("2. Grab Vehicles Oldest To Youngest")
        print("3. Grab Vehicles Youngest To Oldest")
        print("4. Go Back") 
        print("5. Log Out")
        choice = input("> ") 
        if choice == "1":
            year = int(input("Enter Vehicle Year: "))
            instance = Car.find_by_year_asc(year, USER.division_id)
            for n in instance:
                print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
        elif choice == "2":
            instance = Car.alternate_year_desc(USER.division_id)
            for n in instance:
                print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
        elif choice == "3":
            instance = Car.alternate_year_asc(USER.division_id)
            for n in instance:
                print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
        elif choice == "4":
            car_filter_menu(USER)
        elif choice == "5":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def car_division(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    instance = Car.fetch_all_by_name_default(USER.division_id)
    for n in instance:
        print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division, Vehicle ID: {n.id} ")
    print("1. Go back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        car_filter_menu(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")


def all_cars(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    instances = Car.find_all_cars()
    for n in instances:
        print(f"{n.year} {n.brand} Vehicle Type: {n.type} Belongs To The {'Lancaster' if n.division_id == 1 else 'York'} Division")
    print("1. Go back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        car_menu(USER)
    elif choice == "2":
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
            division_menu(USER)
        elif choice == "3":
            manager(USER)
        elif choice == "4":
            log_out()
        else:
            print("Make sure you enter a valid choice!")
def division_menu(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. View Division Employees")
    print("2. Find Employee By Employee ID Hint: IDs provided in selection 1")
    print("3. Find The Star Employee!")
    print("4. Go Back")
    print("5. Log Out")
    choice = input("> ")
    if choice == "1":
        division_employee_menu(USER)
    elif choice == "2":
        inputO = input("Enter Employee ID: ")
        grab_employee_id(USER, inputO)
    elif choice == "3":
        star_employee(USER)
    elif choice == "4":
        employee_menu(USER)
    elif choice == "5":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def star_employee(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    instance = Employee.find_by_highest_performance(USER.division_id)
    print(f"Employee {instance.name} has the highest performance! They destroyed {instance.performance} vehicles!")
    print("1. Want To Leave A Comment To Congratulate Them?")
    print("2. Go Back")
    print("3. Log Out")
    choice = input("> ")
    if choice == "1":
        comment = input("Enter your comment: ")
        instance.comment = f"Manager {USER.name} would like to say: {comment}"
        instance.update()
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        print("Success! Sending you back to the previous menu...")
        time.sleep(2)
        division_menu(USER)
    elif choice == "2":
        division_menu(USER)
    elif choice == "3":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def grab_employee_id(USER, inputO):
    os.system('cls' if os.name == 'nt' else 'clear')
    instance = Employee.find_by_id(inputO)
    print(f"Employee name: {instance.name}, Status: {'Manager' if instance._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if instance.division_id == 1 else 'York'}, Employee Performance: {instance.performance}")
    print("1. Go back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        division_menu(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def division_employee_menu(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Filter Options Below:")
    print(f"1. List Employees In {'Lancaster' if USER.division_id == 1 else 'York'} Division")
    print("2. List Employees By Time")
    print("3. List Employees By Performance")
    print("4. Go Back")
    print("5. Log Out")
    choice = input("> ")
    if choice == "1":
        list_division(USER)
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        alternate_between_lists_by_time(USER)
    elif choice == "3":
        list_by_per(USER)
    elif choice == "4":
        division_menu(USER)
    elif choice == "5":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def list_division(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    instances = Employee.list_high_per(USER.division_id)
    for n in instances:
        print(f"Employee name: {n.name}, Status: {'Manager' if n._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if n.division_id == 1 else 'York'} Employee ID: {n.id}")
    print("1. Go Back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        division_employee_menu(USER)
    elif choice == "2":
        log_out()
    else:
        print("Make sure you enter a valid choice!")
def alternate_between_lists_by_time(USER):
    while True:
        print("1. Longest To Shortest Time Desc")
        print("2. Shortest To Longest Time Asc")
        print("3. Go Back")
        print("4. Log Out")
        choice = input("> ")
        if choice == "1":
            instances = Employee.alternate_between_lists_asc(USER.division_id)
            for n in instances:
                print(f"Employee name: {n.name}, Status: {'Manager' if n._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if n.division_id == 1 else 'York'} Employee Time: {n.time_at_company} years")
        elif choice == "2":
            instances = Employee.alternate_between_lists_desc(USER.division_id)
            for n in instances:
                print(f"Employee name: {n.name}, Status: {'Manager' if n._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if n.division_id == 1 else 'York'} Employee Time: {n.time_at_company} years")
        elif choice == "3":
            division_employee_menu(USER)
        elif choice == "4":
            log_out()
        else:
            print("Make sure you enter a valid choice!")

def list_by_per(USER):
    os.system('cls' if os.name == 'nt' else 'clear')
    instances = Employee.list_high_per(USER.division_id)
    for n in instances:
        print(f"Employee name: {n.name}, Status: {'Manager' if n._is_manager == 'true' else 'Employee'}, Division: {'Lancaster' if n.division_id == 1 else 'York'} Cars Destroyed {n.performance}")
    print("1. Go Back")
    print("2. Log Out")
    choice = input("> ")
    if choice == "1":
        division_employee_menu(USER)
    elif choice == "2":
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
        if USER.is_manager == "true":
            manager(USER)
        else:
            employee(USER)
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
