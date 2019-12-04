#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
fruits={"apple", "banana", "pineapple"}
for fruit in fruits:
    print(fruit)

#Once a set is created, you cannot change its items, but you can add new items.
#ADDING AN ITEM; use add() method
fruits.add("mango")
fruits.add("avocado")
for fruit in fruits:
    print(fruit)

#ADDING ITEMS; use update() method
fruits.update(["cherry", "berry"])
for fruit in fruits:
    print(fruit)


#Assignment: removing itemsin a set
            #deleting a set
            #clearing a set
            #copying a set

#To determine how many items a set has, use the len() method.
print(len(fruits))


#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
fruits.remove("mango")
print(fruits)

fruits.discard("avocado")
print(fruits)



#The clear() method empties the set:
fruits.clear()
print(fruits)

#The del keyword will delete the set completely:
#del (fruits)
#print(fruits)  #this will raise an error because the set no longer exists

#Join Two Sets
#There are several ways to join two or more sets in Python.
#Both union() and update() will exclude any duplicate items
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3=set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set4 = {"x", "y" , "z"}
set5 = {7, 8, 9}

set6=set4.update(set5)
print(set4)