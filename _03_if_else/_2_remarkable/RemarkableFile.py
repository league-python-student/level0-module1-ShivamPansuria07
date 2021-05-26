import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
print("Noah,Andrew,Shivam")
num = simpledialog.askstring("Enter a student name", None)
if num == ("Shivam"):
    print("He thinks that Java and Python are cool!")
elif num == ("Noah"):
    print("They are amazing at coding")
elif num == ("Andrew"):
    print("They love to code in python")
elif num == ("Daniel"):
    print("They have a good youtube chanel!")

