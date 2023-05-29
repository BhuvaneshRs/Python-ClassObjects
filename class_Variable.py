class student:
  state="TamilNadu"
  def getdetails(self,name,age,city):
    self.name=name
    self.age=age
    self.city=city
  def display(self):
    print("name=",self.name)
    print("age=",self.age)
    print("city=",self.city)
    print("state=",student.state)

person1=student()
person1.getdetails("Bhuvanesh",24,"salem")
person2=student()
person2.getdetails("Vinoth",26,"Salem-Omalur")

Output:
person1.display()
name= Bhuvanesh
age= 24
city= salem
state= TamilNadu

person2.display()
name= Vinoth
age= 26
city= Salem-Omalur
state= TamilNadu
