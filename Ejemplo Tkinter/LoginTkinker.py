import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
tamaño = width, height = 300, 300
ventana.title("Ejemplo con POO")
ventana.config(width=width, height=height)

class Login(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = ttk.Label(text="Login", style="TLabel")
        self.titulo.place(x=width/2, y=100, anchor="center")

        self.username = ttk.Entry()
        self.username.place(x=width/2, y=130, anchor="center")

        self.password = ttk.Entry(show="*")
        self.password.place(x=width/2, y=160, anchor="center")
    
        self.ingresar = ttk.Button(text="Ingresar", command=lambda: self.submit(parent))
        self.ingresar.place(x=width/2, y=height/2 + 60, anchor="center")

    def submit(self, parent):
        self.result = {"username": "Sebastian", "password":"hola123"}

        self.form_username = self.username.get()
        self.form_password = self.password.get()
        print(f"Nombre de usuario: {self.form_username} ; Contraseña: {self.form_password}")

        if self.form_username != self.result["username"]: 
            return print("Usuario inexistente")
        if self.form_password != self.result["password"]: 
            return print("Contraseña incorrecta")
        
        self.titulo.destroy()
        self.username.destroy()
        self.password.destroy()
        self.ingresar.destroy()

        Productos(parent)

class Productos(ttk.Frame):
    def __init__(self, parent):

        self.productos = []

        super().__init__(parent)
        self.label_titulo = ttk.Label(text="Productos", style="TLabel")
        self.label_titulo.place(x=width/2, y=80, anchor="center")

        self.input_producto = ttk.Entry()
        self.input_producto.place(x=width/2, y=110, anchor="center")

        self.input_precio = ttk.Entry()
        self.input_precio.place(x=width/2, y=140, anchor="center")

        self.button_agregar = ttk.Button(text="Agregar", command=self.agregarProducto)
        self.button_agregar.place(x=width/2, y=height/2 + 60, anchor="center")

        self.button_print = ttk.Button(text="Imprimir productos", command=self.imprimirProductos)
        self.button_print.place(x=width/2, y=height/2 + 90, anchor="center")

        self.button_editar = ttk.Button(text="Editar productos", command=self.editarProductos)
        self.button_editar.place(x=width/2, y=height/2 + 120, anchor="center")
       
    def agregarProducto(self):
        self.producto = self.input_producto.get()
        self.precio = self.input_precio.get()
        print(f"Producto: {self.producto} ; Precio: {self.precio}")
        self.productos.append({"id":len(self.productos),"producto": self.producto, "precio": self.precio})
        self.input_producto.delete(0, "end")
        self.input_precio.delete(0, "end")

        try:
            for producto in self.productos:
                self.tabla.insert("", "end", text=producto["id"], values=(producto["producto"], producto["precio"]))
        except:
            pass


    def imprimirProductos(self):
        print(self.productos)

    def editarProductos(self):
        self.editarProductos = tk.Toplevel()
        self.editarProductos.title("Editar productos")
        self.editarProductos.config(width=600, height=600)

        self.tabla = ttk.Treeview(self.editarProductos, columns=("Producto", "Precio"))
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Producto")
        self.tabla.heading("#2", text="Precio")
        self.tabla.place(x=300, y=200, anchor="center")

        for producto in self.productos:
            self.tabla.insert("", "end", text=producto["id"], values=(producto["producto"], producto["precio"]))

        self.button_mostrarSeleccionado = ttk.Button(self.editarProductos, text="Eliminar producto seleccionado", command=lambda: self.eliminarProducto(self.itemSeleccionado()))
        self.button_mostrarSeleccionado.place(x=300, y=400, anchor="center")

    def eliminarProducto(self,item):
        del self.productos[item["text"]]
        self.tabla.delete(self.tabla.selection()[0])
        print(self.productos)

    def itemSeleccionado(self):
        self.item = self.tabla.selection()[0]
        self.item = self.tabla.item(self.item)
        return self.item


app = Login(ventana)
ventana.mainloop()