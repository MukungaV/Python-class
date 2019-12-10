class MyClass:           #name of class starts with capital letter s unlike in functions
    x = "John"  #John is an attribute- variable in a class

    y= 12

    theList = [22,34,54,78,90]

#Objest creation

c1 = MyClass()
#c1 = object/instance of the MyClass blueprint/clase
c2 = MyClass() #c2 = second object/instance of MyClass

print(c1.x)
print(c1.y)
print(c1.theList)


print(c2.x)
print(c2.y)
print(c2.theList)

class Person:
    def __init__(self,name, age, country):#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
                 #It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
        self.thename = name #assign the class the "thename" attribute
        self.theage = age   #assign the class the "theage" attribute
        self.thecountry = country

    def getter(self):          #function in a class = method

        print("Hello world")
        print(self.thecountry)
        print(self.thename)

    def myname (self):
        print("Muchiri")

#create objects
p1 = Person("John ", 34 , " Kenya ")
p2 = Person ("Mary ", 14 , " India ")

print(p1.theage)
print(p2.thename)
print(p1.thename + p1.thecountry + str ( p1.theage))


p1.getter()
p2. getter()
p2.myname()


print("###########################################")

class Animal:
    def __init__(self, nature, prey, gender, name, feeding):
        self.thenature = nature
        self.theprey = prey
        self. thegender = gender
        self.thename = name
        self.thefeeding = feeding

    def getDetails (self):
        print(self.thenature)
        print(self.theprey)
        print(self.thegender)
        print(self.thename)
        print(self.thefeeding)

a1 = Animal("Wild ", "chicken ", "male ", "mongoose ", "carnivorous")
a2 = Animal ("Domestic", "grass", "female", "goat", "herbivorous")

a1.getDetails()
print("##")
a2.getDetails()


#Assignment: Create a class that has the following:
    #name = continents
    #attributes = size, number of countries, population

print("AAAAAAAAAAAAAAAA")
print("Assignment:")


class Continents:
    def __init__ (self, name, size,  numberOfCountries, population ):
        self.thename = name
        self.thesize = size
        self.thenumOfCount = numberOfCountries
        self.pop = population

    def Dets (self):
        print(self.thename)
        print(self.thesize)
        print(self.thenumOfCount)
        print(self.pop)

    def ContNames (self):
        print(self.thename)

    def ContSize (self):
        print(self.thesize)

    def get_size_and_pop (self):
        print("The size is {} and the population is {} ." .format(self.thesize, self.pop))



cont1 = Continents("Asia ", " 44,579,000 sq. kms "," 47 ", " 3,879,000,333")

cont2 = Continents("Africa ", " 30,065,000 sq. kms"," 57 ", " 1,032,600,256")

cont3 = Continents("North America ", " 24,256,000 sq. kms "," 23 ", " 528,720,588")

cont4 = Continents("South America ", " 17,819,000 sq. kms"," 12 ", " 387,489,196")

cont5 = Continents("Antarctica ", " 14,000,000 sq. kms"," 0 ", " 0 ")

cont6 = Continents("Europe ", " 9,938,000 sq. kms"," 50 ", " 739,165,030")

cont7 = Continents("Australia ", " 7,687,000 sq. kms"," 3 ", " 31,260,000")




cont1.Dets()
cont7.Dets()

cont4.ContSize()


cont1.ContNames()
cont2.ContNames()

cont4.get_size_and_pop()

#You can delete properties on objects by using the del keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

#print(p1.age)

#You can delete objects by using the del keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

#print(p1)

#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
    pass


#Modifying properties
print("MODIFYING PROPERTIES")

cont1.thenumOfCount = "77"
print(cont1.thenumOfCount)



#Deleting a property
del cont2.pop


#Deleting an object
del cont1



