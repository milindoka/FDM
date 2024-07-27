import tkinter as tk
from tkinter import ttk

class Model:
    def __init__(self):
        self.data = {}
        self.data["Grace"] = "001"
        self.data["Hanna"] = "002"
        self.data["John"] = "003"
        self.data["Mike"] = "004"
        self.data["James"] = "005"

    def add_item(self, key, value):
        self.data[key] = value

    def get_item(self, key):
        return self.data.get(key)

class View:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.label = tk.Label(root, text="Enter Key:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add", command=self.add_item)
        self.add_button.pack()

        self.label_result = tk.Label(root, text="Result:")
        self.label_result.pack()

        self.result = tk.Label(root, text="")
        self.result.pack()

    def add_item(self):
        key = self.entry.get()
        value = self.model.get_item(key)
        if value:
            self.result.config(text=f"Value for {key}: {value}")
        else:
            self.result.config(text=f"Key {key} not found.")

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(tk.Tk(), self.model)

        self.model.add_item("name", "John Doe")
        self.model.add_item("age", 30)

if __name__ == "__main__":
    controller = Controller()
    controller.view.root.mainloop()