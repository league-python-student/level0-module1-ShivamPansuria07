"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
num = simpledialog.askstring("add, subtract, multiply, or divide", None)
num1 = simpledialog.askinteger("enter first number", None)
num2 = simpledialog.askinteger("enter second number", None)
if num ==("add"):
    print(str(num1+num2))
elif num ==("subtract"):
    print(str(num1-num2))
elif num == ("multiply"):
    print(str(num1 * num2))
elif num== ("divide"):
    print(str(num1/num2))