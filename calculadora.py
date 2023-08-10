import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        entry.insert(0, f_num / float(second_number))

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

for i in range(1, 10):
    row = (i - 1) // 3 + 1
    col = (i - 1) % 3
    button = tk.Button(root, text=str(i), padx=20, pady=20, command=lambda i=i: button_click(i))
    button.grid(row=row, column=col)

buttons = [
    ("0", 0, 3),
    (".", 4, 3),
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 2),
    ("=", 4, 0),
    ("C", 0, 5)
]

for label, row, col in buttons:
    button = tk.Button(root, text=label, padx=20, pady=20)
    if label == "=":
        button.config(command=button_equal)
    elif label == "C":
        button.config(command=button_clear)
    elif label in "+-*/":
        if label == "+":
            button.config(command=button_add)
        elif label == "-":
            button.config(command=button_subtract)
        elif label == "*":
            button.config(command=button_multiply)
        elif label == "/":
            button.config(command=button_divide)
    else:
        button.config(command=lambda label=label: button_click(label))
    button.grid(row=row, column=col)

root.mainloop()
