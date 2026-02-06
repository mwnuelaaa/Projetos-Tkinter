import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Cash Converter")
window.geometry("600x600")
window.resizable(True, True)
window.config(bg="#662344")

# variável para guardar moeda escolhida
selected_currency = tk.StringVar()

# função de conversão
def convert_currency():
    try:
        amount = float(quant.get())
        currency = selected_currency.get()
        
        if currency == "USD":
            result_label.config(text=f"{amount} USD is equal to\n {amount * 5.25:.2f} BRL\n {amount * 0.85:.2f} EUR\n {amount * 110.25:.2f} JPY\n {amount * 0.75:.2f} GBP")
        elif currency == "EUR":
            result_label.config(text=f"{amount} EUR is equal to\n {amount * 6.15:.2f} BRL\n {amount * 1.15:.2f} USD\n {amount * 129.50:.2f} JPY\n {amount * 0.85:.2f} GBP")
        elif currency == "BRL":
            result_label.config(text=f"{amount} BRL is equal to\n {amount * 0.19:.2f} USD\n {amount * 0.16:.2f} EUR\n {amount * 21.00:.2f} JPY\n {amount * 0.13:.2f} GBP")    
        elif currency == "JPY":
            result_label.config(text=f"{amount} JPY is equal to\n {amount * 0.0095:.2f} USD\n {amount * 0.0077:.2f} EUR\n {amount * 0.048:.2f} BRL\n {amount * 0.0065:.2f} GBP")
        elif currency == "GBP":
            result_label.config(text=f"{amount} GBP is equal to\n {amount * 1.33:.2f} USD\n {amount * 1.17:.2f} EUR\n {amount * 7.80:.2f} BRL\n {amount * 153.50:.2f} JPY") 
        else:
            messagebox.showerror("Error", "Please select a currency to convert.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")     

# estrutura
label1 = tk.Label(window, text="Cash Converter", font=("Georgia", 18), bg="#662344", fg="#FFFFFF")
label1.pack(pady=10) 

label3 = tk.Label(window, text="Enter the amount you want to convert:", font=("Georgia", 12), bg="#662344", fg="#FFFFFF")
label3.pack(pady=10) 

quant = tk.Entry(window, width=20, font=("Georgia", 12), justify="center")
quant.pack(pady=15) 

label2 = tk.Label(window, text="Choose the currency you want to convert to others:", font=("Georgia", 12), bg="#662344", fg="#FFFFFF")
label2.pack(pady=10)

frame1 = tk.Frame(window, bg="#662344")
frame1.pack(pady=10)

# cada botão define a moeda escolhida
button1 = tk.Button(frame1, text="DOLLAR", width=10, bg="#8B8B8B", font=("Georgia", 10), fg="#FFFFFF", command=lambda: selected_currency.set("USD"))
button1.grid(row=0, column=0, padx=10)

button2 = tk.Button(frame1, text="EURO", width=10, bg="#8B8B8B", font=("Georgia", 10), fg="#FFFFFF", command=lambda: selected_currency.set("EUR"))
button2.grid(row=0, column=1, padx=10) 

button3 = tk.Button(frame1, text="REAL", width=10, bg="#8B8B8B", font=("Georgia", 10), fg="#FFFFFF", command=lambda: selected_currency.set("BRL")) 
button3.grid(row=0, column=2, padx=10) 

button4 = tk.Button(frame1, text="YEN", width=10, bg="#8B8B8B", font=("Georgia", 10), fg="#FFFFFF", command=lambda: selected_currency.set("JPY"))
button4.grid(row=1, column=0, padx=10, pady=10) 

button5 = tk.Button(frame1, text="LIBRA", width=10, bg="#8B8B8B", font=("Georgia", 10), fg="#FFFFFF", command=lambda: selected_currency.set("GBP"))
button5.grid(row=1, column=1, padx=10, pady=10 ) 

# botão para converter
convert_button = tk.Button(window, text="Convert", width=15, bg="#A8A8A8", font=("Georgia", 12), fg="#FFFFFF", command=convert_currency)
convert_button.pack(pady=10)

# resultado
result_label = tk.Label(window, text="", font=("Georgia", 12), bg="#662344", fg="#FFFFFF")
result_label.pack(pady=10) 

window.mainloop()
