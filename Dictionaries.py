#Dictionaries self

thisdict={
   "Brand":"Ford",
   "Model":"Mustang",
   "Year":"1964"
  }
print(thisdict)

x=thisdict["Model"]
print(x)

y=thisdict["Model"]
print(y)

thisdict["Year"]=2020
print(thisdict)

for x in thisdict:
    print(x)

#for x in thisdict:
    #print(thisdict[x])

z=thisdict ["Model"]
print(z)

thisdict1={
    "Name":"Jane", "Age":"33", "Occupation":"Nurse"

  }
print(thisdict1)

students=[{"name":"Tom","English":76,"Math":58,"Biology":88,"Total":76+58+88}, {"name":"Sarah","English":90,"Math":43,"Biology":33,"Total":90+43+33},{"name":"Jack","English":87,"Math":34,"Biology":89,"Total":87+34+89}]
for person in students:
   print(person["name"],person ["English"],person["Math"],person["Biology"],person["Total"])

#print(thisdict1[Name])

thisdict2=[{"Name":"Jane", "Age":"33", "Occupation":"Nurse"}, 
           
           {"Name":"John", "Age":"37", "Occupation":"Driver"},
           
           {"Name":"Mary", "Age": "53", "Occupation": "Teacher"},
           
           {"Name": "Jude", "Age": "23", "Occupation": "Student"}]

print(thisdict2)

print(thisdict2)