import tkinter as tk 
root = tk.Tk()
root.geometry("300x300")

def on_enter(e):
    button.config(cursor = circle)
def on_leave(e):
    button.config(cursor = cross)

button = tk.Button(root, text = "CHANGE CURSOR")
button.pack(pady=50)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
root.mainloop()