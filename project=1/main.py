'''
 1 = scissor
 0 = Stone
-1 = paper

write  s = scissor , Stone = S , paper = p in play
'''
import random

computer = random.choice([1,0,-1])

youstr = input("enter the choice: ")

youdict = {"scissor":1,"Stone":0,"paper":-1} #this is for user
reversedict = {1:"scissor",0:"Stone",-1:"paper"} #this is reverse of dict for computer
you = youdict[youstr] #user 

print(f"you choose : {reversedict[you]}\ncomputer choose :{reversedict[computer]}")

if(computer == you):
    print("It's Draw")
else:
    if(computer == 1 and you == 0):         
            print("You win!")
    elif(computer == 1 and you == -1):      
               print("computer win")
    elif(computer == 0 and you == 1):       
              print("computer win")
    elif(computer == 0 and you == -1):      
                print("computer win")
    elif(computer == -1 and you == 0):      
        print("you win")
    elif(computer == -1 and you == 1):      
                print("you win")
