# 2. class Company:
# 3. ....
    
class Employee:
    tax_rate = None
    overtime = None
    overtime_fee = None
    
    list_of_employees = dict()
    
    def __init__(self, fname, lname, specialty, id_number):
        self.fname = fname
        self.lname = lname
        self.specialty = specialty
        self.id_number = id_number
        Employee.list_of_employees[id_number] = self
        
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, value):
        if not value.isalpha():
            raise ValueError('Name can only include letters')
        self._fname = value
    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, value):
        if not value.isalpha():
            raise ValueError('Last name can only include letters')
        self._lname = value    
    @property
    def id_number(self):
        return self._id_number
    @id_number.setter
    def id_number(self, value):
        if not value.isnumeric():
            raise ValueError('ID number can only include numbers')
        if len(value) != 10:
            raise ValueError('ID number must have 10 digits')
        self._id_number = value
    def printEmplyee(self):
        print(self.national_id)
    

        
