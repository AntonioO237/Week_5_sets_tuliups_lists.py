# Collections = single "variable" used to stoe mulitple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates 
# Tuple = () ordered and unhcangable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "watermelon"]
print(dir(fruits)) # Prints out the methods
print(help(fruits)) # Prints out documentation of amount of values
print(len(fruits)) # Prints out the list 
print("pineapple" in fruits) # Prints if subject is in the list, true or false

fruits[0] = "pineapple" # I can reasign values using this 
fruits.append("pineapple") # To add element to a list 
fruits.remove("apple") # To remove element from list 
fruits.insert(0, "pineapple") # Inserts value at certain index
fruits.sort() # This sorts the list
fruits.reverse() # This reverses the list
fruits.clear() # This clears the list 

print(fruits[0])
for fruit in fruits:
    print(fruit)

