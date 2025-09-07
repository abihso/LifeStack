class Company:
  def __init__(self,name,product):
    self.name = name
    self.product = product
  
  def duty(self):
    print("Start codeing the school managemnet system")
  

class Employee(Company):
  def __init__(self,name,position):
    self.name = name
    self.position = name


emp = Employee("Abihsolo","jnr dev")

emp.duty()