import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Vogals and Consonants Counter")
window.geometry("550x400")
window.resizable(True, True)
window.config(bg="#9D57BB")

# Functionalities to be implemented
def verify():
    phrase = entry_phrase.get() 
    vogals = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count_vogals = sum(1 for char in phrase if char in vogals)
    count_consonants = sum(1 for char in phrase if char in consonants)
    label_result.config(text=f"Vogals: {count_vogals} | Consonants: {count_consonants}") 

def erase():
    entry_phrase.delete(0, tk.END)
    label_result.config(text="") 


# Structure 

label1 = tk.Label(window, text="Vogals and Consonants Counter", bg="#9D57BB", fg="#FFFFFF", font=("Georgia", 17))
label1.pack(pady=10) 

label2 = tk.Label(window, text="Enter a phrase:", bg="#9D57BB", fg="#FFFFFF", font=("Georgia", 11))
label2.pack(pady=5) 

entry_phrase = tk.Entry(window, width=30, font=("Georgia", 12), fg="#000000")
entry_phrase.pack(pady=5) 

# Buttons 

frame_buttons = tk.Frame(window, bg="#9D57BB")
frame_buttons.pack(pady=10)

button_verify = tk.Button(frame_buttons, text="Verify", bg="#A8A8A8", fg="#FFFFFF", font=("Georgia", 14), command=verify)
button_verify.pack(side=tk.LEFT, padx=10)

erase_button = tk.Button(frame_buttons, text="Erase", bg="#A8A8A8", fg="#FFFFFF", font=("Georgia", 14), command=erase) 
erase_button.pack(side=tk.RIGHT, padx=10) 

# Result label

label_result = tk.Label(window, text="", bg="#9D57BB", fg="#FFFFFF", font=("Georgia", 16))
label_result.pack(pady=15) 

window.mainloop() 