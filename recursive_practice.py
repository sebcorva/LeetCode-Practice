def factorial(num):
    #base case
    if num ==0:
        return 1
    #this ensure that the function end when get to 0
    #recursive case
    else: 
        return num * factorial(num-1)
    
#print(factorial(4))

#factorial of a number is (n!) is the product of all the positive numbers lees or equal of a number
#4! = 4 * 3 * 2 * 1 = 24

#Fibonacci
def fibonacci(n):
    #base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    #recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#print(fibonacci(4))
# F(4) = F(3) + F(2) = 2 + 1 = 3
# F(3) = F(2) + F(1) = 1 + 1 = 2
# F(2) = F(1) + F(0) = 1 + 0 = 1
# F(1) = 1
# F(0) = 0
#so F(4) = 3

#sum of a list
def sum_list(arr):
    #base case
    if len(arr) == 0:
        return 0
    #recursive case
    else:
        return arr[0] + sum_list(arr[1:])
    
#print(sum_list([1, 2, 3, 4])) # we expect to get 10

#power of a number
def power_of_number(base, exp):
    #base case
    if exp == 0:
        return 1
    #recursive case
    else:
        return base * power_of_number(base, exp -1)

#print(power_of_number(2, 3)) # we expect to get 8 (2 * 2 * 2)

#reverse a string
def reverse_string(s):
    #base case
    if len(s) <=1:
        return s
    #recursive case
    else:
        return s[-1] + reverse_string(s[:-1])

#print(reverse_string("hello")) # we expect to get "olleh"

#ex 1
def sum_num(n):
    n = str(n)
    #base case
    if len(n) <= 1:
        return int(n)
    #recursive case
    else:
        return int(n[0]) + sum_num(n[1:])

#print(sum_num(1234)) 

#ex 2
#add up all the numbers of a list and return the total
def sum_list(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])

#print(sum_list([1,3,5,15]))
    
#sum function of the example 4.1
def sum(arr):
    if len(arr) == 0: #if arr == []
        return 0
    else:
        return arr[0] + sum(arr[1:])

#print(sum([2,3,5]))

#recursive function to count the numbers of items in a list
def count_list(arr):
    if len(arr) == 0: #if arr == []
        return 0
    else:
        return 1 + count_list(arr[1:])

#here first made the base case whith len = 0, and the recursive base is the taken a 1 for a item and sum this to the rest of the items
#print(count_list([1,3,4,5,3,4]))

#find the max number of a list
def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    submax_num = max_num(arr[1:])
    return arr[0] if arr[1] > submax_num else submax_num

print(max_num([2,4,5,1,9]))
