#ex 1
item_list = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_items(arr):
    counted_items = {}
    for item in arr:
        if counted_items.get(item) is not None:
            counted_items[item] += 1
        else:
            counted_items[item] = 1
    return counted_items

#print(count_items(item_list))

#this is a more clean way
def count_items_clean(arr):
    counted_items = {}
    for item in arr:
        counted_items[item] = counted_items.get(item, 0) + 1 #dict.get(item, default)
    return counted_items

#print(count_items_clean(item_list))

def find_two_sum(arr, target):
    numbers_checked = {}
    index = 0
    for num in arr:
        if numbers_checked.get(num) is None:
            numbers_checked[num] = index
            index += 1

        complement = target - num
        if numbers_checked.get(complement) is not None and numbers_checked.get(complement) != numbers_checked.get(num):
            return numbers_checked[complement], numbers_checked[num]
#this a more clean way
def find_two_sum2(arr, target):
    seen = {} #here we save the items i see

    for i, num in enumerate(arr): #we use enumerate instead of use a manual index in a for, and this numbers (0, 1,2, etc) of the enumerate is assigned to i
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
            #i can use dict[item] because i know that the key exists, if i dont know is better use .get, because if isn't exists that return None
        seen[num] = i
    return []

numbers = [3, 2, 4]
numbers2 = [2, 7, 11, 15]

print(find_two_sum(numbers, 6))
print(find_two_sum2(numbers2, 9))