import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Multiplication Table Generator - Beginner Project")
window.geometry("450x500")
window.resizable(True, True)
window.config(bg="#1D5791")

# Functionalities to be added later
def generate_table():
    try:
        number = int(entry.get())
        table = ""
        for i in range(1, 11):
            table += f"{number} x {i} = {number * i}\n"
            label_result.config(text=table)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.") 

def erase_table():
    entry.delete(0, tk.END)
    label_result.config(text="")


# Structure of the application
label1 = tk.Label(window, text="Multiplication Table Generator", font=("Georgia", 18), fg="#FFFFFF", bg="#1D5791") 
label1.pack(pady=10) 

label2 = tk.Label(window, text="Enter a integer number to generate its multiplication table:", font=("Georgia", 10), fg="#FFFFFF", bg="#1D5791")
label2.pack(pady=5) 

entry = tk.Entry(window, font="Georgia", fg="#000000", bg="#FFFFFF", width=15) 
entry.pack(pady=5) 

# Generate button and erase button

frame_buttons = tk.Frame(window, bg="#1D5791")
frame_buttons.pack(pady=10) 

gen_button = tk.Button(frame_buttons, text="Generate", font=("Georgia", 14), fg="#FFFFFF", bg="#A8A8A8", width=8, height=1, command=generate_table)
gen_button.pack(side="left", padx=10)

erase_button = tk.Button(frame_buttons, text="Erase", font=("Georgia", 14), fg="#FFFFFF", bg="#A8A8A8", width=8, height=1, command=erase_table) 
erase_button.pack(side="left", padx=10)

label_result = tk.Label(window, text="", font="Georgia", fg="#FFFFFF", bg="#1D5791") 
label_result.pack(pady=10) 

window.mainloop() 