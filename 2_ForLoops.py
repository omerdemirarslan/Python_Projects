
List = ["Python","JavaScript","Java"]       #We can print the items in a list With the for loop
for i in List:
    print(i)

"Python"                                    #We can walk through the string and print every element.
for i in "Python":
    print(i)

List = ["Python","JavaScript","Java"]       #We can break loops after the item we want.
for i in List:
    print(i)
    if (i == "JavaScript"):
        break

List = ["Python","JavaScript","Java"]       #If we specify the condition in advance, the condition is not printed.
for i in List:
    if (i == "JavaScript"):
        break
    print(i)

for i in range(11):                         #We can print the number in the desired range With the Range() function
    print(i)

for i in range(3,9):                        #We can determine the beginning.
    print(i)

List  = ["Python","JavaScript","Java"]
List2 = ["Django","C#","C++"]

for x in List:                              #We can create nested loops.
    for y in List2:
        print(x,y)















