#Method Overriding
class base():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print(f"Name={self.name}")
    print(f"Age={self.age}")

class sub(base):
  def __init__(self,name,age):
    super().__init__(name,age)
    self.name=name
    self.age=age
  def display(self):
    print(f"My Name is {self.name}")
    print(f"My age is {self.age}")
#(It should Take only method on sub class)
obj=sub("Bhuvanesh",24)
obj.display()

#Output:
My Name is Bhuvanesh
My age is 24
