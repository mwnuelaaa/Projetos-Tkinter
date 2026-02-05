# simple calculator application using tkinter

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple Calculator - Beginner Project")
window.geometry("450x550")
window.config(bg="#F1BFDE")
window.resizable(True, True)

# Functionality to be added later
def add_to_entry(value):
    entry.insert(tk.END, value) 

label = tk.Label(window, text="Calculator", font="Georgia", fg="#FFFFFF", bg="#F1BFDE")
label.pack(pady=10)  

entry = tk.Entry(window, font="Georgia", fg="#000000", bg="#FFFFFF", width=25)
entry.pack(pady=10) 

frame_numbers = tk.Frame(window, bg="#F1BFDE")
frame_numbers.pack(pady=10) 

# Result function
def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END) 


# Number buttons
button0 = tk.Button(frame_numbers, text="0", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("0")) 
button0.grid(row=0, column=0, padx=5, pady=5) 

button1 = tk.Button(frame_numbers, text="1", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("1"))
button1.grid(row=0, column=1, padx=5, pady=5) 

button2 = tk.Button(frame_numbers, text="2", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("2"))
button2.grid(row=0, column=2, padx=5, pady=5) 

button3 = tk.Button(frame_numbers, text="3", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("3"))
button3.grid(row=1, column=0, padx=5, pady=5) 

button4 = tk.Button(frame_numbers, text="4", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("4"))
button4.grid(row=1, column=1, padx=5, pady=5) 

button5 = tk.Button(frame_numbers, text="5", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("5"))
button5.grid(row=1, column=2, padx=5, pady=5) 

button6 = tk.Button(frame_numbers, text="6", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("6"))
button6.grid(row=2, column=0, padx=5, pady=5)

button7 = tk.Button(frame_numbers, text="7", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("7"))
button7.grid(row=2, column=1, padx=5, pady=5)

button8 = tk.Button(frame_numbers, text="8", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("8"))
button8.grid(row=2, column=2, padx=5, pady=5) 

button9 = tk.Button(frame_numbers, text="9", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("9"))
button9.grid(row=3, column=1, padx=5, pady=5) 

frame_operations = tk.Frame(window, bg="#F1BFDE")
frame_operations.pack(pady=10)

# Operations buttons 
button_add = tk.Button(frame_operations, text="+", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("+")) 
button_add.grid(row=0, column=0, padx=5, pady=5)

button_sub = tk.Button(frame_operations, text="-", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("-"))
button_sub.grid(row=0, column=1, padx=5, pady=5)

button_mult = tk.Button(frame_operations, text="*", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("*"))
button_mult.grid(row=0, column=2, padx=5, pady=5)

button_div = tk.Button(frame_operations, text="/", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=lambda: add_to_entry("/"))
button_div.grid(row=0, column=3, padx=5, pady=5) 

# Result button 
button_result = tk.Button(window, text="=", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=4, height=1, command=calculate_result)  
button_result.pack(pady=10)   

window.mainloop() 