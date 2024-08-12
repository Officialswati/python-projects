import random
top_of_range=int(input("type a number:"))
if (top_of_range<=0):
    print("please type a number larger than 0 next time")
    quit()
else:
    print("please type a  number next time")
    
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses += 1
    user_guess=int(input("make a guess:"))
    if(user_guess==random_number):
        print("You got it correct!:")
        break
    elif(user_guess>random_number):
            print("you were above the number!:")
    else:
            print("you were below the number!:")
            print("you got it wrong!:")
print("you got it in",guesses,"guesses")
print("the number is :",random_number)
