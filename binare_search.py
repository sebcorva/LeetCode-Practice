#function binary search
def binary_search(arr, item):
    low = 0 #here we have the first index
    high = len(arr)-1 #here we have the last index, as the list starts at 0 we need to subtract 1 of the length because the lengthy start at 1

    while low <= high: #while low index is less or equal than high index the function will keep looking for the item
        mid = (low + high) // 2 #we start looking at the middle of the list
        print("low is: ", low, " high is: ", high)
        print("mid is: ", mid)
        guess = arr[mid] #we save the middle as the idem to compare
        
        if guess == item:
            return mid # if we found the item we get out of the while
        if guess > item:
            high = mid -1 #if the guess is greater than the item we are looking for, we need to look at the left side of the list, so we move the high index to mid -1
            print("guess was too high, so new high is: ", high)        
        else:
            low = mid + 1 #if the guess is less than the item we are looking for, we need to look at the right side of the list, so we move the low index to mid +1
            print("guess was too low, so new low is: ", low)
    return None #if we exit the while without finding the item we return None

array1 = [1, 3, 5, 7, 9]
print(binary_search(array1, 3)) # we expect to get index 1

print('------------------------')
#binary search function using recursive
def binary_recursive(arr, item, low, high):
    #base case
    if len(arr) == 1:
        return item
    
    mid = (low + high) // 2
    #base case
    if arr[mid] == item:
        return mid
    #recursive case
    elif arr[mid] < item: # if mid is minor than item means that item is in the side up so we have to up the low
        return binary_recursive(arr, item, mid + 1, high)
    else: #if mid is major than item means that item is in the low side, so we have to down the high
        return binary_recursive(arr, item, low, mid - 1)

print((binary_recursive(array1, 3, 0, len(array1))))