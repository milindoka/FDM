import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

class Model:
    
    def __init__(self):
        self.value = 0
        self.table = []
        self.rows = 10
        self.columns = 9
        self.save_str="ttt"
        
    def savefile(self):
        # Function to save the content of the Text widget to a text file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.save_str)  # Write sample content to file
    
    def open_popup(self):
            self.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message") 
        
    
    def loadfile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                temp_str=file.read()  # Insert file content in temp_str
                return temp_str
              # x=temp_str.split('~')
              # print(x) 
        else :
            return ""
                
    def increment_value(self):
        self.value += 1

    def load_value(self):
        self.value -= 1

class View:
    
    def __init__(self, root, controller):
        self.controller = controller
        # Step 3: Create a Frame for Grid Layout
        frame = tk.Frame(root) 
        frame.grid(row=0, column=0,sticky="nwe") 
        
        self.save_btn = tk.Button(frame, text="  Save ", command=self.controller.save)
        self.save_btn.grid(row=0,column=0,padx=5, pady=5, sticky="w")
        
        self.load_btn = tk.Button(frame, text="  Load  ", command=self.controller.load)
        self.load_btn.grid(row=0,column=1,padx=5, pady=5) 
        
        self.printbtn = tk.Button(frame, text="  Print  ", command=self.controller.print_table_values)
        self.printbtn.grid(row=0,column=2,padx=5, pady=5)
        
        self.addr_btn = tk.Button(frame, text=" Add Row ", command=self.controller.add_row)
        self.addr_btn.grid(row=0,column=3,padx=5, pady=5)
        
        self.sort_btn = tk.Button(frame, text=" Date Sort ", command=self.controller.save)
        self.sort_btn.grid(row=0,column=4,padx=5, pady=5)
        
        # Step 4: Create a Canvas and Scrollbar
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set, height=550)    
    
        # Step 5: Create a Frame for Scrollable Content
        self.content_frame = tk.Frame(canvas)

        # Step 6: Configure the Canvas and Scrollable Content Frame
        self.content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # Create Table 
        #  --Table Title Row -----
        title_str = tk.Entry(self.content_frame,justify="center",bg="gray",width=5)
        title_str.insert(0, "Sr") 
        title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
        title_str.grid(row=1,column=0)
        col_len=[5,12,12,10,10,7,20,10,10]
        title_row=['Principal','Maturity','From','To','Interest','ID','Bank','Title']
        i=1
        for x in title_row:
            title_str = tk.Entry(self.content_frame,justify="center",bg="gray",width=col_len[i])
            title_str.insert(0,x) 
            title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
            title_str.grid(row=1,column=i)
            i=i+1
        # -----Add rows and columns to table-----
        self.table = []
        for i in range(controller.model.rows):
            row = []
            for j in range(controller.model.columns):
                cell_var = tk.StringVar()
                if j==0:
                 cell_entry = tk.Entry(self.content_frame, textvariable=cell_var,width=5)
                 cell_entry.insert(0,str(i))
                 cell_entry.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
                else :
                 cell_entry = tk.Entry(self.content_frame, textvariable=cell_var,width=col_len[j])
                cell_entry.grid(row=i+2, column=j)
                row.append(cell_var)
            self.table.append(row)        
        
        # -----Table Complete --------
        
        
        # Step 8: Create Window Resizing Configuration
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # Step 9: Pack Widgets onto the Window
        canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        canvas.grid(row=2, column=0, sticky="nsew")
        scrollbar.grid(row=2, column=1, sticky="ns")

        # Step 10: Bind the Canvas to Mousewheel Events

    #def update_value(self, value):
    #    self.label.config(text=str(value))

    def get_table_values(self):
        table_values =""
        for i in range(controller.model.rows):
            row_values =""
            for j in range(1,controller.model.columns):
                row_values=row_values+self.table[i][j].get()+'|'
            table_values=table_values+row_values+'~'
        return table_values

    def add_one_row(self):
        print("cc")
        col_len=[5,12,12,10,10,7,20,10,10]
        for i in range(1):
            row = []
            for j in range(controller.model.columns):
                cell_var = tk.StringVar()
                if j==0:
                 cell_entry = tk.Entry(self.content_frame, textvariable=cell_var,width=5)
                 cell_entry.insert(0,str(controller.model.rows))
                 cell_entry.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
                else :
                 cell_entry = tk.Entry(self.content_frame, textvariable=cell_var,width=col_len[j])
                cell_entry.grid(row=controller.model.rows+2, column=j)
                row.append(cell_var)
            self.table.append(row)        
            controller.model.rows=controller.model.rows+1

    
    def copy_ur(self,ro,co):
        #temp=self.table[ro][co].get()
        if ro>2 :
            for c in range(1,controller.model.columns):
              temp=self.table[ro-3][c].get()
              self.table[ro-2][c].set(temp)
              print(temp)  
    


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def save(self):
        self.model.save_str=self.view.get_table_values()
        self.model.savefile()
        
    def load(self):
        data = self.model.loadfile()
        x=data.split('~')
        print(x)
        r=0
        for y in x:
          if not '|' in y : continue
          z=y.split('|')
          for c in range(0,8):  
             self.view.table[r][c+1].set(z[c])
            #print(r,c)
          r=(r+1) 
          if r>(self.model.rows-1) : 
              self.view.add_one_row()
        return  
          
    def print_table_values(self):
        print(self.view.get_table_values())

    def add_row(self):
        self.view.add_one_row() 

        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("FDM-Fixed Deposit Manager")
    screen_width = root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()

   #
   # root.geometry('%dx%d' % (screen_width, screen_height))
   # root.geometry("720x800")
    root.geometry('%dx%d' % (screen_width, 600))

   # root.attributes('-fullscreen', True)
    
    controller = Controller(root)
    
    
    def quit(event):
        print("you pressed control-forwardslash")
        widget = root.focus_get()
        row=widget.grid_info()['row']
        col=widget.grid_info()['column']
        print(row,col)
        
    def copy_upper_row(event): 
        widget = root.focus_get()
        if isinstance(widget,tk.Entry) :
            row=widget.grid_info()['row']
            col=widget.grid_info()['column']
            controller.view.copy_ur(row,col)
            
        else :
            print("noentry")    
            
         
    root.bind('<Control-slash>', quit)
    root.bind('<Control-r>',copy_upper_row)
    root.mainloop()
