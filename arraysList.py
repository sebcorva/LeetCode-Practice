#List
my_list = [1, 2, 3, 'seba', 'nataly']
#search an element with its index
print(my_list[3])
#insert and element at the end of the list
my_list.append(True)
print(my_list)
#insert an element at the middle of the list
my_list.insert(2, 10) #this operation shifts the rest of elements to the right and is low (O(n))
print(my_list)
print('-------------------------')
#arrays
import array
#declare an array of integers
my_array = array.array('i', [1, 2, 3, 4]) # 'i' indicates the type of elements (integer)
print(my_array)
print(my_array.typecode)