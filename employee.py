"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.bonusCommission = None
        self.contractCommission = None
        self.contractNumber = None

    def get_pay(self):
        pass

    def setBonusCommission(self, bonusCommission):
        self.bonusCommission = bonusCommission
    
    def setContractCommission(self, contractCommision):
        self.contractCommission = contractCommision

    def setContractNumber(self, contractNumber):
        self.contractNumber = contractNumber

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
        self.salary = None
        self.bonusCommission = None
        self.contractCommission = None
        self.contractNumber = None

    def set_Salary(self, salary):
        self.salary = salary

    def setBonusCommission(self, bonusCommission):
        self.bonusCommission = bonusCommission
    
    def setContractCommission(self, contractCommision):
        self.contractCommission = contractCommision

    def setContractNumber(self, contractNumber):
        self.contractNumber = contractNumber

    def get_pay(self):
        if self.type == 1:
            return self.salary
        elif self.type == 2:
            return self.salary + self.bonusCommission
        elif self.type == 3:
            return self.salary + self.contractCommission * self.contractNumber
        
    def __str__(self):
        if self.type == 1:
            return f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'
        elif self.type == 2:
            return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}.'
        elif self.type == 3:
            return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contractNumber} contract(s) at {self.contractCommission}/contract. Their total pay is {self.get_pay()}.'
        
class HourlyEmployee(Employee):  
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
        self.hourlyPay = None
        self.hoursWorked = None

    def setHourlyPay(self, hourlyPay):
        self.hourlyPay = hourlyPay

    def setHoursWorked(self,hoursWorked):
        self.hoursWorked = hoursWorked

    def get_pay(self):
        if self.type == 1:
            return self.hourlyPay * self.hoursWorked
        elif self.type == 2:
            return self.hourlyPay * self.hoursWorked + self.bonusCommission
        elif self.type == 3:
            return self.hourlyPay * self.hoursWorked + self.contractCommission * self.contractNumber
    
    def __str__(self):
        if self.type == 1:
            return f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyPay}/hour. Their total pay is {self.get_pay()}.'
        elif self.type == 2:
            return f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyPay}/hour and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}.'
        elif self.type == 3:
            return f'{self.name} works on a contract of {self.hoursWorked} hours at {self.hourlyPay}/hour and receives a commission for {self.contractNumber} contract(s) at {self.contractCommission}/contract. Their total pay is {self.get_pay()}.'


            

billie = SalaryEmployee('Billie', type=1)
billie.set_Salary(4000)

charlie = HourlyEmployee('Charlie', type=1)
charlie.setHourlyPay(25)
charlie.setHoursWorked(100)

renee = SalaryEmployee('Renee', type=3)
renee.set_Salary(3000)
renee.setContractCommission(200)
renee.setContractNumber(4)

jan = HourlyEmployee('Jan', type=3)
jan.setHourlyPay(25)
jan.setHoursWorked(150)
jan.setContractCommission(220)
jan.setContractNumber(3)

robbie = SalaryEmployee('Robbie', type=2)
robbie.set_Salary(2000)
robbie.setBonusCommission(1500)

ariel = HourlyEmployee('Ariel', type=2)
ariel.setHourlyPay(30)
ariel.setHoursWorked(120)
ariel.setBonusCommission(600)

print(billie)  
print(charlie) 
print(renee)  
print(jan)  
print(robbie)  
print(ariel)