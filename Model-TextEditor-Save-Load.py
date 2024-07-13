import tkinter as tk
from tkinter import filedialog

# Function to open a text file and load its content into the Text widget
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete("1.0", tk.END)  # Clear the Text widget
            text_widget.insert(tk.END, file.read())  # Insert file content

# Function to save the content of the Text widget to a text file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", tk.END))  # Write Text widget content to file

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create a Text widget for text editing
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create a "Open File" button to load a text file
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a "Save" button to save changes to the file
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
