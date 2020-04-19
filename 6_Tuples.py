
                                # Tuple is an ordered and unchangeable structure.
                                # In Python tuples are written with ()

Thistuple = ("Turkey","France","England","İtaly","Hungary")
print(Thistuple)                # When we print tuple, the output is tuple again.
                                # Remember! The list[] output is list[] and the dict{} output is dict{}.

print(list(Thistuple))          # If we want to print the tuple list format we can write list(Thistuple)...
                                # and We can also do this for dict{} and list[] structures.


print(Thistuple[2])             # We can access items in tuple in square brackets from index numbers.

print(Thistuple[-1])            # We can reach the last item with [-1]
print(Thistuple[-2])            # We can reach the penultimate item from las item with [-2]


print(Thistuple[1:4])           # Prints from the first("France") item to fourth("Hungary") item but fourt not included
print(Thistuple[:4])            # Prints from the zeroth("Turkey") item to fourth("Hungary") item but fourt not included
print(Thistuple[1:])            # Prints from the first("France") item to last item("Hungary") item but last item


Thistuple = ("Turkey","France","England","İtaly","Hungary")

x    = list(Thistuple)
x[4] = "Germany"
Thistuple = tuple(x)            # First, We asiggned the tuple different variable. After we changed of the list fourth...
                                # item and  did tuple when we changed the of the list. Therefore, we have performed the
                                # item change in the list, which is unchangeable.

for i in Thistuple:             # We can return in the tuple with for loop.
    print(i)

if ("Turkey" in Thistuple):     # We can check whether any item exists in the tuple.
    print("Yes 'Turkey' is in the Thistuple tuple")

print(len(Thistuple))           # Print the number of items in the tuple.


Tuple = ("Budapest")
print(type(Tuple))

Tuple = ("Budapest",)           # A comma must be used after the item for a single-item parenthesis to specify a tuple.
print(type(Tuple))


Thistuple  = ("Turkey","France","England","İtaly","Hungary")
Thistuple2 = ("Germany", "USA","Holland")
Thistuple3 = Thistuple + Thistuple2
print(Thistuple3)

# Thistuple.pop()               # The method's output is error because the tuple items cannot be deleted.



Thistuple = ("Turkey","France","England","İtaly","Hungary")
del Thistuple
print(Thistuple)                # Only the tuple can be deleted.



















