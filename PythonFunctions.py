#1. Is a block of code with a name
#2. This only works when called/when in use
#3.Helps to write repeated code
#def key word used to vreate function:


def nameoffunction(): #creating a function
    print("hello world")

nameoffunction() #calling a function

#Naming a funcion
  #1. It should start with lower case
  #2. It should start with a letter or an underscore

def greetings_1(name): #on function creation, 'name' is a parameter - this takes one arguement
    print("hello world " + name)

greetings_1("John") #on function calling, is an arguement

#greetings_1() #calling the function without an arguement brings an error

#greetings_1(country)   required to be in a string

def greetings_2(name, country, gender ): #takes more than one arguement
    print("My name is " + name + "I come from " + country + "I am " + gender )

greetings_2("John ", "Kenya ", "Male")
greetings_2("John ", "Kenya ", "Male")
greetings_2("John ", "Kenya ", "Male")
greetings_2("John ", "Kenya ", "Male")


#Default parameters
def greeting_3(name="Developer"):
    print("hello world " + name)

greeting_3()
greeting_3("Mary")

def sum_of_two_num(number_1,number_2):
    print(number_1+number_2)
sum_of_two_num(3,5)


def sumOfTwoNum(number_1,number_2):
   theSum= number_1 + number_2
   return theSum
ans=sumOfTwoNum(5,6)
print(ans)

#Create a function that computes an area of a circle of a niven radius

def area_of_cirle (radius):
    print(3.14*radius*radius)
area_of_cirle(21)

def area_of_circle_2(radius=10):
    print(3.14*radius*radius)
area_of_circle_2(21)

def area_of_circle_3(radius3):
    area=3.14*radius3*radius3
    return area
ans3=area_of_circle_3(21)
print(ans3)





shoppingList=["Soap", "sugar", "bread", "cooking oil", ["spoon", "pot"],{"Name":"John"}]
print(shoppingList[4][0])
print(shoppingList[5]["Name"])
def loopList(theList):
    for item in theList:
        print(item)
    
loopList(shoppingList)


def add (a,b):
    print("Adding {a}+{b}")
    return a + b

def subtract (a,b):
    print("Subtracting {a}-{b}")
    return  a - b

def multiply (a,b):
    print("Multiplying {a}*{b}")
    return a * b

def divide (a,b):
    print("Dividing {a}*{b}")
    return a * b

print("Let's do some math with just functions!")

age=add(30,5)
height=subtract(120,40)
weight=multiply(45,3)
iq=divide(400,2)














