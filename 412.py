#Fizz Buzz

def fizzBuzz(n):
    result = []
    for i in range(1, n): #we use 1 first to define the start, and then use n+1 to increase the len in 1(because start at 0)
        if i % 5 == 0 and i % 3 ==0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i% 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i)) #this is necessary because the items on the list must be strings
    return result


print(fizzBuzz(15))
