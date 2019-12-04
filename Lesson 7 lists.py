#scores list
scores=[45,67,87,98,53,42,23,43,2,54,65]
scores.sort()
for mark in scores:
     if mark%2!=0:
      print(mark,"Yes!")
     else:
      print(mark, "No!")
     if mark>=80:
      print(mark,"A")
     if mark>=80:
      print(mark,"A")
     elif mark>=65:
      print(mark,"B")
     elif mark>=50:
      print(mark,"C")
     elif mark>=35:
      print(mark,"D")
     else:
      print(mark,"E")

 #print(len(scores))
# scores.append(22)
# print(scores)
# scores.pop(11)
# print(scores)




# print(scores[0])
#
# scores.append(54)
# print(scores)
# scores[0]=32
# print(scores)
# scores.pop(2)
# print(scores)
# print(len(scores))


# val1=input("What is the radius")
# val2=input("What is the height")
# radius=float (val1)
# height=float(val2)
#
# pi=3.142
#
#
#
# volume=pi*radius*radius*height
# print("The volume is", volume)
#
#
# Q1=input("Name")
# Q2=input("Age")
# Q2=int(Q2)
# if Q2<=18:
#    exit(0)
# Q3=input("Residence")
# Q4=input("Course")

# person={"name":"John", "age":13, "height":1.9, "weight":32}
# print(person["name"])
#
#many=[{"name":"John","score":50}, {"name":"Mary","score":70},{"name":"Mike","score":20}]

#first=many[0]
#print(first["name"])
#
# for person in many:
#    s=person["score"]
#
#    print(person["name"],s)


#students=[{"name":"Tom","English":76,"Math":58,"Biology":88,"Total":76+58+88}, {"name":"Sarah","English":90,"Math":43,"Biology":33,"Total":90+43+33},{"name":"Jack","English":87,"Math":34,"Biology":89,"Total":87+34+89}]
#for person in students:
   #print(person["name"],person ["English"],person["Math"],person["Biology"],person["Total"])


#newlist
newlist=[34,45,56,78,23,45,98,13,28]
newlist.sort()
for mark in newlist:
   if mark >90:
      print(mark,"A")
   elif mark >=90:
      print(mark,"B")
   elif mark >=80:
      print(mark,"C")
   elif mark >=70:
      print(mark,"D")
   else:print(mark,"E")



#newlist3
newlist3=["James","Ken","Jane","Mary","Peach","Wan"]
print(newlist3 [0])

print(newlist3 [-4])

print(newlist3 [:3])

print(newlist3[3:])

print(newlist3[-4:-1])

print(newlist3[-1])

newlist3 [1]= "Rob"

print(newlist3)

for y in newlist3:
   print(y)

if "Jane" in newlist3:
   print("Yes, 'Jane' is in newlist3")

print(len(newlist3))

newlist3.append("Sam")

print(newlist3)

newlist3.insert(2,"Dan")
print(newlist3)

#newlist3.pop()
#print(newlist3)

#newlist3.pop(1)
#print(newlist3)

#del newlist3[3]

mylist=newlist3
print(mylist)

list1= "1","2","3"
list2= "x","y","z"
list3=list1+list2
print(list3)

#for x in list2:
  #list1.append(x)

#print(list1)

newlist4=list(("1","2","3"))
print(newlist4)

#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x=50
if x > 10:
    print("greater than 10")
    if x > 20:
        print("and also greater than 20")
    if x > 40:
        print("and also greater than 40")

