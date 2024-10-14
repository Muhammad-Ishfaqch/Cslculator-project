import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression entered in the text field
def evaluate_expression():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to update the entry field with the button press
def button_press(value):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current_text + str(value))

# Function to clear the entry field
def clear_field():
    entry_field.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("Fantastic Calculator")
window.geometry("400x600")
window.configure(bg="#d3e0ea")  # Set a nice background color

# Set window icon (favicon-like)
icon = tk.PhotoImage(file='favicon.PNG') 
window.iconphoto(False, icon)

# Creating the entry field
entry_field = tk.Entry(window, font=("Arial", 24), borderwidth=5, relief="ridge", justify='center')
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout
button_texts = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Loop through the button_texts to create buttons
for row_idx, row in enumerate(button_texts):
    for col_idx, button_text in enumerate(row):
        if button_text == "=":
            button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 18), bg="#53c653", fg="white", command=evaluate_expression)
        elif button_text == "C":
            button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 18), bg="#e74c3c", fg="white", command=clear_field)
        else:
            button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 18), bg="#3498db", fg="white", command=lambda value=button_text: button_press(value))
        
        button.grid(row=row_idx+1, column=col_idx, padx=10, pady=10)

# Start the Tkinter main loop
window.mainloop()
