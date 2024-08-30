import tkinter as tk
import math 

# Global flag to track if the last button pressed was "="
new_calculation = False

# Function to perform the calculation
def click(button_value):
    global new_calculation
    current = display_var.get()
    
    if button_value == "AC":
        display_var.set("")
        new_calculation = False
    elif button_value == "=":
        try:
            # Substituting symbols with Python's operators before evaluation
            current = current.replace('÷', '/').replace('×', '*').replace('^', '**')
            if '√' in current:
                current = current.replace('√', 'math.sqrt')
            result = eval(current)
            if result == int(result):
                display_var.set(str(int(result)))
            else:
                display_var.set(str(result))
            new_calculation = True  # Setting a flag to indicate that a new calculation should start
        except ZeroDivisionError:
            display_var.set("Error")
            new_calculation = True
        except Exception:
            display_var.set("Invalid input")
            new_calculation = True
    elif button_value == "←":  
        display_var.set(current[:-1])  
    else:
        # If a number is pressed after a result, then a new calculation starts
        if new_calculation and button_value.isdigit():
            display_var.set(button_value)
            new_calculation = False
        else:
            display_var.set(current + button_value)
            new_calculation = False

# Creating the main window
root = tk.Tk()
root.title("Calculator")

bg_color = "#282c34"  
button_color = "#3c4049"  
op_color = "#606469"  
highlight_color = "#ff6b6b" 
equals_color = "#4caf50" 
text_color = "#ffffff"  

# Creating a StringVar for the display area
display_var = tk.StringVar()

# Creating the display area
display_entry = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20, "bold"), bd=0, insertwidth=4, width=14, borderwidth=4, justify='right', bg=bg_color, fg=text_color)
display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

buttons = [
    ('AC', 1, 0, highlight_color), ('(', 1, 1, op_color), (')', 1, 2, op_color), ('÷', 1, 3, op_color),
    ('7', 2, 0, button_color), ('8', 2, 1, button_color), ('9', 2, 2, button_color), ('×', 2, 3, op_color),
    ('4', 3, 0, button_color), ('5', 3, 1, button_color), ('6', 3, 2, button_color), ('-', 3, 3, op_color),
    ('1', 4, 0, button_color), ('2', 4, 1, button_color), ('3', 4, 2, button_color), ('+', 4, 3, op_color),
    ('0', 5, 0, button_color), ('.', 5, 1, button_color), ('←', 5, 2, op_color), ('=', 5, 3, equals_color),
    ('^', 6, 0, op_color), ('√', 6, 1, op_color)  
]

btn_params = {
    "font": ("Helvetica", 15, "bold"),
    "fg": text_color,
    "width": 4,
    "height": 2,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0,
    "highlightbackground": bg_color,
    "highlightcolor": bg_color,
    "border": 0,
    "borderwidth": 0,
    "activebackground": op_color
}

# Creating and placing buttons
for text, row, col, color in buttons:
    button = tk.Button(root, text=text, bg=color, command=lambda t=text: click(t), **btn_params)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configuring row and column weights for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):  
    root.grid_rowconfigure(i, weight=1)

root.configure(bg=bg_color)

root.mainloop()
