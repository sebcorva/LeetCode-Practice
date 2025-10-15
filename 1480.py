#!/usr/bin/env python3
#Running Sum of 1d Array
def runningSum(nums):
    counter = 0
    list = [] #this is the list of the output

    for i in nums: #we iterate into the list
        counter = counter + i #now we sum the current counter with the i number
        list.append(counter) #we add the counter to the list
    return list

solution = runningSum([1,2,3,4])
print(solution)

#when i use a print, this output will be in the console, but i cant use this in other part of the code
#whith a return, i can use after assigning in into a variable