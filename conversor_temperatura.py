# simple converter application in tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk 

window = tk.Tk()
window.title("Temperature Converter - Beginner Project")
window.geometry("450x350") 
window.resizable(True, True)
window.config(bg="#EEB0D5")

# Structure of the application
label1 = tk.Label(window, text="Temperature Converter", font="Georgia", fg="#FFFFFF", bg="#EEB0D5")   
label1.pack(pady=10) 

label2 = tk.Label(window, text="Insert the type of temperature to convert: \n(Celsius, Fahrenheit or Kelvin)", font="Georgia", fg="#FFFFFF", bg="#EEB0D5")
label2.pack(pady=5) 

opcoes = ttk.Combobox(window, values=["Celsius", "Fahrenheit", "Kelvin"], font="Georgia", state="readonly", width=15)
opcoes.pack(pady=5) 

label3 = tk.Label(window, text="Insert the value to convert:", font="Georgia", fg="#FFFFFF", bg="#EEB0D5")
label3.pack(pady=5)

entry = tk.Entry(window, font="Georgia", fg="#000000", bg="#FFFFFF", width=15) 
entry.pack(pady=5) 

# Convert button

def convert_temperature():
    try:
        temp_type = opcoes.get()
        temp_value = float(entry.get())

        if temp_type == "Celsius":
            fahrenheit = (temp_value * 9/5) + 32
            kelvin = temp_value + 273.15
            result = f"{temp_value} °C = {fahrenheit:.2f}°F e {kelvin:.2f}K"
            label_result.config(text=result)
        elif temp_type == "Fahrenheit":
            celsius = (temp_value - 32) * 5/9
            kelvin = celsius + 273.15
            result = f"{temp_value} °F = {celsius:.2f}°C e {kelvin:.2f}K"
            label_result.config(text=result)
        elif temp_type == "Kelvin":
            celsius = temp_value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result = f"{temp_value} K = {celsius:.2f}°C e {fahrenheit:.2f}°F"
            label_result.config(text=result)
        else:
            messagebox.showerror("Error", "Please slect a temperature type.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid temperature value.")
        return 

botao_converter = tk.Button(window, text="Convert", font="Georgia", fg="#FFFFFF", bg="#A8A8A8", width=8, height=1, command=convert_temperature)
botao_converter.pack(pady=10) 

label_result = tk.Label(window, text="", font="Georgia", fg="#FFFFFF", bg="#EEB0D5")
label_result.pack(pady=10) 

window.mainloop() 