# lib/brands/car.py
APPROVED_BRANDS = [ 
  "Abarth",
  "Alfa Romeo",
  "Aston Martin",
  "Audi",
  "Bentley",
  "BMW",
  "Bugatti",
  "Cadillac",
  "Chevrolet",
  "Chrysler",
  "Citroën",
  "Dacia",
  "Daewoo",
  "Daihatsu",
  "Dodge",
  "Donkervoort",
  "DS",
  "Ferrari",
  "Fiat",
  "Fisker",
  "Ford",
  "Honda",
  "Hummer",
  "Hyundai",
  "Infiniti",
  "Iveco",
  "Jaguar",
  "Jeep",
  "Kia",
  "KTM",
  "Lada",
  "Lamborghini",
  "Lancia",
  "Land Rover",
  "Landwind",
  "Lexus",
  "Lotus",
  "Maserati",
  "Maybach",
  "Mazda",
  "McLaren",
  "Mercedes-Benz",
  "MG",
  "Mini",
  "Mitsubishi",
  "Morgan",
  "Nissan",
  "Opel",
  "Peugeot",
  "Porsche",
  "Renault",
  "Rolls-Royce",
  "Rover",
  "Saab",
  "Seat",
  "Skoda",
  "Smart",
  "SsangYong",
  "Subaru",
  "Suzuki",
  "Tesla",
  "Toyota",
  "Volkswagen",
  "Volvo"
]
APPROVED_TYPES = [
    "Truck",
    "Sedan",
    "Coupe",
    "SUV",
    "Destroyed"
]
from models.__init__ import CONN, CURSOR
from models.company import Company
class Car:
    all = {}
    destroyed = []
    def __init__(self, year, brand, type, division_id, id=None):
        self.year = year
        self.brand = brand
        self.type = type
        self.division_id = division_id
        self.id = id
    def __repr__(self):
        return f"<Year = {self.year} brand = {self.brand} type = {self.type} id = {self.id}"

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        if isinstance(year, int) and 1908 <= year <= 2025:
            self._year = year
        else:
            raise ValueError("Oops! brand year must be an integer and between 1908 and 2025")
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and brand in APPROVED_BRANDS:
            self._brand = brand
        else:
            raise ValueError("Oops! Vehicle must be in approved lists of automotive brands.")
    @property
    def type(self):
        return self._type 
    @type.setter
    def type(self, type):
        if isinstance(type, str) and type in APPROVED_TYPES:
            self._type = type
        else:
            raise ValueError("Oops! Vehicle must be in approved lists of automotive vehicle types.")
    @property
    def division_id(self):
        return self._division_id
    @division_id.setter
    def division_id(self, division_id):
        if isinstance(division_id, int) and Company.find_by_id_div(division_id):
            self._division_id = division_id
        else:
            raise ValueError("Vehicle must belong to one division of GI Junking Co.")
    @classmethod
    def create_car_table(cls):
        #Create cars table
        sql = """
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                year INTEGER,
                brand TEXT,
                type TEXT,
                division_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        #Drop table as soon as program starts
        sql = """
        DROP TABLE IF EXISTS cars;
        """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        #Saving class instance into database row
        sql = """
            INSERT INTO cars (year, brand, type, division_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.year, self.brand, self.type, self.division_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    @classmethod
    def create(cls, year, brand, type, division_id):
        #Create a new instance, assign instance id matching row id and add to dict for later purposes
        new_car = cls(year, brand, type, division_id)
        new_car.save()
        cls.all[new_car.id] = new_car
        return new_car
    @classmethod
    def find_all_cars(cls):
        #Grabs all of the rows of the created car table, grabs the id, searches dict and that function returns the instances
        sql = """
            SELECT * FROM cars;
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.db_row_to_instance(row) for row in rows]
    @classmethod
    def db_row_to_instance(cls, row):
        car = cls.all.get(row[0])
        if car:
            car.year = row[1]
            car.brand = row[2]
            car.type = row[3]
            car.division_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            car = cls(row[1], row[2], row[3], row[4])
            car.id = row[0]
            cls.all[car.id] = car
        return car
    @classmethod
    def find_by_id(cls, id):
        #Finds an car by id, only manager can do all read functions
        sql = """
            SELECT * FROM cars
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.db_row_to_instance(row)
    @classmethod
    def find_by_year_asc(cls, year, division_id):
        #Finds an car by id, only manager can do all read functions, grab all of the same year cars
        sql = """
            SELECT * FROM cars
            WHERE year = ? and division_id = ?
        """
        row = CURSOR.execute(sql, (year, division_id)).fetchall()
        return [cls.db_row_to_instance(n) for n in row]
    @classmethod
    def find_by_brand(cls, brand, division_id):
        #Finds an car by id, only manager can do all read functions
        sql = """
            SELECT * FROM cars
            WHERE brand = ? and division_id = ?
        """
        row = CURSOR.execute(sql, (brand, division_id)).fetchall()
        return [cls.db_row_to_instance(n) for n in row]
    @classmethod
    def find_by_type(cls, type, division_id):
        #Finds an car by id, only manager can do all read functions
        sql = """
            SELECT * FROM cars
            WHERE type = ? and division_id = ?
        """
        row = CURSOR.execute(sql, (type, division_id)).fetchall()
        return [cls.db_row_to_instance(n) for n in row]
    @classmethod
    def alternate_year_desc(cls, division_id):
        #oldest to youngest
        sql = """
            SELECT * FROM cars
            WHERE division_id = ?
            ORDER BY year DESC
            
        """
        rows = CURSOR.execute(sql, (division_id,)).fetchall()
        return [cls.db_row_to_instance(row) for row in rows]
    @classmethod
    def alternate_year_asc(cls, division_id):
        #Oldest to youngest
        sql = """
            SELECT * FROM cars
            WHERE division_id = ?
            ORDER BY year ASC
            
        """
        rows = CURSOR.execute(sql, (division_id,)).fetchall()
        return [cls.db_row_to_instance(row) for row in rows]
    @classmethod
    def fetch_all_by_name_default(cls, division_id):
        #Switch between inputs using user input
        sql = """
            SELECT * FROM cars
            WHERE division_id = ?
            ORDER BY brand
        """
        rows = CURSOR.execute(sql, (division_id,)).fetchall()
        return [cls.db_row_to_instance(row) for row in rows]
    
    @classmethod
    def delete_by_id(cls, id):
        #
        sql = """
            DELETE FROM cars
            WHERE id = ? 
        """
        CURSOR.execute(sql, (id,))
        CONN.commit()
        instance = cls.all[id]
        instance.id = None
        instance.type = "Destroyed"
        cls.destroyed.append(instance)
        del cls.all[id]