#This code creates a simple editable table with 3 rows and 3 columns using Tkinter. The EditableTable class creates the table and allows you to get the values entered in the table. The print_table_values function prints the entered values when the button is clicked.


import tkinter as tk

class EditableTable:
    def __init__(self, root):
        self.root = root
        self.rows = 3
        self.columns = 3
        self.create_table()

    def create_table(self):
       #table title row
        for k in range(1):
            for l in range(self.columns):
              title1 = tk.Entry(self.root,justify="center",bg="gray")
              title1.insert(0, "title") 
              title1.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")

              title1.grid(row=k+1,column=l)
        
        self.table = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                cell_var = tk.StringVar()
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
                cell_entry = tk.Entry(self.root, textvariable=cell_var)
                cell_entry.grid(row=self.rows+1, column=j)
                row.append(cell_var)
            self.table.append(row)
            self.rows=self.rows+1

if __name__ == "__main__":
    root = tk.Tk()
    table = EditableTable(root)

    def print_table_values():
        print(table.get_table_values())

    btn = tk.Button(root, text="Print Table Values", command=print_table_values)
    btn.grid(row=table.rows+1, columnspan=table.columns)

    btn2 = tk.Button(root, text="ADD ROW", command=table.add_row)
    btn2.grid(row=0,column=1)
    root.mainloop()

