'''
@author: Bradley 
'''
import random


import tkinter as tk

# Window?
game=tk.Tk()
game.title("Dice Game")
game.geometry("600x400")

label = tk.Label(text = "GAME")
label.grid(column=0,row=0)

roll = tk.Button(game,text="Roll")
roll.grid(column=5,row=5)






game.mainloop()

# Use to add more dice
'''
[-----]\n[0   0]\n[0   0]\n[0   0]\n[-----]
'''


#die = ["[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]","[-----]\n[0    ]\n[     ]\n[    0]\n[-----]","[-----]\n[0    ]\n[  0  ]\n[    0]\n[-----]","[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]","[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]","[-----]\n[0   0]\n[0   0]\n[0   0]\n[-----]"]

#run = True

#while run:
#    num = random.randint(0,5)
#    print(die[num])
#    go = str(input("Type \"stop\" to stop rolling, otherwise hit enter \n"))
#    if go == "stop":
#        run = False



