# message widget
import tkinter as tk

master = tk.Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tk.mainloop()

# radio button widget
import tkinter as tk

def get_selected():
    print("You selected:", variable.get())

master = tk.Tk()

variable = tk.StringVar()
variable.set("Option1")  # default value

tk.Label(master, text="Select an option:").pack()

tk.Radiobutton(master, text="Option1", variable=variable, value="Option1").pack()
tk.Radiobutton(master, text="Option2", variable=variable, value="Option2").pack()
tk.Radiobutton(master, text="Option3", variable=variable, value="Option3").pack()

tk.Button(master, text="Get Selected", command=get_selected).pack()

tk.mainloop()


# overview of tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack()

# Create an entry field
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked!"))
button.pack()

# Create a checkbox
checkbox = tk.Checkbutton(root, text="Check me!")
checkbox.pack()

# Create a radio button
radio_button = tk.Radiobutton(root, text="Radio button 1", value=1)
radio_button.pack()

# Create a listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()

# Create a text area
text_area = tk.Text(root, height=5, width=20)
text_area.pack()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start the GUI event loop
root.mainloop()


# setting up tkinter
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("My Tkinter Window")

# Set the size of the window
root.geometry("400x300")

# Set the background color of the window
root.configure(background="light blue")

# Create a label to display a message
label = tk.Label(root, text="Welcome to my Tkinter window!")
label.pack()

# Start the GUI event loop
root.mainloop()


# window
import tkinter as tk

root = tk.Tk()
root.mainloop()


# button label
import tkinter as tk

root = tk.Tk()

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack()

# Create a button
button = tk.Button(root, text="Click me!")
button.pack()

root.mainloop()



#entry text
import tkinter as tk

root = tk.Tk()

# Create an entry text field
entry = tk.Entry(root, width=20)
entry.pack()

# Create a label to display the entered text
label = tk.Label(root, text="")
label.pack()

# Create a button to get the entered text
def get_text():
    text = entry.get()
    label.config(text=text)

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

root.mainloop()



# frame
import tkinter as tk

root = tk.Tk()

# Create a frame
frame = tk.Frame(root, bg="gray", bd=5)
frame.pack()

# Add some widgets to the frame
label = tk.Label(frame, text="Hello, World!")
label.pack()

button = tk.Button(frame, text="Click me!")
button.pack()

root.mainloop()


# geometry management pack
import tkinter as tk

root = tk.Tk()

# Create three labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Use the pack geometry manager to add the labels to the window
label1.pack()
label2.pack()
label3.pack()

root.mainloop()


# grid place
import tkinter as tk

root = tk.Tk()

# Create six labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")
label4 = tk.Label(root, text="Label 4")
label5 = tk.Label(root, text="Label 5")
label6 = tk.Label(root, text="Label 6")

# Use the grid geometry manager to add the labels to the window
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
label5.grid(row=2, column=0)
label6.grid(row=2, column=1)

root.mainloop()


# event handling
import tkinter as tk

def button_clicked():
    print("Button clicked!")

def mouse_moved(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

def key_pressed(event):
    print(f"Key pressed: {event.char}")

root = tk.Tk()

# Create a button
button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack()

# Create a label to display mouse movements
label = tk.Label(root, text="Move the mouse over me!")
label.pack()

# Bind the mouse movement event to the label
label.bind("<Motion>", mouse_moved)

# Bind the key press event to the root window
root.bind("<Key>", key_pressed)

root.mainloop()
