# MESSAGE WIDGET
import tkinter as tk

root = tk.Tk()

message = tk.Message(root, text="This is a message widget\nwith multiple lines")
message.pack()

root.mainloop()

# BUTTON WIDGET
import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text="Click me!")
button.pack()

root.mainloop()


# RADIO BUTTON WIDGET
import tkinter as tk

root = tk.Tk()

var = tk.IntVar()

rb1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
rb2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
rb3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3)

rb1.pack()
rb2.pack()
rb3.pack()

root.mainloop()