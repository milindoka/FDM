import tkinter as tk
root = tk.Tk()
root.title("Say Hello")
label = tk.Label(root, text="Hello World")
label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
button = tk.Button(root, text="OK", command=lambda: root.destroy())
button.pack(side="bottom", fill="none", expand=True)
root.mainloop()
