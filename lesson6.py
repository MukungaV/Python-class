# counter = 200
# while counter>=0:
#     print(counter*counter)
#     counter-=1

counter=1
while counter<=5:
    counter+=1
    val1 = input("Enter radius")
    val2 = input("Enter height")
    if val1=="finish" or val2== "finish":
        break #to termnate a loop
    # conversion to float
    radius = float(val1)
    height = float(val2)

    volume = 3.142 * radius * radius * height

    print("The volume is ", volume)

    #loop 1-100
    #if counter is divisible by 2= print your name
    #if counter is divisible by 3= print a city
    #if counter is divisible by both= print a country
    #otherwise= phone model