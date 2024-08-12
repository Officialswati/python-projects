import random
def rolldice(min,max):
    while True:
        print("rolling dice ....")
        number = random.randint(min,max)
        print(f"Your number : {number}")
        choice = input("Do you want to roll the dice again:(y/n):").lower()
        if (choice.lower()=="y"):
            continue
        elif(choice.lower()!= ("n" or "y")):
            print("invalid input:")
            break
        elif(choice.lower()=="n"):
            break
                
        print("thank you for playing:")
                
    
rolldice(1,6)
