from .conexion_db import ConexionDB
from tkinter import messagebox
def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE inventario(
        codigo_teni INTEGER, 
        marca VARCHAR(20),
        cantidad VARCHAR(100),
        precio INTEGER,
        talla INTEGER,
        PRIMARY KEY(codigo_teni AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)    
    
    
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = 'DROP TABLE inventario'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'la tabla de la base de datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)
    except:     
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje) 
        
class Inventario:
    def __init__(self, marca, cantidad, precio, talla):
       self.codigo_teni = None
       self.marca = marca
       self.cantidad = cantidad
       self.precio = precio 
       self.talla = talla 
    
    def __str__(self):
        return f'Inventario[{self.marca}, {self.cantidad}, {self.precio}, {self.talla}]'
    
def guardar(inventario):
    conexion = ConexionDB()
    
    sql = f"""INSERT INTO inventario (marca, cantidad, precio, talla)
    VALUES('{inventario.marca}','{inventario.cantidad}','{inventario.precio}','{inventario.talla}')"""
    
    try:
        conexion.cursor.execute(sql)  
        conexion.cerrar()
    except:
        titulo = 'Conexion al regitro'
        mensaje = 'la tabla inventario no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)    

def listar():
    conexion = ConexionDB()
    
    lista_inventario = []
    sql = 'SELECT * FROM inventario'     
    
    try:
        conexion.cursor.execute(sql)
        lista_inventario = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Crear la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)                
    
    return lista_inventario    

def modificar(inventario, codigo_teni):
    conexion = ConexionDB()
    
    sql = f"""UPDATE inventario
    SET marca = '{inventario.marca}', cantidad = '{inventario.cantidad}', precio = '{inventario.precio}', talla = '{inventario.talla}'
    WHERE codigo_teni = {codigo_teni}"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
        
    except:
        titulo = 'Modificacion de datos'
        mensaje = 'No se a podido modificar este registro'
        messagebox.showerror(titulo, mensaje)   
    
def eliminar(codigo_teni):
    conexion = ConexionDB() 
    sql = f'DELETE FROM inventario WHERE codigo_teni = {codigo_teni}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
        
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se a podido eliminar este registro'
        messagebox.showerror(titulo, mensaje)  



def buscar():
    conexion = ConexionDB() 
    sql = f"""DELETE FROM inventario WHERE talla = 39"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
        
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se a podido eliminar este registro'
        messagebox.showerror(titulo, mensaje)  