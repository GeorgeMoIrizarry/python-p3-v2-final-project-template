# lib/models/company.py
#Create list with both company divisions, connect self id, READ ONLY class, make it possible to gain all employees
#and cars under division, add division id to cars and employees so that they belong to company division, add find,
#method to division only accessible to managers that can see companies whole employee and car set up
from models.__init__ import CONN, CURSOR

class Company:
    all = []
    db_dict = {}
    def __init__(self, name, id=None):
        self.name = name
        self.id = id
    
    @property
    def name(self):
        return self._name
    @name.setter 
    def name(self, name):
        if isinstance(name, str):
            self._name = f"Divison : {name}"
        else:
            raise ValueError("Names are preapproved, if this error appears then refer to the companies IT department.")
    @classmethod
    def create_company_table(cls):
        #Create table
        sql = """
            CREATE TABLE IF NOT EXISTS divisions (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        #Drop table as soon as program starts
        sql = """
        DROP TABLE IF EXISTS divisions;
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def create(cls, name):
        division = cls(name)
        division.save()
        cls.db_dict[division.id] = division
        return division
    def save(self):
        #Saving class instance into database row
        sql = """
            INSERT INTO divisions (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all.append(self)
        type(self).db_dict[self.id] = self
    @classmethod
    def db_row_to_instance(cls, row):
        division = cls.db_dict.get(row[0])
        if division:
            division.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            division = cls(row[1])
            division.id = row[0]
            cls.db_dict[division.id] = division
        return division
    @classmethod
    def find_all_divisions(cls):
        sql = """
            SELECT * FROM divisions
        """
        rows = CURSOR.execute(sql)
        return [cls.db_row_to_instance(n) for n in rows]
    @classmethod
    def find_by_id_div(cls, id):
        sql = """
            SELECT * FROM divisions
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.db_row_to_instance(row)
    @classmethod
    def find_all_department_employees(cls, id):
        #Import employee table and search with department id
        from models.employee import Employee
        sql = """
            SELECT * FROM employees
            WHERE division_id = ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        return [Employee.db_row_to_instance(n) for n in rows]
    @classmethod
    def find_all_department_cars(cls, id):
        #Import car table and search with department id
        from models.car import Car
        sql = """
            SELECT * FROM cars
            WHERE division_id = ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        return [Car.db_row_to_instance(n) for n in rows]
