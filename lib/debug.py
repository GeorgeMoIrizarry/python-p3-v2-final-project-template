#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.employee import Employee
Employee.drop_table()
Employee.create_table()
George = Employee.create("Geo", 21, "jok@e", "true", 3)
Manny = Employee.create("Manny", 19, "Heyo@", "false", 1)
Fonso = Employee.create("Fonso", 20, "Wowow@", "false", 2)
ipdb.set_trace()
