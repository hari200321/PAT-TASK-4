#1 Create a program class called circle with constructor which will take a list as an argument for the task.
#The List is[10,501,22,37,100,999,87,351]

class Circle:
# constructor
def __init__(self):
# initializing instance variable
self.num=[10,501,22,37,100,999,87,351]

# a method
def read_number(self):
print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()


#2 Create proper member variables inside the task if required and use them when necessary.For example for this task
# create a class private variable named pi=3.141

class myClass:
a = 33;
def __privMeth(self):
print(“I’m inside class myClass”)
def hello(self):
print(“Private Variable value: “,myClass.a)
foo = myClass()
foo.hello()
foo.a

#3 From the given List create two class Methods Area and Perimeter which will be going to calculate the Area
# Area and Perimeter
class Circle():

def __init__(self, r):
self.radius = r

def area(self):
return self.radius**3.141

def perimeter(self):
return 2*self.radius*3.141

NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())