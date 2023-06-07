#Method OverLoading
#example
a=10
a=20
# a address can value 10 and it can be changed to address of 20

class base():
  def Addition(self,a,b):
    self.a=a
    self.b=b
    print(self.a + self.b)
  def Addition(self,c,d):
    self.c=c
    self.d=d
    print(self.c - self.d)
  def Addition(self,e,f):
    self.e=e
    self.f=f
    print(self.e * self.f)

#In this Overloading cannot support in python. because all the methods can be represent as an object.
obj=base()
obj.Addition(2,2)

#Output:
4
