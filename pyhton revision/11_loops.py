# while and For loops
 # while

# x = 0
# while (x<=5):
#     print(x)
#     x=x+1

#for loops

# for x in range(5,11):
#     print(x)

# array
days = ["Mon", "Tue", "Wed", "Thu","Fri", "Sat", "Sun"]

for d in days:
    # if(d=="Fri"):break
    if (d=="Fri"):continue # skips fri
    print(d)
