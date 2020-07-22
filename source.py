import pyperclip
from tkinter import *

root = Tk()
root.title("Empty line deleter")
root.attributes('-topmost', 'true')

def click():
    result_str = ""
    in_str = pyperclip.paste()
    print(in_str)
    temp_str = ""
    for ch in in_str:
        if ch != '\n' and ord(ch) != 13:
            temp_str = temp_str + ch
        elif ch == '\n':
            temp_str = temp_str + ' '

    result_str = temp_str
    pyperclip.copy(result_str)
 
frame = Frame(root, width=100, height=30)
btn = Button(text = "Press", command = click)
btn.pack()
root.lift()
frame.pack()
mainloop()
