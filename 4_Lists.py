                        #In Python lists are written []

List = [1, 2, 3, 4, 5, 6]
print(List)             #We can print the item of the List

List = ["İstanbul","Paris","Londan","Rome"]
print(List)             #We can describe again.

type(List)              #Indicates which type the list is.
len(List)               #Shows the length of the list.Indicates how many items it contains.

List.append("Budapest") #We can add new items to the list with append
print(List)

print(List[0])          #Prints the zeroth item of the List
print(List[3])          #Prints the third item of the List
print(List[-1])         #Prints with [-1] the last item of the List
print(List[:])          #Prints the all items of the List
print(List[2:])         #Prints from the second item to the last item of the list.


List1 = ["Turkey","France","England","Italy","Hungary"]
List2 = ["İstanbul","Paris","Londan","Rome","Budapest"]

print(List1+List2)      #Lists can be collected.
print(List1*3)          #Lists can be multiplied.

x = List1.copy()        #Returns a copy of the list
y = List2.copy()

print(x)
print(y)

List1[3] = "Germany"    #Changes the third item of the list.
List2[3] = "Berlin"     #Changes the third item of the list.
print(List1)
print(List2)

List1.pop()             #Deletes the last item in the list if () empty
print(List1)

List1.pop(0)            #Deletes the zeroth item of the list
print(List1)

List2.remove("İstanbul") #Removes the item with the specified value
print(List2)

List2.clear()           #Removes all the elements from the list
print(List2)

del (List1)             #Delete List1
print(List1)

