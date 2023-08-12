import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    include_uppercase = uppercase_var.get()

    char_set = string.ascii_lowercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation
    if include_uppercase:
        char_set += string.ascii_uppercase

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_text.delete("1.0", tk.END)  # Clear previous text
    password_text.insert("1.0", password)

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")  # Set initial dimensions to 400x300

length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_text = tk.Text(window, height=2, width=30)
password_text.pack()

window.mainloop()
