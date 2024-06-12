# event handling
# Import the Required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to display the message
def display_text(e):
    label.config(text="Code never lies, comments sometimes do", font=('Helvetica 17 bold'))

# Create a label widget to add some text
label = Label(win, text="")
label.pack(pady=50)

# Bind the Mouse button event
win.bind('<Button-1>', display_text)
win.mainloop()


# canvases and message boxes
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Canvas Example")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Draw a rectangle on the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Draw a circle on the canvas
canvas.create_oval(200, 200, 250, 250, fill="red")

# Draw a line on the canvas
canvas.create_line(100, 100, 300, 300, fill="green", width=5)

# Draw some text on the canvas
canvas.create_text(150, 250, text="Hello, World!", font=("Helvetica", 24))

# Run the Tkinter event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create a Tkinter window
root = tk.Tk()
root.title("Message Box Example")

# Create a button that shows a message box when clicked
def show_message():
    messagebox.showinfo("Information", "This is an information message.")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

# Create a button that shows an error message box when clicked
def show_error():
    messagebox.showerror("Error", "This is an error message.")

button = tk.Button(root, text="Show Error", command=show_error)
button.pack()

# Create a button that shows a warning message box when clicked
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

button = tk.Button(root, text="Show Warning", command=show_warning)
button.pack()

# Create a button that shows an askyesno message box when clicked
def ask_yes_no():
    response = messagebox.askyesno("Question", "Do you want to continue?")
    if response:
        print("You clicked Yes")
    else:
        print("You clicked No")

button = tk.Button(root, text="Ask Yes/No", command=ask_yes_no)
button.pack()

# Run the Tkinter event loop
root.mainloop()


# storing text from a textbox in a python variable
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Store Text in Variable")

# Create a Text widget (textbox)
text_box = tk.Text(root, width=40, height=10)
text_box.pack()

# Create a variable to store the text
text_variable = ""

# Create a button to get the text from the textbox and store it in the variable
def get_text():
    global text_variable
    text_variable = text_box.get("1.0", "end-1c")
    print("Text stored in variable:", text_variable)

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

# Run the Tkinter event loop
root.mainloop()



# simple calculator
import tkinter as tk

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(root, text="Clear", width=10, command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()


# button clicked
import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Button Click Example")

button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack()

root.mainloop()