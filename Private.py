class student:
  def __init__(self,__name,__age):
    self.__name=__name
    self.__age=__age
  def display(self):
    print("Name=",self.__name)
    print("Age=",self.__age)

stu1=student("Bhuvanesh",24)
stu1.display()

#Output:
Name= Bhuvanesh
Age= 24
