#!/usr/bin/env python3
# lib/debug.py
from models.employee import Employee
from models.car import Car

from models.company import Company
from models.__init__ import CONN, CURSOR
def seed():
    Company.drop_table()
    Company.create_company_table()
    Car.drop_table()
    Car.create_car_table()
    Employee.drop_table()
    Employee.create_table()
    Lancaster = Company.create("Lancaster")
    York = Company.create("York")
    George = Employee.create("Geo", 21, "jok@e", "true", Lancaster.id, 3)
    Manny = Employee.create("Manny", 19, "Heyo@", "false", Lancaster.id, 2)
    Fonso = Employee.create("Fonso", 20, "Wowow@", "false", York.id, 1)
    Car.create(2003, "Honda", "Coupe", Lancaster.id)
    Car.create(2004, "Honda", "SUV", 2)
    Car.create(2003, "Toyota", "SUV", 1)
    Car.create(2004, "Ford", "Truck", 1)
    Car.create(2003, "Honda", "Coupe", 2)
    Car.create(2009, "Kia", "Sedan", 2)
    Car.create(2003, "Kia", "Sedan", 1)



