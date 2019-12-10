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
    def __init__(self,name, age, country):
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
        self.thenumberOfCountries = numberOfCountries
        self.pop = population

    def Dets (self):
        print(self.thename)
        print(self.thesize)
        print(self.thenumberOfCountries)
        print(self.pop)

    def ContNames (self):
        print(self.thename)


cont1 = Continents("Asia ", " 44,579,000 sq. kms "," 47 ", " 3,879,000,333")
cont2 = Continents("Africa ", " 30,065,000 sq. kms"," 57 ", " 1,032,600,256")


cont1.Dets()
cont2.Dets()


cont1.ContNames()
cont2.ContNames()




