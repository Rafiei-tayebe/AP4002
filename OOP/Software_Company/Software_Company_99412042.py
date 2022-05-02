"""
mro digram
Participant --> (Employee, Trainee)
Employee --> (Junior, Senior, Manager)
"""

"""
AddEmployee         fName                   lName                Level   National_ID    profession
AddTraineeToSenior  National_id_Trainee     National_id_senior
SetTraineeTime      National_id_Trainee     Time_Elapsed
PrintEmployee       National_ID
SetBaseSalary       Level                   Base_Salary
SetTax              Level                   Tax_percentage
SetExtraWorkFee     Fee
SetExtraWork        National_ID             Extra_Work(h)
ComputeSalary       National_ID
"""

from numbers import Real

class Participant:
    base_salary = None
    tax_percentage = 0
    people:list["Participant"] = []
    
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        self.fName = fName
        self.lName = lName
        self.profession = profession
        self.national_id = national_id

    @classmethod
    def get_by_id(cls, national_id:str) -> "cls":
        """Search in participants list and return the participant with the given id if it exists otherwise return None."""
        for participant in cls.people:
            if participant.national_id == national_id:
                return participant
        else:
            return None

    @classmethod
    def add_participant(cls, participant):
        if isinstance(participant, cls):
            cls.people.append(participant)
        else:
            ValueError(f"participant must be an object of {cls.__name__}")

    @classmethod
    def set_base_salary(cls, base_salary:float) -> None:
        f"""Sets the base salary of {cls.__name__}."""
        cls.base_salary = base_salary    

    def compute_salary(self) -> float:
        f"""Returns the finall salary of the {cls.__name__}"""
        raise NotImplementedError

    def __repr__(self):
        raise f"{type(self).__name__}({self.fName}', lName='{self.lName}', profession='{self.profession}', national_id={self.national_id})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.national_id == other.national_id
        else:
            return NotImplemented


class Employee(Participant):
    fee:float = None
    
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        super().__init__(fName, lName, national_id, profession)
        self.extra_work = 0

    @classmethod
    def set_tax(cls, percentage:float) -> None:
        f"""Sets {cls.__name__} tax percentage."""
        cls.tax_percentage = percentage

    @classmethod
    def set_extra_work_fee(cls, fee:float):
        """Sets the fee for each hour of extra work"""
        cls.fee = fee

    def compute_salary(self):
        f"""Computes the final salary of the {type(self).__name__}"""
        if self.base_salary is not None and self.fee is not None:
            return (self.base_salary + self.extra_work * self.fee) * (100 - self.tax_percentage) / 100
        else:
            print("You must specify base_salary and fee.")

    def set_extra_work(self, extra_work:float):
        """sets extra work for the instance"""
        self.extra_work = extra_work


class Trainee(Participant):
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        super().__init__(fName, lName, national_id, profession)
        self.total_time = 0

    def set_trainee_time(self, time_elapsed:float):
        assert isinstance(time_elapsed, Real)
        self.total_time = float(time_elapsed)

    def compute_salary(self):
        return self.base_salary * self.total_time

    def __repr__(self):
        return f"Trainee(fName='{self.fName}', lName='{self.lName}', profession='{self.profession}', national_id='{self.national_id}', "\
        f"extra_hours={self.total_time})"



class Junior(Employee):
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        super().__init__(fName, lName, national_id, profession)


class Senior(Employee):
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        super().__init__(fName, lName, national_id, profession)
        self.trainees:list[Trainee] = []

    def add_trainee_to_senior(self, trainee:Trainee):
        """Adds a trainee to the senior trainees."""
        if isinstance(trainee, Trainee):
            self.trainees.append(trainee)
        else:
            raise TypeError(f"{trainee} must be of type {Trainee.__name__}.")

    def __repr__(self):
        return f"Senior({self.fName}', lName='{self.lName}', profession='{self.profession}', national_id='{self.national_id}', " \
            f"number_of_trainees={len(self.trainees)})"

class Manager:
    def __init__(self, fName:str, lName:str, national_id:str, profession:str):
        super().__init__(fName, lName, national_id, profession)

    
if __name__ == '__main__':
    while True:
        command = input().split()

        if not len(command):
            continue

        if command[0].lower() == 'exit':
            break
        else:

            if command[0].lower() == 'addemployee':
                if len(command) == 6:
                    try:
                        cls:Participant = eval(command[3])
                        obj:Participant = cls(*command[1:3], *command[4:])
                        cls.add_participant(obj)
                    except NameError:
                        print(f"wrong level {command[3]}")
                else:
                    print("The length of arguments of this command is 6.")

            elif command[0].lower() == 'addtraineetosenior':
                if len(command) == 3:
                    trainee:Trainee = Trainee.get_by_id(command[1])
                    sen:Senior = Senior.get_by_id(command[2])
                    if trainee and sen:
                        sen.add_trainee_to_senior(trainee)
                    else:
                        print("national id's are not found.")
                else:
                    print("The length of arguments of this command is 3.")

            elif command[0].lower() == 'settraineetime':
                if len(command) == 3:
                    trainee:Trainee = Trainee.get_by_id(command[1])
                    if trainee:
                        try:
                            trainee.set_trainee_time(float(command[2]))
                        except ValueError:
                            print(f"{command[2]} must be numeric.")
                    else:
                        print("national id not found.")
                else:
                    print("The length of arguments of this command is 3.")

            elif command[0].lower() == 'printemployee':
                if len(command) == 2:
                    par = Participant.get_by_id(command[1])
                    if par:
                        print(par)
                    else:
                        print("national id not found.")
                else:
                    print("The length of arguments of this command is 2.")

            elif command[0].lower() == 'setbasesalary':
                if len(command) == 3:
                    try:
                        par:Participant = eval(command[1])
                        par.set_base_salary(float(command[2]))
                    except NameError:
                        print(f"wrong level {command[1]}.")
                    except ValueError:
                        print(f"{command[2]} must be numeric.")
                else:
                    print("The length of arguments of this command is 3.")

            elif command[0].lower() == 'settax':
                if len(command) == 3:
                    try:
                        emp:Employee = eval(command[1])
                        emp.set_tax(float(command[2]))
                    except NameError:
                        print(f"wrong level {command[1]}")
                    except ValueError:
                        print(f"{command[2]} must be numeric.")
                    except AttributeError:
                        print(f"Trainee is not an employee so he/she doesn't pay any tax.")
                else:
                    print("The length of arguments of this command is 3.")

            elif command[0].lower() == 'setextraworkfee':
                if len(command) == 2:
                    try:
                        Employee.set_extra_work_fee(float(command[1]))
                    except ValueError:
                        print(f"{command[1]} must be numeric.")
                else:
                    print("The length of arguments of this command is 2.")

            elif command[0].lower() == 'setextrawork':
                if len(command) == 3:
                        emp:Employee = Employee.get_by_id(command[1])
                        if emp:
                            try:
                                emp.set_extra_work(float(command[2]))
                            except ValueError:
                                print(f"{command[2]} must be numeric.")
                        else:
                            print("national_id not found.")
                else:
                    print("The length of arguments of this command is 3.")

            elif command[0].lower() == 'computesalary':
                if len(command) == 2:
                    par:Participant = Participant.get_by_id(command[1])
                    if par:
                        print(par.compute_salary())
                    else:
                        print("national_id not found.")
                else:
                    print("The length of arguments of this command is 2.")
                    
            else:
                print(f"{command[0]} isn't a supported command.")
