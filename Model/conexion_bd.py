import sqlite3 #importar datos de sqlite3

class ConexionBD:
    
    def __init__(self):
        self.base_datos = 'Database/Inventario.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor= self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
        

