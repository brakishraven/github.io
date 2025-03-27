import tkinter as tk
import math
import re
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("Calculator")


def preprocess_expression(expression):
    expression = expression.replace("^", "**")

    expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
    expression = re.sub(r'(\))(\()', r'\1*\2', expression)

    return expression

def plot_graph():
    try:
        expression = preprocess_expression(entry.get())
        x = sp.symbols('x')
        expr = sp.sympify(expression)

        x_vals = np.linspace(-10, 10, 400)
        y_vals = []
        
        for val in x_vals:
            y_val = expr.subs(x, val).evalf()
            if y_val.is_real:
                y_vals.append(float(y_val))
            else:
                y_vals.append(float('nan')) 
        
        ax.clear()
        ax.plot(x_vals, y_vals, label=expression, color='blue')
        ax.axhline(0, color='black', linewidth=1) 
        ax.axvline(0, color='black', linewidth=1)  
        ax.legend()

        canvas.draw() 

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error: {str(e)}")  

def button_x():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "x")

fig, ax = plt.subplots(figsize=(4, 3))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=2, column=8, rowspan=5, padx=20, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_square():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result**2))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 

def button_srqt():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result**0.5))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_para(opening):
    try:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + opening)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_para(close):
    try:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + close)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_int():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, "∫" + current)

def button_pi():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(math.pi))\
    
def button_e():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(math.e))



def button_backspace():
    current_text = entry.get()
    entry.delete(len(current_text), tk.END)

def button_equal(event=None):
    try:
        expression = entry.get().replace("pi", str(math.pi))
        expression = expression.replace("∫", "")  

        
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression) 
        
        if "x" in expression:
            plot_graph()
            return
        if "∫" in entry.get():
            x = sp.symbols('x')
            expr = sp.sympify(expression)
            integral = sp.integrate(expr, x)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(integral))
        else:
            result = eval(expression, {"__builtins__": None}, {"pi": math.pi, "e": math.e, "sqrt": math.sqrt, "pow": pow})
            
            result_display = str(result).replace("**", "^").replace("*", "") 
            
            entry.delete(0, tk.END)
            entry.insert(tk.END, result_display)  
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


entry = tk.Entry(window, width=50, font=("Arial", 24), borderwidth=0)
entry.grid(row=0, column=1, columnspan=8, padx=10, pady=20)
entry.focus_set()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 1), ("+", 4, 3), ("x", 4, 0)
]
    

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, padx=40, pady=40, command=button_equal)
    else:
         button = tk.Button(window, text=text, padx=40, pady=40,font=("Arial", 20), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

button_clear = tk.Button(window, text="Clear", padx=30, pady=60, command=button_clear)
button_clear.grid(row=5, column=1)

button_enter = tk.Button(window, text="Enter", padx=30, pady=60, command=button_equal)
button_enter.grid(row=5, column=2)

button_period = tk.Button(window, text=".", padx=40, pady=60, command=lambda: button_click("."))
button_period.grid(row=5, column=0)

button_square = tk.Button(window, text="^", padx=40, pady=40, command=button_square)
button_square.grid(row=1, column=5)

button_sqrt = tk.Button(window, text="√", padx=40, pady=40, command=button_srqt)
button_sqrt.grid(row=2, column=5)

button_opening = tk.Button(window, text="(", padx=40, pady=40, command=lambda: button_para("("))
button_opening.grid(row=3, column=5)

button_closing = tk.Button(window, text=")", padx=40, pady=40, command=lambda: button_para(")"))
button_closing.grid(row=4, column=5)

button_pi = tk.Button(window, text="π", padx=40, pady=40, command=button_pi)
button_pi.grid(row=4, column=2)

button_e = tk.Button(window, text="e", padx=40, pady=40, command=button_e)
button_e.grid(row=4, column=0)

button_int = tk.Button(window, text="Int", padx=40, pady=40, command=lambda: button_click("∫"))
button_int.grid(row=5, column=5)

button_x = tk.Button(window, text="x", padx=40, pady=40, command=button_x)
button_x.grid(row=3, column=4)

button_graph = tk.Button(window, text="Graph", padx=40, pady=40, font=("Arial", 15), command=plot_graph)
button_graph.grid(row=5, column=4, columnspan=1)

labels = [
    ("Hi there this program is quite rudimentary, but I am working on it,"
    "\nI am working on making it better, and will keep adding functions"
    "\nI hope you like it, and if you have any suggestions, please let me know."
    "\nSo far it can add, subtract, multiply, divide, square, square root, and use parentheses."
    "\nIt can also use pi and e, and it can use the period for decimals."
    "\nIt can also use the equal sign to get the result, and the clear button to clear the screen."
    "\nIt can also use the backspace button to delete the last character."
    "\nIt can also use the enter button to get the result."
     
     
    ,1, 8),
]

for text, row, col in labels:
    label = tk.Label(window, text=text, justify="left", font=("Arial", 15), anchor="w")
    label.grid(row=row, column=col, padx=0, pady=0, sticky="w")  # Align text to left

window.bind("<Return>", lambda event: button_equal()) 
window.bind("<BackSpace>", lambda event: button_backspace())  
window.bind("<Escape>", lambda event: button_clear()) 
window.mainloop()