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