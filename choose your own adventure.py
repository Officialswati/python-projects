name=input("Type your name:")
print("welcome",name,"to this adventure!")


answer=input("You are on dirt road,it has come to an end and you can go left or right.Which way would you like to go?: ").lower()

if(answer=="left"):
   answer = input("you come to a river,you can walk around it or swim across?Type walk to walk around and swim to swim across: ")
   if(answer=="swim"):
       print("you swim across and were eaten by an alligator.")
        
   elif(answer=="walk"):
       print("you walked many miles,ran out of water and you lost the game")
       
   else:
       print("not a valid option,you lose")    
    
elif(answer=="right"):
    answer = input("you come to a bridge,it looks wobbly,do you want to cross it or held back?(cross/back) : ")
    if (answer == "back"):
        print("you go back to main road and lose.")
    elif(answer == "cross"):
        answer=input("you cross the bridge and meet a stranger.Do you talk to them?(yes/no) :")
        if(answer== "yes"):
            print("you talk to the stranger and they give you gold,you win!!:")
        elif(answer == "no"):
            print("you ignore the stranger and they are offended and you lose:")
            
        else:
            print("not a valid option.You lose")
    else:
        print("not a valid option.You lose")
else:
    print("not a valid option.You lose")
print("thank you for trying:",name)