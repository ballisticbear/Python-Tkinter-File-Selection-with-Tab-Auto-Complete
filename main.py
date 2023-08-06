import os
import tkinter as tk
from tkinter import filedialog

def is_valid_filename(filename):
    return os.path.isfile(filename)

def autocomplete(event):
    current_text = entry.get()
    matching_files = [file for file in os.listdir(".") if file.startswith(current_text)]
    if len(matching_files) == 1:
        entry.delete(0, tk.END)
        entry.insert(0, matching_files[0])

def validate_filename(event):
    filename = entry.get()
    if is_valid_filename(filename):
        entry.config({"background": "SpringGreen"})
    else:
        entry.config({"background": "Salmon"})

def browse_file():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)
    validate_filename(None)


if __name__ == '__main__':

    # Initilize the Tiknter window
    root = tk.Tk()
    root.title("File Selection")
    
    # Size and add padding to the window
    root.geometry("350x175")
    root.config(padx=10, pady=10)
    
    # Label
    label = tk.Label(root, text="Enter the filename:", font=("Helvetica", 16))
    label.pack(pady=10)

    # File name entry box
    entry = tk.Entry(root, width=50, font=("Calibri 12"), validate="focusout")
    entry.pack(pady=10)
    entry.bind("<FocusOut>", validate_filename)
    entry.bind("<Tab>", autocomplete)

    # File dialog button
    browse_button = tk.Button(root, text="Browse for File", font=("Helvetica", 12), command=browse_file)
    browse_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()