from datetime import datetime
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
                file.write(self.save_str)  # Write sample content to fil    
    
    
    # Function to convert the 2D list to an HTML table
    def list_to_html_table(self,data):
        html="<!DOCTYPE html>\n"
        html+="<html>\n"
        html+="<style>\n"
        html+="table, th, td \n"
        html+="{\n"
        html+="border:1px solid black;\n"
        html+="}\n"
        html+="</style>\n"
        html+="<body>\n"
        html+="<table style=\"width:100%\">\n"
        for row in data:
            html += "  <tr>\n"
            for cell in row:
                html += f"    <td>{cell}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        html +="</body>\n"
        return html

    # Convert the list to an HTML table
    def save_html_table(self,tablearr):
        html_string = self.list_to_html_table(tablearr)
        # Save the HTML table to a file
        #print(html_string)
        with open("fd_table.html", "w") as file:
            file.write(html_string)
        print("table saved as fd_table.html")    

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
                
    def sort_data(self):
        print("sort")

    def load_value(self):
        self.value -= 1

class View:
    
    def __init__(self, root, controller):
        self.controller = controller
        # Step 3: Create a Frame for Grid Layout
        frame = tk.Frame(root) 
        frame.grid(row=0, column=0) 
        
        self.save_btn = tk.Button(frame, text=" Save ", command=self.controller.save)
        self.save_btn.grid(row=0,column=0,padx=5, pady=5)
        
        self.load_btn = tk.Button(frame, text="Load", command=self.controller.load)
        self.load_btn.grid(row=0,column=1,padx=5, pady=5) 
        
        #self.printbtn = tk.Button(frame, text="  Print  ", command=self.controller.print_table_values)
        #self.printbtn.grid(row=0,column=2,padx=5, pady=5)
        
        self.addr_btn = tk.Button(frame, text="Add Row", command=self.controller.add_row)
        self.addr_btn.grid(row=0,column=2,padx=5, pady=5)
        
        self.sort_btn = tk.Button(frame, text="Date Sort", command=self.controller.sort_table)
        self.sort_btn.grid(row=0,column=3,padx=5, pady=5)
        
        self.repo_btn = tk.Button(frame, text="FY Report", command=self.controller.fy_report)
        self.repo_btn.grid(row=0,column=4,padx=5, pady=5)

        self.html_btn = tk.Button(frame, text="Save Table ", command=self.controller.save_table)
        self.html_btn.grid(row=0,column=5,padx=5, pady=5)
        
        self.crpo_btn = tk.Button(frame, text="Create Report", command=self.controller.cr_report)
        self.crpo_btn.grid(row=0,column=6,padx=5, pady=5)

        
        # Step 4: Create a Canvas and Scrollbar
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set, height=550,width=1200)    
    
        # Step 5: Create a Frame for Scrollable Content
        self.content_frame = tk.Frame(canvas)

        # Step 6: Configure the Canvas and Scrollable Content Frame
        self.content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # Create Table 
        #  --Table Title Row -----
        title_str = tk.Entry(self.content_frame,justify="center",bg="gray",width=5)
        title_str.insert(0, "Sr") 
        title_str.config(state=tk.DISABLED,disabledbackground="#D3D3D3", disabledforeground="black")
        title_str.grid(row=2,column=0)
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
                 cell_entry.insert(0,str(i+1))
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
        canvas.grid(row=2, column=0, columnspan=8,sticky="nsew")
        scrollbar.grid(row=2, column=10,sticky="ns")

        # Step 10: Bind the Canvas to Mousewheel Events

    #def update_value(self, value):
    #    self.label.config(text=str(value))

    def get_table_array(self):
        table_array=[]
        for i in range(controller.model.rows):
            row_array=[]
            for j in range(1,controller.model.columns):
                #row_values=row_values+self.table[i][j].get()+'|'
                row_array.append(self.table[i][j].get())
            table_array.append(row_array)
        return(table_array)  


    def get_table_values(self):
        table_values =""
        for i in range(controller.model.rows):
            row_values =""
            for j in range(1,controller.model.columns):
                row_values=row_values+self.table[i][j].get()+'|'
            table_values=table_values+row_values+'~'
        return table_values

    def validate_date(self,date_str):
        try:
            datetime.strptime(date_str, '%d/%m/%y')
            return True
        except ValueError:
            return False

    def sort_data(self):
        table_array=[]
        for i in range(controller.model.rows):
            row_array=[]
            for j in range(1,controller.model.columns):
                #row_values=row_values+self.table[i][j].get()+'|'
                row_array.append(self.table[i][j].get())
            table_array.append(row_array)
        print(table_array)    
        #table_array.sort(key=lambda t: datetime.strptime(t[3],'%d/%m/%y'))
        sorted_d=sorted(table_array,key=lambda t: datetime.strptime(t[3] ,'%d/%m/%y') if self.validate_date(t[3]) else datetime.min)

        for x in sorted_d :
            print(x)
        #
        #put sorted entries back to table
        for i in range(controller.model.rows):
            for j in range(0,controller.model.columns-1):
                #row_values=row_values+self.table[i][j].get()+'|'
                self.table[i][j+1].set(sorted_d[i][j])
        
        
    def add_one_row(self):
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
              
        
    def GetFinancialYear(self,detstr):
        FY="-"
        keymonths=['01','02','03']
        if  detstr[3:5] in keymonths: 
                yearint=int(detstr[6:8])
                FY="FY-"+str(yearint-1)+'-'+str(yearint)
        else : 
                yearint=int(detstr[6:8])
                FY="FY-"+str(yearint)+'-'+str(yearint+1)
        return FY        
    
    
    def delete_row(self,ro,co):       #same as copy upper row, code for del row pending
        #temp=self.table[ro][co].get()
        if ro>2 :
            for c in range(1,controller.model.columns):
              temp=self.table[ro-3][c].get()
              self.table[ro-2][c].set(temp)
              print(temp)  
    
    def GetIncome(self,rownum):
          principle=self.table[rownum][1].get() 
          maturity =self.table[rownum][2].get()
          income=int(maturity) - int(principle)
          return income

    def get_header(self):
        html="<!DOCTYPE html>\n"
        html+="<html>\n"
        html+="<style>\n"
        html+="table\n"
        html+="{table-layout:fixed;\n"
        html+="width:100%;\n"
        html+="border:none;\n"
        html+="td\n"
        html+="{border:2px black double}\n"
        html+="}\n"
        html+="</style>\n"
        html+="<body>\n"
        html+="<table>\n"
        return html
              
    def fy_report(self):
        print("report")
        self.sort_data()
        html_doc=self.get_header()
        
        FY_list=[]
        NEM_list=[]
        for i in range(controller.model.rows):
            strdate=self.table[i][4].get()          # column 4 : To dates
            NEM_list.append(self.table[i][8].get()) # column 8 : Depositor Name
            FY=self.GetFinancialYear(strdate)
            FY_list.append(FY)
            #print(strdate,FY)
        FY_set=set(FY_list)        # remove dulicates
        FY_list=sorted(FY_set)     # sort uniqe-FY list in ascending order
        NEM_set=set(NEM_list)      # remove duplicate depositor names
        NEM_list=sorted(NEM_set)   # sort depositor Names and convert to list
        #print(FY_list)
        #print(NEM_list)
        for n in NEM_list:
            print("===="+n+"====")
            for f in FY_list :
                incomelist=[]
                totalincome=0
                for i in range(controller.model.rows):
                    curname=self.table[i][8].get()
                    if curname != n : continue
                    curdate=self.table[i][4].get()
                    fy=self.GetFinancialYear(curdate)
                    if fy != f : continue
                    income=self.GetIncome(i)
                    srnumb=self.table[i][0].get()
                    banknem=self.table[i][7].get()
                    totalincome=totalincome+income
                    incomelist.append(srnumb+"] "+curdate+":"+banknem+":"+str(income))
                    
                #print(f, str(totalincome)  )
                #print(incomelist) 
                html_doc+="<tr><td>\n"
                html_doc+=n
                html_doc+=" :"+f+" : "+str(totalincome)
                html_doc+="</td>\n"
                html_doc+="</tr>\n" 
                html_doc+="<tr>\n"   
                column=1
                for z in incomelist:
                    html_doc+="<td>\n"
                    html_doc+=z
                    html_doc+="</td>\n"
                    if column%5 == 0 : 
                        html_doc+="</tr><tr>\n"         
                        if len(incomelist)==(column-1) :  html_doc+="<\tr>\n"
                    column=column+1
                html_doc+="<tr><td style=\"border:none;\">&nbsp</td></tr>\n"
        with open("fd_reort.html", "w") as file:
            file.write(html_doc)
        print("table saved as fd_table.html")                   
        print("html report saved")                
        
        
        
        #for i in range(controller.model.rows):
        #    income=self.GetIncome(i)       
        #    print(str(i)+"] "+str(income))
                
            
               
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
        #print(x)
        r=0
        for y in x:
          if not '|' in y : continue
          z=y.split('|')
          if r>(self.model.rows-1) : 
             self.view.add_one_row()
          for c in range(0,8):  
             self.view.table[r][c+1].set(z[c])
            #print(r,c)
          r=(r+1) 
        return  


    def save_table(self):
        #self.model.save_html_table()
        table_array=self.view.get_table_array()
        self.model.save_html_table(table_array)
       # print(table_array)
       
    def cr_report(self):
        table_array=self.view.get_table_array()
        #self.model.save_html_table(table_array)
        print(table_array)
                
    def add_row(self):
        self.view.add_one_row()
        
    def del_row(self):
        self.view.del_one_row()    
    
    def sort_table(self):
        self.view.sort_data()
         
    def fy_report(self):
        self.view.fy_report()
        
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
    
    def delete_current_row(event): 
        widget = root.focus_get()
        if isinstance(widget,tk.Entry) :
            row=widget.grid_info()['row']
            col=widget.grid_info()['column']
            controller.view.delete_row(row,col)            
        else :
            print("noentry")     
        
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
    root.bind('<Control-d>',delete_current_row)

    root.mainloop()
