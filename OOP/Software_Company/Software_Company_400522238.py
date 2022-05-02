class Employee:
    base_salary = 0
    tax_rate = 0
    employees = {}

    def __init__(self, first_name, last_name, level, national_id, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.national_id = national_id
        self.profession = profession
        Employee.employees[national_id] = self

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if name.isalpha():
            self._first_name = name
        else:
            raise ValueError("The entered name is invalid!")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        if name.isalpha():
            self._last_name = name
        else:
            raise ValueError("The entered name is invalid!")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level in ["Trainee", "Junior", "Senior", "Manager",
                    "trainee", "junior", "senior", "manager"]:
            self._level = level
        else:
            raise ValueError("The entered level is invalid!")


    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, id):
        if str(id).isdecimal():
            self._national_id = id
        else:
            raise ValueError("The entered ID is invalid!")


    def PrintEmployee(self):
        print("-----------------------------")
        print(f"First name: {self.first_name}\nLast name: {self.last_name}")
        print(f"National ID: {self.national_id}\nLevel: {self.level}=>({self.profession})")


    @classmethod
    def SetBaseSalary(cls, salary):
        if not salary.isalpha():
            cls.base_salary = float(salary)
        else:
            print("Base salary must be an int or float!")

    @classmethod
    def SetTax(cls, tax):
        if not tax.isalpha():
            cls.tax_rate = float(tax)
        else:
            print("Tax rate must be an int or float!")






class Trainee(Employee):

    def __init__(self, first_name, last_name, level, national_id, profession):
        super().__init__(first_name, last_name, level, national_id, profession)
        self.trainee_time = 0

    @property
    def trainee_time(self):
        return self._trainee_time

    @trainee_time.setter
    def trainee_time(self, time):
        self._trainee_time = time

    def SetTraineeTime(self, time):
        self.trainee_time += float(time)

    def ComputeSalary(self):
        salary = -1*(self.base_salary * (self.tax_rate/100)) + self.base_salary
        return salary
        

    def PrintEmployee(self):
        super().PrintEmployee()
        string =  f"Base salary: {self.base_salary}\nTax rate: {self.tax_rate}\n"
        string += f"Trainee time: {self.trainee_time}\nTotal salary: {self.ComputeSalary()}"
        string += "\n-----------------------------"
        print(string)



class Junior(Employee):
    extra_work_fee = 0
    def __init__(self, first_name, last_name, level, national_id, profession):
        super().__init__(first_name, last_name, level, national_id, profession)
        self.extra_work_time = 0


    @property
    def extra_work_time(self):
        return self._extra_work_time

    @extra_work_time.setter
    def extra_work_time(self, time):
        self._extra_work_time = time


    def SetExtraWork(self, time):
        self.extra_work_time += float(time) 

    @classmethod
    def SetExtraWorkFee(cls, fee):
        cls.extra_work_fee = fee

    def ComputeSalary(self):
        salary = self.base_salary + (float(self.extra_work_fee) * self.extra_work_time)
        salary -= self.base_salary * (self.tax_rate/100)
        return salary

    def PrintEmployee(self):
        super().PrintEmployee()
        string =  f"Base salary: {self.base_salary}\nTax rate: {self.tax_rate}\n"
        string += f"Extra_Work time: {self.extra_work_time}\nExtra_work fee: {self.extra_work_fee}\nTotal salary: {self.ComputeSalary()}"
        string += "\n-----------------------------"
        print(string)
        









class Manager(Employee):
    extra_work_fee = 0
    def __init__(self, first_name, last_name, level, national_id, profession):
        super().__init__(first_name, last_name, level, national_id, profession)
        self.extra_work_time = 0


    @property
    def extra_work_time(self):
        return self._extra_work_time

    @extra_work_time.setter
    def extra_work_time(self, time):
        self._extra_work_time = time


    def SetExtraWork(self, time):
        self.extra_work_time += float(time) 

    @classmethod
    def SetExtraWorkFee(cls, fee):
        cls.extra_work_fee = fee

    def ComputeSalary(self):
        salary = self.base_salary + (float(self.extra_work_fee) * self.extra_work_time)
        salary -= self.base_salary * (self.tax_rate/100)
        return salary

    def PrintEmployee(self):
        super().PrintEmployee()
        string =  f"Base salary: {self.base_salary}\nTax rate: {self.tax_rate}\n"
        string += f"Extra_Work time: {self.extra_work_time}\nExtra_work fee: {self.extra_work_fee}\nTotal salary: {self.ComputeSalary()}"
        string += "\n-----------------------------"
        print(string)





class Senior(Employee):
    extra_work_fee = 0

    def __init__(self, first_name, last_name, level, national_id, profession):
        super().__init__(first_name, last_name, level, national_id, profession)
        self.extra_work_time = 0
        self.list_of_trainees = {}

    @property
    def extra_work_time(self):
        return self._extra_work_time

    @extra_work_time.setter
    def extra_work_time(self, time):
        self._extra_work_time = time

    
    def SetExtraWork(self, time):
        self.extra_work_time += float(time)  

    @classmethod
    def SetExtraWorkFee(cls, fee):
        cls.extra_work_fee = fee

    def ComputeSalary(self):
        salary = self.base_salary + (float(self.extra_work_fee) * float(self.extra_work_time))
        salary -= self.base_salary * (self.tax_rate/100)
        return salary

    def AddTraineeToSenior(self, trainee):
        if isinstance(trainee, Trainee):
            self.list_of_trainees[trainee.national_id] = trainee
        else:
            print("We can not add a non-trainee!")

    def PrintEmployee(self):
        super().PrintEmployee()
        string =  f"Base salary: {self.base_salary}\nTax rate: {self.tax_rate}\n"
        string += f"Extra_Work time: {self.extra_work_time}\nExtra_work fee: {self.extra_work_fee}\nTotal salary: {self.ComputeSalary()}\n"
        string += f"Number of trainees: {len(self.list_of_trainees)}"
        string += "\n-----------------------------"
        print(string)



menu = """<<software company command programm>>
Menu =>
        AddEmployee        (1)
        AddTraineeToSenior (2)
        SetTraineeTime     (3)
        PrintEmployee      (4)
        SetBaseSalary      (5)
        SetTax             (6)
        SetExtraWorkFee    (7)
        SetExtraWork       (8)
        ComputeSalary      (9)
        ShowAllEmployees   (11)
        Menu               (12)
        Exit               (0)"""




print(menu)
while True:
    data = input(">>>").split()
    try:
        command = data[0]
    except:
        command = ""

    if command == "AddEmployee" or command == "1":
        if len(data) == 6:
            if data[3] == "Senior":
                Senior(*data[1:])
                print("Senior_Employee successfully added")
            elif data[3] == "Manager":
                Manager(*data[1:])
                print("Manager_Employee successfully added")
            elif data[3] == "Junior":
                Junior(*data[1:])
                print("Junior_Employee successfully added")
            elif data[3] == "Trainee":
                Trainee(*data[1:])
                print("Trainee_Employee successfully added")
            else:
                print("Enter a valid level...")
                
        else:
            print("AddEmployee takes 5 arguments!")



    elif command == "AddTraineeToSenior" or command == "2":
        if len(data) == 3:
            try:
                id_of_senior = data[2]
                id_of_trainee = data[1]
                the_trainee = Employee.employees[id_of_trainee]
                the_senior = Employee.employees[id_of_senior]
                the_senior.AddTraineeToSenior(the_trainee)
                print("Senior added successfully")
            except:
                print("No one was found with this ID")
        else:
            print("AddTraineeToSenior takes 2 arguments!")



    elif command == "SetTraineeTime" or command == "3":
        if len(data) == 3:
            try:
                id_of_trainee = data[1]
                time = data[2]
                the_trainee = Employee.employees[id_of_trainee]
                the_trainee.SetTraineeTime(time)
                print("Time set successfully")
            except:
                print("can't process that...")
        else:
            print("SetTraineeTime takes 2 arguments!")




    elif command == "PrintEmployee" or command == "4":
        if len(data) == 2:
            try:
                id = data[1]
                employee = Employee.employees[id]
                employee.PrintEmployee()
            except:
                print("No one was found with this ID")
        else:
            print("PrintEmployee takes 1 arguments!")




    elif command == "SetBaseSalary" or command == "5":
        if len(data) == 3:
            try:
                salary = data[2]
                level = data[1]
                if level == "Manager":
                    Manager.SetBaseSalary(salary)
                elif level == "Senior":
                    Senior.SetBaseSalary(salary)
                elif level == "Junior":
                    Junior.SetBaseSalary(salary)
                elif level == "Trainee":
                    Trainee.SetBaseSalary(salary)
                else:
                    print("Enter a valid level")
                if not salary.isalpha():
                    print("Base salary set successfully")
            except:
                print("can't process that...")
        else:
            print("SetBaseSalary takes 2 arguments!")




    elif command == "SetTax" or command == "6":
        if len(data) == 3:
            try:
                tax = data[2]
                level = data[1]
                if level == "Manager":
                    Manager.SetTax(tax)
                elif level == "Senior":
                    Senior.SetTax(tax)
                elif level == "Junior":
                    Junior.SetTax(tax)
                elif level == "Trainee":
                    Trainee.SetTax(tax)
                else:
                    print("Enter a valid level")
                if not tax.isalpha():
                    print("Tax rate set successfully")
            except:
                print("can't process that...")
        else:
            print("SetTax takes 2 arguments!")




    elif command == "SetExtraWorkFee" or command == "7":
        if len(data) == 2:
            try:
                fee = data[1]
                Senior.SetExtraWorkFee(fee)
                Junior.SetExtraWorkFee(fee)
                Manager.SetExtraWorkFee(fee)
                print("Extra work fee set successfully")
            except:
                print("can't process that...")
        else:
            print("SetExtraWorkFee takes 1 arguments!")




    elif command == "SetExtraWork" or command == "8":
        if len(data) == 3:
            try:
                id = data[1]
                time = data[2]
                person = Employee.employees[id]
                person.SetExtraWork(time)
                print("Extra work set successfully")
            except:
                print("can't process that...")
        else:
            print("SetExtraWork takes 2 arguments!")




    elif command == "ComputeSalary" or command == "9":
        if len(data) == 2:
            try:
                id = data[1]
                person = Employee.employees[id]
                salary = person.ComputeSalary()
                print(f"The amount of salary is for {person.first_name} {person.last_name} is {salary} dollars")
            except:
                print("can't process that...")

        else:
            print("ComputeSalary takes 2 arguments!")




    elif command == "Exit" or command == "0":
        print("Exite...")
        break




    elif command == "ShowAllEmployees" or command == "11":
        for i in Employee.employees.values():
            i.PrintEmployee()


    elif command == "Menu" or command == "12":
        print(menu)



    else:
        continue