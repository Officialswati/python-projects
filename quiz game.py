print("welcome to my computer quiz!")
playing=input("do you want to play? ")
if (playing.lower()!="yes"):
    quit()
    
print("okay! Let's play! ")  
score = 0
answer=input("what does CPU stands for? ")
if(answer.lower()=="central processing unit"):
    print("right answer!")
    score += 1
else:
    print("wrong answer!")
    
answer=input("what does GPU stands for? ")
if(answer.lower()=="graphics processing unit"):
    print("right answer!")
    score += 1
else:
    print("wrong answer!")
answer=input("what does RAM stands for? ")
if(answer.lower()=="random access memory "):
    print("right answer!")
    score += 1
else:
    print("wrong answer!")
answer=input("what does PSU stands for? ")
if(answer.lower()=="power supply unit"):
    print("right answer!")
    score += 1
else:
    print("wrong answer!")
print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4)*100) + "%." )





    