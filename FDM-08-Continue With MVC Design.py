import tkinter as tk
from tkinter import ttk

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
        # Step 3: Create a Frame for Grid Layout
        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, sticky="nwe")
        
        self.label = ttk.Label(frame, text="0")
        self.label.grid(row=1, column=0, pady=10)

       # self.label = ttk.Label(frame, text="Scrollable Content")
       # self.label.grid(row=0, column=0, padx=20,pady=10)
        # Add Buttons above the scroll area
       # self.new_button = ttk.Button(frame, text="New Button")
        #self.new_button.grid(row=1, column=0, pady=10)
        self.increment_button = ttk.Button(frame, text="Increment", command=self.controller.increment)
        self.increment_button.grid(row=1, column=1, pady=10)
        self.decrement_button = ttk.Button(frame, text="Decrement", command=self.controller.decrement)
        self.decrement_button.grid(row=1, column=2, pady=10) 
        # Step 4: Create a Canvas and Scrollbar
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Step 5: Create a Frame for Scrollable Content
        content_frame = ttk.Frame(canvas)

        # Step 6: Configure the Canvas and Scrollable Content Frame
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # Create Table 
        #  --Table Title Row -----
        title_str = tk.Entry(content_frame,justify="center",bg="gray",width=5)
        title_str.insert(0, "Sr") 
        title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
        title_str.grid(row=1,column=0)
        
        title_row=['Principal','Maturity','From','To','Interest','ID','Title']
        i=1
        for x in title_row:
            title_str = tk.Entry(content_frame,justify="center",bg="gray")
            title_str.insert(i,x) 
            title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
            title_str.grid(row=1,column=i)
            i=i+1
        
        for i in range(2, 21):
            self.button = ttk.Button(content_frame, text=f"Button {i}")
            self.button.grid(row=i, column=0, pady=5)

        # Step 8: Create Window Resizing Configuration
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # Step 9: Pack Widgets onto the Window
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.grid(row=2, column=0, sticky="nsew")
        scrollbar.grid(row=2, column=1, sticky="ns")

        # Step 10: Bind the Canvas to Mousewheel Events

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
    root.title("FDM-Fixed Deposit Manager")
    root.geometry("720x800")
   # root.attributes('-fullscreen', True)

    controller = Controller(root)
    root.mainloop()
