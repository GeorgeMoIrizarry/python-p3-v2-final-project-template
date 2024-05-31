# G.I. Junking Corporation JUNK Terminal Version 1.01

## Introduction

Hello, and welcome to the README file of the G.I. Junking Corporation JUNK 
Terminal Version 1.01! This README will act as the docmentation for this
project of mine, below I will describe all of the classes, associated
methods, attributes, functions, lists, and more that are involved
in this project!

---

## cli.py

This file is hub for this project, this connects everything together to make
this project cohesive. Starting from the top, we import all of our important
files, and functions, below that we import some helper functions, and below
that is our main function, which is what starts our CLI program. Since this
is the "hub", I'll slowly go through this file and explain every bit, 
starting with __init__ import!

## __init__.py 

__init__ has two main purposes, connecting to the database while also naming 
said database and allowing us to perform actions on it. It does this by using
connect and cursor. 

## employee.py, car.py, company.py 

employee.py, car.py, and company.py are the three main files containing the
classes needed for this CLI project. All classes has many but similar CRUD ORM 
methods, dictionaries and lists that we'll go over below. We will then go into
the unique features contain within our project files.

## all

A list used for debugging purposes, contains instances. The Car class has a 
list called destroy meant to store instances that have has their rows
deleted.

## db_dict

A dictionary used to grab instances out of rows, does this by assigning
row ids to keys, and the corresponding instance as a value. Car has a 
dictionary called ALL that performs the exact same action.

## init

Init method used with creating employee, car, and division instances, 
employee init assigns name, age, password, is_manager, division_id, 
time_at_company, id, comment, performance to the new instance. Car init
assigns self, year, brand, type, division_id, id to new instances. Car and
employee has a many to one relationship with division, division being the name
of the instances constructed from the company class. Company init assigns 
a name and an id to new instances

### Property methods

Every single instance attribute in the Employee class, Car Class, and the
Company Class has getter and setter methods that applies validations to 
what can be set to the attributes of the instances those classes can
create.

## repr methods

The repr methods are used for debugging purposes, returns a cleaning 
formatted example of an instance.

## create table

The class method create table creates a table using a SQL statement which
is ran by python. The table columns are the attributes the init method
sets on the classes instances. This is set in the debug.py file, which
for this project is acting as the data seed.

## drop table

The class method drop table drops a formed data table. Used for reseting 
purposes, this method is set in the debug.py file, which for this project
is acting as the data seed

## create method

The create method is what we use to create new instances for all of the
classes. Contains the save method.

## save

The save method inserts all of the instances attributes into table cells
that correspond with the appropiate columns in the appropiate data table.
It then assigns the instance id to the id corresponding with the row the
instance was assign too, making the id unique. It then makes a key value
pair, assigning the key as the id, and instance as the value and appends it
to db_dict.

## db_row_to_instance

db_row_instance accepts a row, it then uses this rows id and passes it as 
an argument to a get method on db_dict. As mentioned before, db_dict
stores instances, the get method grabs these instances. We then make sure 
the instance information is updated by assigning the instance attributes
to the row data, IF the key value pair existed. If a row existed without
an instance assigned to it, db_row_instance will then make an instance.
We then return this instance.

## find all []

The find all class method grabs all of the rows from their appropiate
tables using a SQL statement and uses db_row_instance to return instances.

## find by id

The find by id class method passes an id arguement and searches through
the appropiate tables for a singualr row that matches that id and
passes that row into db_row_instance and returns an instance.

## find by division

The find by division class method uses the shared division id every class
has and returns rows that contain that division id, and passes those rows
into db_row_instance to return instances.

## car.py unique features

car.py has two lists, APPROVED_BRANDS, and APPROVED_TYPES, both containing values
that instance attributes brand and types can be set with.

Car class also has multiple read ORM methods that are mainly used to filter instance
results, this include: find by year ascending and decending, find by brand,
and find by type.

Car class also contains a destroy ORM method that requires a id to be passed in
as an argument. It then finds the row with the corresponding id and deletes
it. It then sets the instance that was connected to the row id to None.

## employee.py unique features

Employee class also has multiple read ORM methods that are mainly used to filter instance
results, this include: find by time at company ascending and decending, find by name,
find by performance, all and singular, find by longest at company singular, and
find by password.

Employee class also contains two ORM update methods and a delete method, 
updating comment and performance, then a similar delete method to the one
car class contains. 

## main in cli.py

Returning to cli.py, the main function starts our CLI project by setting inputs,
with printed messages explaining what every input is equating to.

---
