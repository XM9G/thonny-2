import sys
import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import threading



def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

def run_file(event=None):  # Added event parameter for binding
    content = text.get("1.0", tk.END)
    with open("sandbox/temp_file.py", "w") as temp_file:
        temp_file.write(content)

    process = subprocess.Popen(["python", "sandbox/temp_file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    def update_output():
        while process.poll() is None:
            output = process.stdout.readline()
            error = process.stderr.readline()
            result_text.insert(tk.END, output + error)
            result_text.yview(tk.END)
        
    threading.Thread(target=update_output).start()

def stop_execution():
    if 'process' in globals() and process.poll() is None:
        process.terminate()

# Create the main window
root = tk.Tk()
root.title("Thonny 2")
root.iconbitmap("assets/logo.ico")

# Create a text widget for code input
text = tk.Text(root, wrap="word", undo=True, bg="black", fg="white", insertbackground="white")
text.pack(expand="yes", fill="both" )

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run menu
run_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Run Python File (ctrl+r)", command=run_file)

# Create a text widget for result output with a smaller height
result_text = scrolledtext.ScrolledText(root, wrap="word", height=10, bg="black", fg="white", insertbackground="white")
result_text.pack(expand="yes", fill="both" )

# Bind Ctrl+R to run_file function
root.bind("<Control-r>", run_file)

# Run the Tkinter event loop
root.mainloop()
