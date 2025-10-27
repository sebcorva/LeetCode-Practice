#function to find the smalest item in a list
def findSmallest(arr):
    smallest = arr[0] #assume the first item is the smallest
    smallest_index = 0 #save the index of the smallest item
    for i in range(1, len(arr)): 
        #print("Comparing:", arr[i], "with smallest:", smallest)
        if arr[i] < smallest:
            smallest = arr[i] #if we find a smaller item, update smallest
            smallest_index = i #update the index of the smallest item
            #print("Smallest updated to:", smallest)
    return smallest_index

#function to make selection sort
def selectionSort(arr):
    newArr = [] #create a empty list to store sorted items
    for i in range(len(arr)): #go through the all the element in the list 
        print("Analizyng index:" , i)
        smallest = findSmallest(arr) #find the smallest item in the unsorted list
        print("Smallest item found:", arr[smallest])
        newArr.append(arr.pop(smallest)) #add the smallest item to the newArray and remove de smallest of the initial list
    return newArr
    
#test the selection sort function
#my_list = [5, 3, 6, 2, 10]
#sorted_list = selectionSort(my_list)
#print("Sorted list:", sorted_list)

unorder_list = [64, 25, 12, 22, 11]

def selection_sort_ex(arr):
    n = len(arr) 
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n): #range(start, end)
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
print(selection_sort_ex(unorder_list))