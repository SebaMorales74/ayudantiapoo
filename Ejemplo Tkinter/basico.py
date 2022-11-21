import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
tamaño = width, height = 300, 300
ventana.title("Ejemplo basico de tkiner")
ventana.config(width=width, height=height)

etiqueta_holaMundo = ttk.Label(text="Hola mundo", style="TLabel")
etiqueta_holaMundo.place(x=width/2, y=height/2 - 20, anchor="center")

input_nombre = ttk.Entry()
input_nombre.place(x=width/2, y=height/2 + 20, anchor="center")

def saludar():
    print("Hola", input_nombre.get())

button_saludar = ttk.Button(text="Saludar", command=lambda: print("Hola", input_nombre.get()))
button_saludar.place(x=width/2, y=height/2 + 60, anchor="center")

ventana.mainloop()