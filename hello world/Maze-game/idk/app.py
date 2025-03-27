import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Canvas Example")

# Set canvas dimensions
canvas_width = 600
canvas_height = 400

# Create the canvas widget
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw shapes on the canvas (example)
# Draw a line
canvas.create_line(50, 50, 200, 50, fill="black")
# Draw a rectangle
canvas.create_rectangle(50, 100, 200, 150, fill="lightblue")
# Draw a circle (oval)
canvas.create_oval(50, 200, 200, 250, outline="red")

# Add text to the canvas
canvas.create_text(300, 300, text="Hello, Canvas!", font=("Arial", 16))


# Start the Tkinter event loop
window.mainloop()
