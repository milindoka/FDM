import tkinter as tk

class EditableTable:
    def __init__(self, root):
        self.root = root
        self.rows = 3
        self.columns = 3
        self.create_table()

    def create_table(self):
        self.table = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                cell_var = tk.StringVar()
                cell_entry = tk.Entry(self.root, textvariable=cell_var)
                cell_entry.grid(row=i, column=j)
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

if __name__ == "__main__":
    root = tk.Tk()
    table = EditableTable(root)

    def print_table_values():
        print(table.get_table_values())

    btn = tk.Button(root, text="Print Table Values", command=print_table_values)
    btn.grid(row=table.rows, columnspan=table.columns)

    root.mainloop()

#This code creates a simple editable table with 3 rows and 3 columns using Tkinter. The EditableTable class creates the table and allows you to get the values entered in the table. The print_table_values function prints the entered values when the button is clicked.
