import tkinter as tk

class Model:
    def __init__(self):
        self.value = 0

    def increment_value(self):
        self.value += 1

    def decrement_value(self):
        self.value -= 1

class View:
    def __init__(self, root, controller):
        self.controller = controller

        self.label = tk.Label(root, text="0")
        self.label.pack()

        self.increment_button = tk.Button(root, text="Increment", command=self.controller.increment)
        self.increment_button.pack()

        self.decrement_button = tk.Button(root, text="Decrement", command=self.controller.decrement)
        self.decrement_button.pack()

    def update_value(self, value):
        self.label.config(text=str(value))

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def increment(self):
        self.model.increment_value()
        self.view.update_value(self.model.value)

    def decrement(self):
        self.model.decrement_value()
        self.view.update_value(self.model.value)

if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(root)
    root.mainloop()
