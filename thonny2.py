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

def run_file():
    content = text.get("1.0", tk.END)
    with open("temp_file.py", "w") as temp_file:
        temp_file.write(content)

    global process
    process = subprocess.Popen(["python", "temp_file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def monitor_process():
        output, error = process.communicate()
        result_window = tk.Toplevel(root)
        result_window.title("Python Terminal Output")

        # Create a scrolled text widget to display output
        output_text = scrolledtext.ScrolledText(result_window, wrap="word", bg="black", fg="white", insertbackground="white")
        output_text.pack(expand="yes", fill="both")

        # Display the output and error
        output_text.insert(tk.END, output)
        output_text.insert(tk.END, error)

    # Start a separate thread to monitor the process
    threading.Thread(target=monitor_process).start()

def stop_execution():
    if 'process' in globals():
        process.terminate()

# Create the main window
root = tk.Tk()
root.title("Thonny 2")

# Create a text widget
text = tk.Text(root, wrap="word", undo=True, bg="black", fg="white", insertbackground="white")
text.pack(expand="yes", fill="both")

# Create a menu
menu = tk.Menu(root, bg="black")
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run button
run_button = tk.Button(root, text="Run", command=run_file)
run_button.pack(side=tk.LEFT, padx=5)

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_execution)
stop_button.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()
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

def run_file():
    content = text.get("1.0", tk.END)
    with open("temp_file.py", "w") as temp_file:
        temp_file.write(content)

    global process
    process = subprocess.Popen(["python", "temp_file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def monitor_process():
        output, error = process.communicate()
        result_window = tk.Toplevel(root)
        result_window.title("Python Terminal Output")

        # Create a scrolled text widget to display output
        output_text = scrolledtext.ScrolledText(result_window, wrap="word", bg="black", fg="white", insertbackground="white")
        output_text.pack(expand="yes", fill="both")

        # Display the output and error
        output_text.insert(tk.END, output)
        output_text.insert(tk.END, error)

    # Start a separate thread to monitor the process
    threading.Thread(target=monitor_process).start()

def stop_execution():
    if 'process' in globals():
        process.terminate()

# Create the main window
root = tk.Tk()
root.title("Thonny 2")

# Create a text widget
text = tk.Text(root, wrap="word", undo=True, bg="black", fg="white", insertbackground="white")
text.pack(expand="yes", fill="both")

# Create a menu
menu = tk.Menu(root, bg="black")
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run button
run_button = tk.Button(root, text="Run", command=run_file)
run_button.pack(side=tk.LEFT, padx=5)

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_execution)
stop_button.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()
