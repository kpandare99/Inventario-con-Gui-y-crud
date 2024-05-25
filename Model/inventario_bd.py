from .conexion_bd import ConexionBD
from tkinter import messagebox

def crear_tabla():
    
    conexion = ConexionBD()
    
    #codigo sql para crea tabla en la base de datos
    sql ='''
    CREATE TABLE inventario (
        Id_inventario INTEGER,
        Nombre VARCHAR(100),
        Objeto VARCHAR(100),
        Cantidad VARCHAR(100),
        PRIMARY KEY(Id_inventario AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se Ha creado la Tabla de Base de Datos con exito¡'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'Ya la tablas exite '
        messagebox.showwarning(titulo,mensaje)
    
def borrar_tabla():
    
    conexion = ConexionBD()
    
    sql = 'DROP TABLE inventario'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'Se Ha Borrado la Tabla de Base de Datos con exito¡'
        messagebox.showinfo(titulo,mensaje)
    
    except:
        titulo = 'Borrar Registro'
        mensaje = '!No hay Tabla para Borrar¡'
        messagebox.showerror(titulo,mensaje)
        
        
class Datos:
    def __init__(self, Nombre, Objeto, Cantidad):
        self.id_inventario = None
        self.Nombre = Nombre
        self.Objeto = Objeto
        self.Cantidad = Cantidad
        
    def __str__(self):
        return f'Datos[{self.Nombre},{self.Objeto},{self.Cantidad}]'

def guardar(Datos):
    conexion = ConexionBD()
    
    sql = f"""INSERT INTO inventario (nombre, objeto, cantidad)
    VALUES('{Datos.Nombre}','{Datos.Objeto}','{Datos.Cantidad}')"""

    try:
       conexion.cursor.execute(sql)
       conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla inventario no esta creada en la base de datos¡'
        messagebox.showerror(titulo, mensaje)
        

def listar():
    conexion = ConexionBD()
    
    datos_inventario = []
    sql = 'SELECT * FROM inventario '
    
    try:
        conexion.cursor.execute(sql)
        datos_inventario = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Debes Crear La Tabla De la Base de Datos'
        messagebox.showwarning(titulo,mensaje)
        
    return datos_inventario
 
def editar(Datos, Id_inventario):

    conexion = ConexionBD()
    
    sql = f""" UPDATE inventario 
    SET nombre = '{Datos.Nombre}', 
    objeto = '{Datos.Objeto}', 
    cantidad = '{Datos.Cantidad}'
    WHERE Id_inventario = {Id_inventario}""" 
    
    try:
        conexion.cursor.execute(sql) 
        conexion.cerrar() 
        
    except:
        titulo = 'Edicion de Datos'
        mensaje = 'No se pudo editar el registro'
        messagebox.showerror(titulo, mensaje)

def eliminar (Id_inventario):
    conexion = ConexionBD()
    sql = f'DELETE FROM inventario WHERE Id_inventario = {Id_inventario}'
    
    try:
       conexion.cursor.execute(sql)
       conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar datos¡'
        messagebox.showerror(titulo, mensaje)
    
