import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num = simpledialog.askstring("Enter a birthday", None)
    if num ==("05/19"):
       print("Happy birthday!")
    else:
        print("Happy unbirthday!")
