"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF");
canvas.grid()

'''
Text Rendering Example:
                    x    y                                                       
canvas.create_text(100, 50, text="text goes here", font=("Arial", 16))
'''
# Put your code below
num = 0
b = True
nums = 0
num1 = 0
boolean = True
str = "ice cream"
for int in range(4):


    canvas.create_text(100,100+num,text=str, font=("Arial", 16))
    b = False
    nums += 1

    if b==False:
        num = 48
        if nums == 2:
            num = 24
        if nums ==3:
            num = 72
            str = "banana"
            boolean=False

root.mainloop()
