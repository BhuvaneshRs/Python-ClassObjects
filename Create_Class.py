class Student:
  def details(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("name=",self.name)
    print("age=",self.age)
    
child1=Student()
child1.details("Bhuvanesh",24)
child1.display()

#Output:
name= Bhuvanesh
age= 24
