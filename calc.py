import tkinter as tk

# Function to update the entry field with the button clicked or Enter key pressed
def update_entry(char):
    entry.insert(tk.END, char)

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid input!")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character in the entry field
def delete_char():
    entry.delete(len(entry.get()) - 1)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
numbers = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1)
]

for number, row, col in numbers:
    button = tk.Button(window, text=number, width=5, command=lambda num=number: update_entry(num))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create arithmetic operation buttons
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
]

for operation, row, col in operations:
    button = tk.Button(window, text=operation, width=5, command=lambda op=operation: update_entry(op))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the equal button
equal_button = tk.Button(window, text="=", width=5, command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# Create "Clear" and "Delete" buttons
clear_button = tk.Button(window, text="Clear", width=5, command=clear_entry)
clear_button.grid(row=4, column=0, padx=5, pady=5)

delete_button = tk.Button(window, text="Delete", width=5, command=delete_char)
delete_button.grid(row=4, column=1, padx=5, pady=5)

# Create display buttons
display_button = tk.Button(window, text="(", width=5, command=lambda: update_entry("("))
display_button.grid(row=5, column=0, padx=5, pady=5)

display_button = tk.Button(window, text=")", width=5, command=lambda: update_entry(")"))
display_button.grid(row=5, column=1, padx=5, pady=5)

display_button = tk.Button(window, text="%", width=5, command=lambda: update_entry("%"))
display_button.grid(row=5, column=2, padx=5, pady=5)

# Run the main event loop
window.mainloop()
