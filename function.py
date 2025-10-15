print("hello world")
print('hello world 2')

x = 5 
y = 10
z = x + y
print(z)

name = "sebastian"
print(name)

#this is a comment

#types of variables

num = int(5)
string = str("cinco")
floatNumber = float(5)

print(num, 'is an integer,', string, 'is a string,', floatNumber, 'is a float')
#in a print i can't user + to concatenate different types of variables
#in this case i can user , to separate them

#assign multiple variables
a, b, c = 'Sebastian', 'is', 31

print(a, b, c)

#i can unpack a list into variables
list = ['apple', 'banana', 'cherry']
a, b, c = list 
print(a, b, c)

#global variables 
globalVariable = "im created outside a function"

def myfunction():
    insideVariable = "im created inside a function"
    print(insideVariable)
    print(globalVariable)

myfunction()

#list and tuples
mylist = ['apple', 'banana', 'cherry'] #we can change the values or the order in the list
mytuple = ('apple', 'banana', 'cherry') # we can't change the values nor the order in the tuple (nor= ni)

#a none variable
nomeVariable = None

#how to get the type of a variable
print(type(globalVariable))
print(type(mylist))
print(type(mytuple))
print(type(nomeVariable))

num = 5
floatNumber2 = 5.5

floatToInt = int(floatNumber2)
print(floatToInt)
IntToFloat = float(num)
print(IntToFloat)

#py haven't a ramdom function, so we can import random module
import random
print(random.randint(1, 10)) #get a random number between 1 and 10 (10 not included)
print(random.random()) #get a random number between 0 and 1 (1 not included)
print(random.uniform(1, 10)) #get a random float number between 1 and 10 (10 not included)
print(random.randrange(2, 10, 2)) #get a random number between 1 and 10 (10 not included) with a step of 2 
#for randrange take steps of 2, so if we start in 2, the random numbers will be pairs
#if we start in 1, the random numbers will be odd (odd = impar)

#casting is when we specify a type for a variable
text = str('this is a text')
number = int(5)

print(text)
print(number)
print(text[1]) #get the second character of the text

#looping into a string
for a in text:
    print(a)

#get the lenght of a string
print(len(text))

#check a string
print("text" in text) #if the word searched is in the variable text,it will return true
print("text" not in text)
#check using a if statement
if "texts" in text:
    print("text is in the variable text")
else:
    print("text is not in the variable text")

#slicing a string
print(text[3:7]) #get characters from position 3 to 6
print(text[:7]) #get characters from the beginning to position 6
print(text[3:]) #get characters from position 3 to the end

print(text.upper()) #convert the string to uppercase
print(text.lower()) #convert the string to lowercase
print(text.strip()) #remove any whitespace from the beginning or the end

list1 = [1,2,3,4,5]
list2 = [True, False, True]
print(list1)
print(list2)
print(type(list2))