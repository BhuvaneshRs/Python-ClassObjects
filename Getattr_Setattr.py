class employee:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("name=",self.name)
    print("age=",self.age)

emp1=employee("Bhuvanesh",24)
emp2=employee("Vinoth",26)
emp1.display()
emp2.display()

emp1.name="Bhuvaneshwaran"
getattr(emp1,"name")

setattr(emp2,"name","VinothKumar")
getattr(emp2,"name")

#Output:
name= Bhuvanesh
age= 24
name= Vinoth
age= 26
'Bhuvaneshwaran'
'VinothKumar'
