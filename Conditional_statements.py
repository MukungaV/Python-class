#Conditional statements
#1. if - checks is a single condition is true
#2.if...else -executes the condition that is not true
#3.if...elif...else   -executes the conditions before it, if they are not true

#If statements most of the time make use of the assingment operators i.e <,>,<=,>=,!=

x = 5
y = 3

if x > y:
    print(str(x) + " is greater than " + str(y) )
    print("{} is greater than {}" .format(x,y))

else:
    print("{} is less than {}".format(x, y)) #checks for false conditions

if x < y:
    print(str(x) + " is greater than " + str(y))
    print("{} is greater than {}".format(x, y))

elif x<10:
    print("{} is less than {} " .format(x,10))

else:
    print("{} is not less than {}".format(x, y))  # checks for false conditions

#Nested if
if x > y:
    if y > 4:
        print("y is greater than 2, but less than {}".format(x))
    else:
        print("y is not greater than {} and {}".format(2,x))

else:
    print("{} is not greater than {}".format(x,y))




# While loops
count = 0
while count < 10:
    print("hello world")
    count = count + 1
    # count += 1

num = 0

while num <= 10:
    print(num)
    num = num + 1
    # num += 1


# Break and continue statemnts
num2 = 0

while num2 <= 10:
    if num2 == 5:
        print("at the middle")
        break
    print(num2)
    num2 = num2 + 1
    # num += 1


num3 = 0

while num3 <= 10:
    num3 = num3 + 1
    # num3 += 1
    if num3 == 5:
        #print("at the middle")
        continue #this causes it to skip the inatance that is true and go to the next iteration
    print(num3)


#For loop
for letter in "John":
    print(letter)

#for loop with a range

for i in range (5):  #n-1
    print(i)

for i in range(3,10): #range(starting point, ending point)
    print(i)

for i in range(3,10,2): #range(starting point, ending point, increment value)
    print(i)

#else statement with a for loop
for i in range (10):
    print(i)
else:
    pass


#Assignment: write a program that prints the smallest and largest numbers in this list;

numbers= [210,0,34,65,33,54,54,54,3,65]
#for i in numbers:
print(len(numbers))
print("Maximum integer in list is: " , max(numbers))


numbers.sort()
print(numbers)

#Python program to find largest number in list

# 1
#my_list = []
# 2
#count = int(input("How many numbers you want to add : 10 "))
# 3
#for i in range(1, count + 1):
 #   my_list.append(int(input("Enter number {}: ".format(i))))
# 4
#print("Input Numbers : ")
#print(my_list)
# 5
#min = my_list[0]
#max = my_list[0]
# 6
#for no in my_list:
 #   if no < min:
  #      min = no elif no > max:
   #     max = no
# 7
#print("Minimum number : {}, Maximum number : {}".format(min, max))


NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of the Element : "))
    NumList.append(value)

print("The Largest Element in this List is : ", max(NumList))

