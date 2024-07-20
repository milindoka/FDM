#This code creates a simple editable table with self.rows and self.columns using Tkinter.
# The EditableTable class creates the table and allows you to get the values entered in the table. 
# The print_table_values function prints the entered values when the button is clicked.


import tkinter as tk

class EditableTable:
    def __init__(self, root):
        self.root = root
        self.rows = 3
        self.columns = 8
        self.create_table()

    def create_table(self):
       #====== create table title row======
    
        title_str = tk.Entry(self.root,justify="center",bg="gray",width=5)
        title_str.insert(0, "Sr") 
        title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
        title_str.grid(row=1,column=0)
    
        title_row=['Principal','Maturity','From','To','Interest','ID','Title']
        i=1
        for x in title_row:
            title_str = tk.Entry(self.root,justify="center",bg="gray")
            title_str.insert(i,x) 
            title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
            title_str.grid(row=1,column=i)
            i=i+1

                      
        #==================================
        self.table = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                cell_var = tk.StringVar()
                if j==0:
                 cell_entry = tk.Entry(self.root, textvariable=cell_var,width=5)
                else :
                 cell_entry = tk.Entry(self.root, textvariable=cell_var)
                cell_entry.grid(row=i+2, column=j)
                row.append(cell_var)
            self.table.append(row)

    def get_table_values(self):
        table_values = []
        for i in range(self.rows):
            row_values = []
            for j in range(self.columns):
                row_values.append(self.table[i][j].get())
            table_values.append(row_values)
        return table_values
    
    
    
    def add_row(self):
       for i in range(1):
            row = []
            for j in range(self.columns):
                cell_var = tk.StringVar()
                if j==0:
                 cell_entry = tk.Entry(self.root, textvariable=cell_var,width=5)
                else :
                 cell_entry = tk.Entry(self.root, textvariable=cell_var)               
                cell_entry.grid(row=self.rows+2, column=j)
                row.append(cell_var)
            self.table.append(row)
            self.rows=self.rows+1

if __name__ == "__main__":
    root = tk.Tk()
    
   # screen_width = root.winfo_screenwidth()
   # screen_height = root.winfo_screenheight()
   # root.geometry(f'{screen_width}x{screen_height}')


    table = EditableTable(root)

    def print_table_values():
        print(table.get_table_values())

    btn = tk.Button(root, text="Print Table Values", command=print_table_values)
    btn.grid(row=table.rows+1, columnspan=table.columns)

    btn2 = tk.Button(root, text="ADD ROW", command=table.add_row)
    btn2.grid(row=0,column=1)
    root.mainloop()

