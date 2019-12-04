#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

profile = tuple(("John","male",1999)) #OR
profile = ("John","male",1999)
print(profile)
print(profile[0])

#AN EMPTY LIST; shoppinglist=list()

#EMPTY DICTIONARY; john2=dict()

#EMPTY TUPLE; profile2=tuple()


#Assignment: removing keys and values in a tuple
            #deleting a tuple
            #clearing a tuple
            #copying a tuple

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
profile_list=list(profile)
profile_list[0]="Jade"
profile=tuple(profile_list)
print(profile)

#Tuple Length
#To determine how many items a tuple has, use the len() method
print(len(profile))


#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

#To join two or more tuples you can use the + operator:
tuple1=("John","male",1999)
tuple2=("Jane", "female", 1989)
tuple3=tuple1 + tuple2
print(tuple3)


# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
del profile
print(profile)#this will raise an error because the tuple no longer exists