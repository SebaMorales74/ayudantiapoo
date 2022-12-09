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

        self.caja_password = Entry(show='*',width=30)
        self.caja_password.place(x=250, y=150)

        self.boton_ingresar = Button(text="Ingresar", command=lambda: self.validarUsuario(parent))
        self.boton_ingresar.place(x=250, y=200)

        self.widgets = [self.etiqueta_titulo, self.caja_usuario, self.caja_password, self.boton_ingresar]
    
    def validarUsuario(self,parent):
        usuario = self.caja_usuario
        password = self.caja_password
        resultado = Oracle.query(f"SELECT * FROM MAMC_USUARIOS WHERE username='{usuario.get()}' AND contraseña='{password.get()}'")
        if resultado == False: return print("Error al validar usuario")
        for i in resultado:
            if i[3] != 'admin':
                self.limpiar()
                MenuUsuario(parent)
                return print("Bienvenido usuario")

            print("Bienvenido administrador")
            self.limpiar()
            MenuAdmin(parent)
    
    def limpiar(self):
        for widget in self.widgets:
            widget.destroy()

class MenuAdmin(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Menu Administrador")
        self.etiqueta_opciones = Label(text="Opciones", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_opciones.place(x=250, y=50)

        self.boton_agregarUsuario = Button(text="Agregar Usuario", command=self.agregarUsuario)
        self.boton_agregarUsuario.place(x=250, y=150)

        self.boton_listarUsuarios = Button(text="Listar Usuarios", command=self.listarUsuarios)
        self.boton_listarUsuarios.place(x=250, y=200)

        self.boton_agregarProducto = Button(text="Agregar Productos", command=self.agregarProducto)
        self.boton_agregarProducto.place(x=250, y=250)

        self.boton_listarProductos = Button(text="Listar Productos", command=self.listarProductos)
        self.boton_listarProductos.place(x=250, y=300)

    def listarProductos(self):
        self.listarProductos = tk.Toplevel()
        self.listarProductos.title("Visualizacion de productos")
        self.listarProductos.config(width=600, height=600, bg="white")
        self.tabla = ttk.Treeview(self.listarProductos, columns=("Producto", "Precio"))
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Producto")
        self.tabla.heading("#2", text="Precio")
        self.tabla.place(x=300, y=200, anchor="center")

        self.eliminarProducto = Button(self.listarProductos, text="Eliminar Producto", command=self.eliminarProducto)
        self.eliminarProducto.place(x=300, y=400, anchor="center")

        resultado = Oracle.query("SELECT * FROM MAMC_PRODUCTOS")

        if resultado == False: return print("Error al listar productos")

    def eliminarProducto(self):
        idProducto = self.tabla.item(self.tabla.selection())['text']
        self.tabla.delete(self.tabla.selection()[0])
        resultado = Oracle.query(f"DELETE FROM MAMC_PRODUCTOS WHERE id_producto={idProducto}")
        if resultado == False: return print("Error al eliminar producto")
        print("Producto eliminado")
        
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

        self.boton_submit = Button(self.agregarProducto, text="Agregar Producto", command=lambda: Oracle.query(f"INSERT INTO MAMC_PRODUCTOS (nombre,precio) VALUES ('{self.caja_producto.get()}', '{self.caja_precio.get()}')") )
        self.boton_submit.place( x=250, y=250)
    


    def listarUsuarios(self):
        self.listarUsuarios = tk.Toplevel()
        self.listarUsuarios.title("Visualizacion de usuarios")
        self.listarUsuarios.config(width=800, height=600, bg="white")
        self.tabla = ttk.Treeview(self.listarUsuarios, columns=("Username", "Contraseña", "Rol"))
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Username")
        self.tabla.heading("#2", text="Contraseña")
        self.tabla.heading("#3", text="Rol")
        self.tabla.place(x=400, y=200, anchor="center")

        self.boton_eliminarUsuario = Button(self.listarUsuarios, text="Eliminar Usuario", command=self.eliminarUsuario)
        self.boton_eliminarUsuario.place(x=400, y=500, anchor="center")

        resultado = Oracle.query("SELECT * FROM MAMC_USUARIOS WHERE idUsuario>1")

        if resultado == False: return print("Error al listar usuarios")

        for i in resultado:
            self.tabla.insert("", "end", text=i[0], values=(i[1], i[2], i[3]))
    def eliminarUsuario(self):
        idUsuario = self.tabla.item(self.tabla.selection())['text']
        self.tabla.delete(self.tabla.selection()[0])
        resultado = Oracle.query(f"DELETE FROM MAMC_USUARIOS WHERE idUsuario={idUsuario}")
        if resultado == False: return print("Error al eliminar usuario")
        print("Usuario eliminado")



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

        self.etiqueta_rol = Label(self.agregarUsuario, text="Ingrese Rol", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_rol.place( x=250, y=250 )

        self.caja_rol = Entry(self.agregarUsuario, width=30 )
        self.caja_rol.place( x=250, y=300 )

        self.boton_submit = Button(self.agregarUsuario, text="Agregar Usuario", command=self.subirUsuario )
        self.boton_submit.place( x=250, y=350 )
    def subirUsuario(self):
        resultado = Oracle.query(f"INSERT INTO MAMC_USUARIOS (username,contraseña,rol) VALUES ('{self.caja_username.get()}', '{self.caja_password.get()}', '{self.caja_rol.get()}')")
        
        if resultado == False: 
            self.agregarUsuario.destroy() 
            return print("Error al agregar usuario")
        
        print("Usuario agregado")
        self.agregarUsuario.destroy() 

class MenuUsuario(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Menu de Usuario")
        self.etiqueta_menu = Label(self, text="Menu de Usuario", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_menu.place( x=250, y=50 )

        self.boton_realizarVenta = Button(text="Realizar venta", command=self.realizarVenta)
        self.boton_realizarVenta.place(x=250, y=100)

        self.boton_listarProductos = Button(text="Listar productos", command=self.listarProductos)
        self.boton_listarProductos.place(x=250, y=150)

    def listarProductos(self):
        self.listarProductos = tk.Toplevel()
        self.listarProductos.title("Visualizacion de productos")
        self.listarProductos.config(width=600, height=600, bg="white")
        self.tabla = ttk.Treeview(self.listarProductos, columns=("Producto", "Precio"))
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Producto")
        self.tabla.heading("#2", text="Precio")
        self.tabla.place(x=300, y=200, anchor="center")

        self.caja_buscarProducto = Entry(self.listarProductos, width=30 )
        self.caja_buscarProducto.place( x=300, y=400, anchor="center" )
        self.boton_buscarProducto = Button(self.listarProductos, text="Buscar Producto", command=self.buscarProducto)
        self.boton_buscarProducto.place( x=300, y=450, anchor="center" )

        resultado = Oracle.query("SELECT * FROM MAMC_PRODUCTOS")
        if resultado == False: return print("Error al listar productos")
        for i in resultado:
            self.tabla.insert("", "end", text=i[0], values=(i[1], i[2]))

    def buscarProducto(self):
        resultado = Oracle.query(f"SELECT * FROM MAMC_PRODUCTOS WHERE nombre LIKE '%{self.caja_buscarProducto.get()}%'")
        if resultado == False: return print("Error al buscar productos")
        self.tabla.delete(*self.tabla.get_children())
        for i in resultado:
            self.tabla.insert("", "end", text=i[0], values=(i[1], i[2]))
    
    def realizarVenta(self):
        self.realizarVenta = tk.Toplevel()
        self.realizarVenta.title("Realizar venta")
        self.realizarVenta.config(width=600, height=600, bg="white")

        self.etiqueta_producto = Label(self.realizarVenta, text="Ingrese Producto", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_producto.place( x=250, y=50 )

        self.caja_producto = Entry(self.realizarVenta, width=30 )
        self.caja_producto.place( x=250, y=100 )

        self.etiqueta_cantidad = Label(self.realizarVenta, text="Ingrese Cantidad", bg="white", fg="black", font=("Arial", 20))
        self.etiqueta_cantidad.place( x=250, y=150 )

        self.caja_cantidad = Entry(self.realizarVenta, width=30 )
        self.caja_cantidad.place( x=250, y=200 )

        self.boton_submit = Button(self.realizarVenta, text="Realizar venta", command=self.realizarVenta )
        self.boton_submit.place( x=250, y=350 )

app = Login(ventana)
ventana.mainloop()