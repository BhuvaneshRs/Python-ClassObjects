#user input in Instance Variable
class Teacher():
  def __init__(self):
    self.name=input("Enter name ")
    self.age=int(input("Enter Age "))
  def display(self):
    print(self.name)
    print(self.age)
    
#Teacher1 is an Object that can be get value from user
teacher1=Teacher()
#used to call method to display object 
teacher1.display()

teacher2=Teacher()
teacher2.display()

#Output:
Enter name Bhuvanesh
Enter Age 24
Bhuvanesh
24
Enter name Vinoth
Enter Age 55
Vinoth
55
