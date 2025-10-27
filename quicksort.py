#code for quicksort
def quicksort(arr):
    if len(arr) < 2:
        return arr
    #if the array have 1 item then the array is sorted
    else:
        pivot = arr[0] #here we take a pivot 
        less = [i for i in arr[1:] if i <= pivot] #we create a array with all the items in the array that are minor or equal that the pivot
        greater = [i for i in arr[1:] if i > pivot] #we create an array with all the items in the array that are major than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)
        #then we use recursive to less and greater to sorted all

print(quicksort([10, 5, 3, 2]))