class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("Name=",self.name)
    print("Age=",self.age)
    
#Output:
person1=student("Bhuvanesh",24)
person1.display()
Name= Bhuvanesh
Age= 24

person2=student("Vinoth",27)
person2.display()
Name= Vinoth
Age= 27
