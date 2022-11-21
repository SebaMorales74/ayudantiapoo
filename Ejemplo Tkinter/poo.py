import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
tamaño = width, height = 300, 300
ventana.title("Ejemplo con POO")
ventana.config(width=width, height=height)

class Aplicacion(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.etiqueta_holaMundo = ttk.Label(text="Hola mundo", style="TLabel")
        self.etiqueta_holaMundo.place(x=width/2, y=height/2 - 20, anchor="center")

        self.input_nombre = ttk.Entry()
        self.input_nombre.place(x=width/2, y=height/2 + 20, anchor="center")
    
        self.button_saludar = ttk.Button(text="Saludar", command=self.saludar)
        self.button_saludar.place(x=width/2, y=height/2 + 60, anchor="center")
        
    def saludar(self):
        print("Hola", self.input_nombre.get())


app = Aplicacion(ventana)
ventana.mainloop()