#while and For loops 
 
 #while loops
# x=1
# while (x<=5):
#     print(x)
#     x=x+1

#For loop 
# for x in range(4,11):
#     print(x)

#array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    # if (d=="Fri"):break #loop stops
    if (d=="Fri"):continue #Skips d
    print(d)