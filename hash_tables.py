#hash tables = hash + arrays

#to create a empty hash table we going to use dict on python
book = dict() #or book = {}
#apple is a key, and 3.500 is the value
book["apple"] = 3.500
book["banana"] = 1.000
book["tomato"] = 700

print(book)

print(book["apple"])

exist = book.get("tomato")
exist2 = book.get("watermelon")

print(exist) #if the item exits return the value
print(exist2) #if the item doesn't exist return None
