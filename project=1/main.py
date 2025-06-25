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