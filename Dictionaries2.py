#Python Dictionary Data Structure
#In a dictionary we use {}, list []
#A dictionary is made up of a key and a value; data is in pairs





John={
    "Height": 5.7,
    "Country":"Kenya",
    "Language":["Python","Java","Javascript"]
}
print(type(John))
print(John)

#ACCESSING VALUES IN A DICTIONARY
#syntax
#dictionaryvariable [key]
print(John["Height"])

print(John["Language"])


#ACCESSING VALUES IN A DICTIONARY
#syntax; dictionaryname.get(key)
print(John.get("Country"))

#CHANGING DICTIONARY VALUES
#syntax; dictionaryname["key"]= new value
John["Country"]="India"
print(John)


#LOOPING THROUGH A DICTIONARY
for item in John:
    print(item)
for data in John:
    print(John[data])
#for data in John:
    #print(data+":"+ str(John[data]))


key_list=[]
value_list=[]
for data in John:
    key_list.append(data)
    value_list.append(John[data])
print(key_list)
print(value_list)


#LOOPING THROUGH KEYS
for data in John:
    print(data)

#LOOPING THROUGH VALUES
for val in John.values():
    print(val)

#LOOPING THROUGH BOTH KEYS AND VALUES
for my_key,my_value in John.items():
    print("printing keys and values")
    print("KEY " + my_key + " VALUE " + str(my_value))

#ADDING KEYS AND VALUES TO AN EXISTING DICTIONARY
#syntax; dictionaryname[newkey]=new value
John["status"]= "complicated"
John["occupation"]= 'python engineer'
print(John)


#Assignment: removing keys and values in a dictionary
            #deleting a dictionary
            #clearing a dictionary
            #copying a dictionary


#To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(John))

#Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:
John.pop("Language")
print(John)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
John.popitem()
print(John)

#The del keyword removes the item with the specified key name:
del John["status"]
print(John)

#The del keyword can also delete the dictionary completely:
#del John
#print(John)  #this will cause an error because "John" no longer exists.

#The clear() keyword empties the dictionary:
#John.clear()
#print(John)

#Make a copy of a dictionary with the copy() method:
John2=John.copy()
print(John2)

#Another way to make a copy is to use the built-in method dict().
#Make a copy of a dictionary with the dict() method:
John3=dict (John)
print(John3)