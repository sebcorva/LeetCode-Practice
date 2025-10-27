#implement the classic binary search to find the index of a specific target value
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid] #i have to assig guess with the content to compare with the target
        if guess == target:
            return mid , low#here i return the result
        elif guess > target: #is the menor not equal and if guess is more than target always i have to change de high
            high = mid - 1
        else:
            low = mid + 1
    return -1

list1 = [1, 3, 5, 6]

#print(binary_search(list1, 8))

#white ap function that takes a sorted list of distincs int and an int target
#the return is the index where the target would be insert to be in order

def find_insertion_point(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
# when the target isn't in the arr the function can't find its, so the low always will be more than high, and in this situation the while ends and the low always will be the position of where the target must go
print(find_insertion_point(list1, 2))

#binary search again if i remember

def binary_search_from_memory(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) //2
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

