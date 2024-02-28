import sys
import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import threading
from tkinter import Toplevel, Frame, Entry, Button

# Assuming that you have the 'ai' function defined in the 'ai' module
from ai import send_to_gpt3

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".thonny2", filetypes=[("Thonny2 Files", "*.thonny2"), ("Python Files", "*.py"), ("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".thonny2", filetypes=[("Thonny2 Files", "*.thonny2"), ("Python Files", "*.py"), ("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

def run_file(event=None):
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

def open_website():
    website_window = Toplevel(root)
    website_window.title("Thonny 2 advanced")
    website_frame = Frame(website_window)
    website_frame.pack(expand="yes", fill="both")
    html_widget = tkhtml.HtmlFrame(website_frame)
    html_widget.set_content("<iframe src='xm9g.xyz' width='100%' height='100%'></iframe>")
    html_widget.pack(expand="yes", fill="both")

def ai(prompt):
    try:
        AIresponse = send_to_gpt3(prompt)
    except Exception as e:
        AIresponse = f"ERROR:\n{e}"
        warn("An error has occored with the AI\nPlease check that you have set up the api key correctly.")
    print(AIresponse)
    ai_text.insert(tk.END, AIresponse)
    
    
def warn(text):
    popup = tk.Toplevel(root)
    popup.title("Warning!")
    label = tk.Label(popup, text=text)
    label.pack(padx=10, pady=10)
    popup.iconbitmap("assets/warning.ico")
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Thonny 2")
root.iconbitmap("assets/logo.ico")


text = tk.Text(root, wrap="word", undo=True, bg="black", fg="white", insertbackground="white")
text.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

run_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Run Python File (ctrl+r)", command=run_file)

result_text = scrolledtext.ScrolledText(root, wrap="word", height=10, bg="black", fg="white", insertbackground="white")
result_text.pack(expand="yes", fill="both")





# Bind Ctrl+R to run_file function
root.bind("<Control-r>", run_file)

# New input box and button for AI function with increased size
ai_input = Entry(root, bg="white", fg="black", width=50)
ai_input.pack(side=tk.LEFT, padx=5)
ai_button = Button(root, text="Run AI", command=lambda: ai(ai_input.get()))
ai_button.pack(side=tk.LEFT, padx=5)

ai_text = scrolledtext.ScrolledText(root, wrap="word", height=10, bg="black", fg="white", insertbackground="white")
ai_text.pack(expand="yes", fill="both")

root.mainloop()
