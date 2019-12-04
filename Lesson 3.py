#if statements
captured= input("Enter Your Age :")
# print(captured)
# print(type (65.9))
age=int(captured)
if age<13:
    print("This is a kid")
elif age>=13 and age<=20:
    print("This is a teen")
elif age>=21 and age<=35:
    print("This is a youth")
elif age>=36 and age<=55:
    print("This is a middle age")
else:
    print("This is a senior")


