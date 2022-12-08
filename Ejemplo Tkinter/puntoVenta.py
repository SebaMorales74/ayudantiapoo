import os
import cx_Oracle
from tkinter import *
import tkinter as tk
from tkinter import ttk

ventana = Tk()
ventana.geometry("700x500")
ventana.configure(bg="white")

class Oracle:
    os.environ["TNS_ADMIN"]="\pythonsql\wallet"
    conexion = cx_Oracle.connect("admin", ".Inacap2022.", "db20220530152721_high")
    cursor = conexion.cursor()

    def query(sql):
        try:
            Oracle.cursor.execute(sql)
            Oracle.conexion.commit()
            return Oracle.cursor
        except Exception as e:
            print(e)
            return False

class Login(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        parent.title("Login")

        self.etiqueta_titulo = Label(text="Ingrese Usuario", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_titulo.place(x=250, y=50)

        self.caja_usuario = Entry(width=30)
        self.caja_usuario.place(x=250, y=100)

        self.caja_password = Entry(width=30)
        self.caja_password.place(x=250, y=150)

        self.boton_ingresar = Button(text="Ingresar", command=lambda: self.validarUsuario(parent))
        self.boton_ingresar.place(x=250, y=200)

        self.widgets = [self.etiqueta_titulo, self.caja_usuario, self.caja_password, self.boton_ingresar]
    
    def validarUsuario(self,parent):
        usuario = self.caja_usuario
        password = self.caja_password
        resultado = Oracle.query(f"SELECT * FROM usuarios WHERE username='{usuario.get()}' AND clave='{password.get()}'")

        for i in resultado:
            if i[0] != usuario.get() and i[1] != password.get(): return print("Usuario no existe")
            elif "admin" == usuario.get() or usuario.get() == "javier":
                print("Bienvenido administrador")
                self.limpiar()
                MenuAdmin(parent)
            else:
                print("Bienvenido usuario")
                self.limpiar()
                MenuUsuario(parent)
    
    def limpiar(self):
        for widget in self.widgets:
            widget.destroy()

class MenuAdmin(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.etiqueta_opciones = Label(text="Opciones", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_opciones.place(x=250, y=50)

        self.boton_agregarUsuario = Button(text="Agregar Usuario", command=self.agregarUsuario)
        self.boton_agregarUsuario.place(x=250, y=150)

        self.boton_agregarProducto = Button(text="Agregar Productos", command=self.agregarProducto)
        self.boton_agregarProducto.place(x=250, y=200)

        self.boton_listarProductos = Button(text="Listar Productos", command=self.listarProductos)
        self.boton_listarProductos.place(x=250, y=250)

    def listarProductos(self):
        self.listarProductos = tk.Toplevel()
        self.listarProductos.title("Visualizacion de productos")
        self.listarProductos.config(width=600, height=600, bg="white")
        self.tabla = ttk.Treeview(self.listarProductos, columns=("Producto", "Precio"))
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Producto")
        self.tabla.heading("#2", text="Precio")
        self.tabla.place(x=300, y=200, anchor="center")

        resultado = Oracle.query("SELECT * FROM producto")

        if resultado == False: return print("Error al listar productos")

        for i in resultado:
            self.tabla.insert("", "end", text=i[0], values=(i[1], i[2]))


    def agregarUsuario(self):
        self.agregarUsuario = tk.Toplevel()
        self.agregarUsuario.title("Visualizacion de productos")
        self.agregarUsuario.config(width=600, height=600, bg="white")

        self.etiqueta_username = Label(self.agregarUsuario, text="Ingrese Usuario", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_username.place( x=250, y=50 )

        self.caja_username = Entry(self.agregarUsuario, width=30 )
        self.caja_username.place( x=250, y=100 )

        self.etiqueta_password = Label(self.agregarUsuario, text="Ingrese Contraseña", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_password.place( x=250, y=150 )

        self.caja_password = Entry(self.agregarUsuario, width=30 )
        self.caja_password.place( x=250, y=200 )

        self.boton_submit = Button(self.agregarUsuario, text="Agregar Usuario", command=lambda: Oracle.query(f"INSERT INTO usuarios VALUES ('{self.caja_username.get()}', '{self.caja_password.get()}')") )
        self.boton_submit.place( x=250, y=250 )
    
    def agregarProducto(self):
        self.agregarProducto = tk.Toplevel()
        self.agregarProducto.title("Agregar Producto")
        self.agregarProducto.config(width=600, height=600, bg="white")

        self.etiqueta_producto = Label(self.agregarProducto, text="Ingrese Producto", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_producto.place( x=250, y=50)

        self.caja_producto = Entry(self.agregarProducto, width=30)
        self.caja_producto.place( x=250, y=100)

        self.etiqueta_precio = Label(self.agregarProducto, text="Ingrese Precio", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_precio.place( x=250, y=150)

        self.caja_precio = Entry(self.agregarProducto, width=30)
        self.caja_precio.place( x=250, y=200)

        self.boton_submit = Button(self.agregarProducto, text="Agregar Producto", command=lambda: Oracle.query(f"INSERT INTO producto (producto,precio) VALUES ('{self.caja_producto.get()}', '{self.caja_precio.get()}')") )
        self.boton_submit.place( x=250, y=250)

class MenuUsuario(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

app = Login(ventana)
ventana.mainloop()