import tkinter as tk

# Function to perform the calculation
def click(button_value):
    current = display_var.get()
    if button_value == "AC":
        display_var.set("")
    elif button_value == "=":
        try:
            current = current.replace('÷', '/').replace('×', '*')
            result = eval(current)
            if result == int(result):
                display_var.set(str(int(result)))  
            else:
                display_var.set(str(result))  
        except ZeroDivisionError:
            display_var.set("Error")
        except Exception:
            display_var.set("Invalid input")
    elif button_value == "←":  
        display_var.set(current[:-1])  
    else:
        display_var.set(current + button_value)

# Create the main window
root = tk.Tk()
root.title("Calculator")


bg_color = "#282c34"  
button_color = "#3c4049"  
op_color = "#606469"  
highlight_color = "#ff6b6b" 
equals_color = "#4caf50" 
text_color = "#ffffff"  

# Create a StringVar for the display area
display_var = tk.StringVar()

# Create the display area
display_entry = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20, "bold"), bd=0, insertwidth=4, width=14, borderwidth=4, justify='right', bg=bg_color, fg=text_color)
display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

buttons = [
    ('AC', 1, 0, highlight_color), ('(', 1, 1, op_color), (')', 1, 2, op_color), ('÷', 1, 3, op_color),
    ('7', 2, 0, button_color), ('8', 2, 1, button_color), ('9', 2, 2, button_color), ('×', 2, 3, op_color),
    ('4', 3, 0, button_color), ('5', 3, 1, button_color), ('6', 3, 2, button_color), ('-', 3, 3, op_color),
    ('1', 4, 0, button_color), ('2', 4, 1, button_color), ('3', 4, 2, button_color), ('+', 4, 3, op_color),
    ('0', 5, 0, button_color), ('.', 5, 1, button_color), ('←', 5, 2, op_color), ('=', 5, 3, equals_color)
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

# Create and place buttons
for text, row, col, color in buttons:
    button = tk.Button(root, text=text, bg=color, command=lambda t=text: click(t), **btn_params)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure row and column weights for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.configure(bg=bg_color)

root.mainloop()
