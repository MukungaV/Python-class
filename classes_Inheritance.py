#INHERITANCE

class Animal:  #PARENT CLASS
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Name is {} and country is {}." .format(self.name, self.country))



class Goat(Animal):  #CHILD CLASS
    #pass  -used when you do not want to add any other properties or methods to the class.
    def __init__(self, name , country, owner): #adding __init__ means the child clas will no longer inherit from the parent class 'Animal'
        self.name = name
        self.country = country
        self.owner = owner
    def printDetails(self):
        print("Name is {} and country is {} while owner is {}." .format(self.name, self.country, self.owner))



g1 = Goat("gush", "kenya", "John")

g1.printDetails()

class Dog (Animal):
    def __init__(self,name, country, color):
        #Animal. __init__(self,name, country) - inherit from parent
        super().__init__(name,country)
        self.color = color



    def printDetails(self):
        print("Name is {} and country is {} and color is {}.".format(self.name, self.country, self.color))


d1 = Dog('Bruno ' ,'UG', 'red')

d1.printDetails()


#Object oriented programming: -goals
#                            -principle
#                            -patterns

#
