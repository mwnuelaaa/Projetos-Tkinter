import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Number Verifier - Beginner Project") 
window.geometry("400x400")
window.resizable(True, True)
window.config(bg="#f7d275") 

# Funcionalities to be implemented
def verify_number():
    try:
        number = float(entry_number.get())
        if number == 0 and number % 2 == 0:
            result = "The number is zero and even."
        elif number > 0 and number % 2 == 0:
            result = "The number is positive and even."
        elif number > 0 and number % 2 != 0:
            result = "The number is positive and odd."
        elif number < 0 and number % 2 == 0:
            result = "The number is negative and even."
        elif number < 0 and number % 2 != 0:
            result = "The number is negative and odd."
        else:
            result = "Invalid input."
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return
    label_result.config(text=result) 

def clear_fields():
    entry_number.delete(0, tk.END)
    label_result.config(text="") 
    
# Structure of the program

label1 = tk.Label(window, text="Number Verifier", font=("Georgia", 18), bg="#f7d275", fg="#FFFFFF") 
label1.pack(pady=10) 

label2 = tk.Label(window, text="Enter a number to verify if it's:\n even or odd \n positive or negative:", font=("Georgia", 11), bg="#f7d275", fg="#FFFFFF")
label2.pack(pady=10) 

entry_number = tk.Entry(window, font=("Georgia", 15)) 
entry_number.pack(pady=10) 

# Buttons

frame_buttons = tk.Frame(window, bg="#f7d275")
frame_buttons.pack(pady=10)

verify_button = tk.Button(frame_buttons, text="Verifiy", font=("Georgia", 14), bg="#A8A8A8", fg="#FFFFFF", command=verify_number)
verify_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(frame_buttons, text="Clear", font=("Georgia", 14), bg="#A8A8A8", fg="#FFFFFF", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=10) 

# Result label 

label_result = tk.Label(window, text="", font=("Georgia", 14), bg="#f7d275", fg="#FFFFFF")
label_result.pack(pady=15) 

window.mainloop() 