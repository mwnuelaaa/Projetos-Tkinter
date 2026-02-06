import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Sun, Moon, Star - Message Game")
window.geometry("600x200")
window.config(bg="#F0F0F0")

# messages

def sun_message():
    messagebox.showinfo("Sun Message", "You shine bright! Keep spreading your warmth and positivity!!")

def moon_message():
    messagebox.showinfo("Moon Message", "You are gentle and calm. Your light guides others through darkness.")

def star_message():
    messagebox.showinfo("Star Message", "You are a shining example of brilliance and hope.")

# structure

label1 = tk.Label(window, text="Welcome to the Sun, Moon, Star; Message Game!", font=("Georgia", 16), bg="#F0F0F0", fg="#000000")
label1.pack(pady=10) 

label2 = tk.Label(window, text="Click on a button to receive a message:", font=("Georgia", 14), bg="#F0F0F0", fg="#000000")
label2.pack(pady=10) 

# buttons

frame_bts = tk.Frame(window, bg="#F0F0F0")
frame_bts.pack(pady=15) 

sun_button = tk.Button(frame_bts, text="Sun", font=("Georgia", 12), bg="#E1B635", fg="#FFFFFF", width=10, command=sun_message)
sun_button.grid(row=0, column=0, padx=10)

moon_button = tk.Button(frame_bts, text="Moon", font=("Georgia", 12), bg="#A9A9A9", fg="#FFFFFF", width=10, command=moon_message)
moon_button.grid(row=0, column=1, padx=10) 

star_button = tk.Button(frame_bts, text="Star", font=("Georgia", 12), bg="#2A7CAF", fg="#FFFFFF", width=10, command=star_message)
star_button.grid(row=0, column=2, padx=10) 

window.mainloop() 