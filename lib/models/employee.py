# lib/models/employee.py
# ADD HOW MANY CARS HAVE BEEN PREPPED AND HOW MANY CARS HAVE BEEN DESTROYED IN INIT



from models.__init__ import CONN, CURSOR
class Employee:
    all = []
    db_dict = {}
    def __init__(self, name, age, password, is_manager, time_at_company=0, id=None):
        self.name = name
        self.age = age
        self.password = password
        self._is_manager = is_manager
        self.time_at_company = time_at_company
        self.id = id
        Employee.employee_list(self)
    @classmethod
    def employee_list(cls, employee):
        cls.all.append(employee)
    @classmethod
    def show_employee_list(cls):
        #Might not be needed as we might iterate over employee table and return a list that way
        print ([n.name for n in cls.all])
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 2:
            self._name = name
        else:
            raise ValueError("Oops! Your name must contain no numbers and must be longer than two characters! ")
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 18:
            self._age = age 
        else:
            raise ValueError("Oops! Your age must be over 18, as you'll be handling dangerous and heavy machinery. If this is a mistake on your part, please enter the correct age. If not, refer to an higher authority to handle this matter.")
    @property
    def is_manager(self):
        return self._is_manager
    @is_manager.setter
    def is_manager(self, is_manager):
        if isinstance(is_manager, str):
            is_manager.title()
            if is_manager == "True" or is_manager == "False":
               self.is_manager = is_manager.title()
        else:
            raise ValueError('To set authority status, input must be the word True or False')
    @property
    def time_at_company(self):
        return self._time_at_company
    @time_at_company.setter
    def time_at_company(self, time_at_company):
        if isinstance(time_at_company, int) and time_at_company >= 0:
            self._time_at_company = time_at_company
        else:
            raise ValueError("Oops! Time must be a number and greater than zero!")
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        if "@" in password:
            self._password = password
        else:
            raise ValueError("Oops! For security, a password must include an @ symbol.")
    @classmethod
    def create_table(cls):
        #Creates Employee table, when user "logs in", add this class method as well as the other class methods
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            password TEXT,
            is_manager TEXT,
            time_at_company INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        #drops table if table exists, less bearing to call this upon log out
        sql = """
            DROP TABLE IF EXISTS employees;
        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        #Saving class instance into database row
        sql = """
            INSERT INTO employees (name, age, password, is_manager, time_at_company)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.password, self._is_manager, self.time_at_company))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).db_dict[self.id] = self
    @classmethod
    def create(cls, name, age, password, is_manager, time_at_company):
        #This creates a new instance, attaches itself in a new row in the employees table and returns the instance
        new_employee= cls(name, age, password, is_manager, time_at_company)
        new_employee.save()
        return new_employee
    