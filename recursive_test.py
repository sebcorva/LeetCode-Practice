#recursive without base case
def countdown(i):
    print(i)
    countdown(i-1) #here we call the function itself
    #but is infinite because there isn't a base case to stop it

#countdown(3)

#recursive with base case
def countdown_with_recursive(i):
    print(i)
    #base case
    if i <= 0:
        print("recursive is ended")
        return
    #recursive case
    else:
        countdown_with_recursive(i-1)

countdown_with_recursive(3)