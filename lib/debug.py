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
    Employee.create("George", 21, "ILuvPizza@", "true", Lancaster.id, 3)
    Employee.create("Manny", 19, "Heyo@", "false", Lancaster.id, 2)
    Employee.create("Fonso", 20, "Wowow@", "false", York.id, 1)
    Employee.create("Victor", 20, "worldwide@", "false", York.id, 4)
    Employee.create("Abigail", 20, "password@", "false", Lancaster.id, 9)
    Employee.create("Nerida", 20, "max@", "false", Lancaster.id, 7)
    Employee.create("Giovanni", 20, "1234@", "true", York.id, 10)
    Employee.create("Marializ", 20, "bigM@", "false", York.id, 3)
    Employee.create("Hector", 20, "fre@mind", "false", Lancaster.id, 6)
    Car.create(2003, "Honda", "Sedan", Lancaster.id)
    Car.create(1994, "Toyota", "SUV", Lancaster.id)
    Car.create(2007, "Rolls-Royce", "SUV", Lancaster.id)
    Car.create(2021, "KTM", "Coupe", Lancaster.id)
    Car.create(2010, "Fiat", "Coupe", Lancaster.id)
    Car.create(2002, "Kia", "Sedan", Lancaster.id)
    Car.create(2011, "BMW", "Coupe", Lancaster.id)
    Car.create(2011, "Mazda", "Sedan", Lancaster.id)
    Car.create(1997, "Ford", "Truck", York.id)
    Car.create(2023, "Toyota", "SUV", York.id)
    Car.create(2015, "BMW", "SUV", York.id)
    Car.create(2001, "Honda", "Sedan", York.id)
    Car.create(2004, "Honda", "Sedan", York.id)
    Car.create(2015, "Fiat", "Sedan", York.id)
    Car.create(2015, "Nissan", "SUV", York.id)
    Car.create(2008, "Kia", "SUV", York.id)
    Car.create(2006, "Nissan", "SUV", Lancaster.id)
    Car.create(2009, "Honda", "Coupe", Lancaster.id)
    Car.create(2013, "Toyota", "Truck", York.id)
    Car.create(2023, "BMW", "Sedan", York.id)
    Car.create(1989, "Ford", "Truck", York.id)
    Car.create(2012, "Ford", "Truck", York.id)
seed()


