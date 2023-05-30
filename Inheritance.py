class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("Name=",self.name)
    print("Age=",self.age)

class teacher(student):
  def getdata(self,city,state):
    self.city=city
    self.state=state
  def displayt(self):
    student.display(self)
    print("City=",self.city)
    print("State=",self.state)
stu1=teacher("Bhuvanesh",24)
stu1.getdata("Salem","Tamilnadu")
stu1.displayt()

#Output:
Name= Bhuvanesh
Age= 24
City= Salem
State= Tamilnadu
