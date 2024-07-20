import tkinter as tk
root = tk.Tk()
def func(event):
    key = event.keysym
    if key == 'a':
        print('a')
    elif key == 'b':
        print('b') 

root.bind('<Key>',func)
root.mainloop()
