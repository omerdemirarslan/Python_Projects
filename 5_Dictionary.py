
                                # The Dictionary is a very flexible and extensive structure to use.
                                # The dictionary is indicated by {} on the other hand dictionary{} have keys and values

ThisDict = {"Brand": "BMW",
            "Model": "X6",
            "Year": 2019,
            "Gear": "Automatic"}

print(ThisDict)                 # Here, "Brand","Model","Year" and "Gear" are the key and
                                # "BMW","X6","2019" and "Automatic" the value.

a = ThisDict["Brand"]
print(a)                        #If we want, we can just print any keys. However the output of the key is the key value.


#b = ThisDict["Automatic"]
#print(b)                       # Well, can we do what we do on the key? No!
                                # While the key can print the value, the value does not print the key.
                                # This code outputs error.

ThisDict["Gear"] = "Manuel"
print(ThisDict)                 # We can change the value of a specific item by referring to its key name

for k in ThisDict:
    print(k)                    # We can return the keys in the dictionary With the For() loop

for v in ThisDict:
    print(ThisDict[v])          # We can return the values in the dictionary With the For() loop

for v in ThisDict.values():
    print(v)                    # We can also return the values with the values() method.

for k,v in ThisDict.items():    # We can return both the key and the value With two different variables
    print(k,v)

print(len(ThisDict))            # We can find out how many items are in the dictionary with the Len method

ThisDict = {"Brand": "BMW",
            "Model": "X6",
            "Year": 2019,
            "Gear": "Automatic"}

ThisDict["Color"] = "Blue"      # We can add a new item to the dictionary with its key and value.
print(ThisDict)

ThisDict.pop("Color")           # We can delete an item in the dictionary with the Pop() method.
print(ThisDict)                 # Note that we have written the key of the item we want to delete in parentheses.


del ThisDict["Gear"]            # Del also deletes key and value items, such as pop.
print(ThisDict)

SpareDict = ThisDict.copy()
print(SpareDict)
                                # In both cases, we have copied our dictionary.
SpareDict = dict(ThisDict)
print(SpareDict)

ThisDict = {"Brand": "BMW",
            "Model": "X6",
            "Year": 2019,
            "Gear": "Automatic"}

ThisDict.clear()                # The clear() method deletes all items in the dictionary.
print(ThisDict)

del ThisDict                    # The del() method deletes the dictionary.
print(ThisDict)

# IMPORTANT RİMENDERS

# The used methods used were also used in list structures.
# When we add new item the key writes in [].
# When we delete any item the key writes in [].
# When we change any value information the key writes in [].
# The clear() method deletes all items in the dictionary but the del() method just deletes the dictionary

















