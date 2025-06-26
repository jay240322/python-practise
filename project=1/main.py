'''
 1 = scissor
 0 = Stone
-1 = paper

write  s = scissor , Stone = S , paper = p in play
'''
import random

computer = random.choice([1,0,-1])

print("choose any one : paper , scissor , Stone ")

youstr = input("enter the choice: ")

youdict = {"scissor":1,"Stone":0,"paper":-1} #this is for user
reversedict = {1:"scissor",0:"Stone",-1:"paper"} #this is reverse of dict for computer
you = youdict[youstr] #user 
print(f"\nyou choose : {reversedict[you]}\ncomputer choose :{reversedict[computer]}")

if(computer == you):
    print("\tIt's Draw")
else:
    # this is shortcut way
    # this condition is arrived from the last condition which is commented
    # if((computer - you == -1)and(computer - you == 2)):
    #     print("Computer Win !!")
    # else:
    #     print("You Win !!")

    #  this is a main condition 
    #                  
    if(computer == 1 and you == 0):          #(1-0) = 1
        print("you win !!")
    elif(computer == 1 and you == -1):      #(1-(-1)) = 2
                print("computer win")
    elif(computer == 0 and you == 1):       #(0-1) = -1
               print("computer win")
    elif(computer == 0 and you == -1):      #(0-(-1)) = 1
                 print("you win")
    elif(computer == -1 and you == 0):      #((-1)-0) = -1
                print("computer win") 
    elif(computer == -1 and you == 1):      #((-1)-1) = -2
               print("you win")
    # else:
    #     print("something went wrong !!")    #this appears when some one write another word