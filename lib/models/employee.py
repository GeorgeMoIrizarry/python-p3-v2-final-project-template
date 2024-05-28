# lib/models/employee.py
import ipdb 
class Employee:
    def __init__(self, name, age, time_at_company=0, id=None):
        self.name = name
        self.age = age
        self.time_at_company = time_at_company
        self.id = id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 3:
            self._name = name
        else:
            raise ValueError("Oops! Your name must contain no numbers and must be longer than three characters! ")
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 
