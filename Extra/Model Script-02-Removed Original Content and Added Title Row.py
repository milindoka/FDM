import tkinter as tk
from tkinter import ttk

# Step 2: Create the Tkinter Window
root = tk.Tk()
root.title("Scrollable Grid Example")
root.geometry("720x250")



# Step 3: Create a Frame for Grid Layout
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Step 4: Create a Canvas and Scrollbar
canvas = tk.Canvas(frame)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Step 5: Create a Frame for Scrollable Content
content_frame = ttk.Frame(canvas)

# Step 6: Configure the Canvas and Scrollable Content Frame
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Step 7: ===================Add Widgets to the Content Frame=========
# Example widgets (replace with your own)

       #---create table title row----
    
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

                      
#==============================================================================
#==============================End Add Widgets======================================
# Step 8: Create Window Resizing Configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Step 9: Pack Widgets onto the Window
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Step 10: Bind the Canvas to Mousewheel Events
def _on_mousewheel(event):
   canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Step 11: Run the Tkinter Event Loop
root.mainloop()
