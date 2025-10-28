#Numbers of steps to reduce a number to zero
def numberOfSteps(num):
    steps = 0
    while num != 0: #or num > 0
        if (num % 2 == 0):
            num /= 2
            steps +=1
        else:
            num -= 1
            steps +=1
    return steps

print(numberOfSteps(123))