import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Model.inventario_bd  import crear_tabla, borrar_tabla
from Model.inventario_bd import Datos, guardar, listar, editar, eliminar


def barra_menu(root): #definicion de variables para barra de menu de inicio
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear un Registro nuevo en Base de Datos', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar un Registro nuevo en Base de Datos', command=borrar_tabla)
    menu_inicio.add_command(label='Exit', command= root.destroy)
    
class Frame(tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root, width = 480, height = 320) #heredar clase padre par el constructor            
        self.root = root
        self.pack()
        self.config(bg = "white")

        self.id_inventario = None
        
        self.campos()
        self.deshabilitar_campos()
        self.tabla_datos()
        
    def campos(self):
        #label de cada campo 
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font = ('Arial', 13, 'bold' ))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_objeto = tk.Label(self, text = 'Objeto: ')
        self.label_objeto.config(font = ('Arial', 13, 'bold' ))
        self.label_objeto.grid(row = 2, column = 0, padx = 10, pady = 10 )

        self.label_cantidad = tk.Label(self, text = 'Cantidad: ')
        self.label_cantidad.config(font = ('Arial', 13, 'bold' ))
        self.label_cantidad.grid(row = 4, column = 0, padx = 10, pady = 10)

        #Entrada para cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width = 50, font=('Arial', 12) )
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.mi_objeto = tk.StringVar()
        self.entry_objeto = tk.Entry(self, textvariable=self.mi_objeto)
        self.entry_objeto.config(width = 50, font=('Arial', 12) )
        self.entry_objeto.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad)
        self.entry_cantidad.config(width = 50, font=('Arial', 12) )
        self.entry_cantidad.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        
        #botenes de acción
        
        #Boton para agrregar
        self.boton_agregar = tk.Button(self, text="Agregar", command = self.habilitar_campos)
        self.boton_agregar.config(width = 14, font=('Arial', 12, 'bold'),fg='white', bg ='#0BD4E1', cursor = 'hand2' , activebackground = 'yellow' )
        self.boton_agregar.grid(row = 0, column = 3, padx=5, pady=5)
        
        #Boton para guardar 
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width = 14, font=('Arial', 12, 'bold'),fg='white', bg ='green', cursor = 'hand2' , activebackground = 'blue' )
        self.boton_guardar.grid(row = 2, column = 3, padx=5, pady=5)
        
        #Boton para cancelar
        self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 14, font=('Arial', 12, 'bold'),fg='white', bg ='orange', cursor = 'hand2' , activebackground = 'grey' )
        self.boton_cancelar.grid(row = 4, column = 3, padx=5, pady=5)
        
        
    def habilitar_campos(self): #habilitar campos de entry
        
        self.mi_nombre.set('')#limpiar datos con la funcion
        self.mi_cantidad.set('')
        self.mi_objeto.set('')
        
        
        
        self.entry_nombre.config(state='normal')
        self.entry_objeto.config(state='normal')
        self.entry_cantidad.config(state='normal')
            
    
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self): #funcion para desabilitar campos entry
        self.id_inventario = None
        self.mi_nombre.set('')#limpiar datos con la funcion
        self.mi_cantidad.set('')
        self.mi_objeto.set('')
        
        
        
        self.entry_nombre.config(state='disable')
        self.entry_objeto.config(state='disable')
        self.entry_cantidad.config(state='disable')
            
    
        self.boton_guardar.config(state='disable')
        self.boton_cancelar.config(state='disable')     
       
    
    #funcion para boton guardar
    def guardar_datos(self):
        
       datos = Datos(
           self.mi_nombre.get(),
           self.mi_objeto.get(),
           self.mi_cantidad.get())
       
       if self.id_inventario == None:
           guardar(datos)
       else:
           editar(datos, self.Id_inventario)
        
       
       
       self.tabla_datos()
       
       
       self.deshabilitar_campos() #deshabilitar campos
    
    #diseño de tabal de datos
    def tabla_datos(self):
        #Parametros de la tabla
        self.datos_inventario = listar()
        self.datos_inventario.reverse()
        
        self.tabla = ttk.Treeview(self, columns= ('Nombre', 'Objeto', 'Cantidad' ))
        self.tabla.grid(row=6, column=0, columnspan = 5, sticky='nse' )
        
        #scrollbar para tabla
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=5, sticky='nse')
        self.tabla.config(yscrollcommand=self.scroll.set)
        
        #encabezado de la tabla 
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Objeto')
        self.tabla.heading('#3', text='Cantidad')
        
        #iterar datos de inventario 
        for p in self.datos_inventario:
            #valores de tabla
            self.tabla.insert('',0, text=p[0] , values= (p[1], p[2], p[3]))
        
        #Boton Editar 
        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(width = 14, font=('Arial', 12, 'bold'),fg='white', bg ='grey', cursor = 'hand2' , activebackground = 'green' )
        self.boton_editar.grid(row = 7, column = 0, padx=10, pady=10)
        
        #Boton para eliminar
        self.boton_elimminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.boton_elimminar.config(width = 14, font=('Arial', 12, 'bold'),fg='white', bg ='red', cursor = 'hand2' , activebackground = 'orange' )
        self.boton_elimminar.grid(row = 7, column = 3, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.Id_inventario = self.tabla.item(self.tabla.selection())['text']
            self.nombre = self.tabla.item(self.tabla.selection())['values'][0]
            self.objeto = self.tabla.item(self.tabla.selection())['values'][1]
            self.cantidad = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()
            
            
            self.entry_nombre.insert(0,self.nombre)
            self.entry_objeto.insert(0,self.objeto)
            self.entry_cantidad.insert(0,self.cantidad)
            
        except:
            titulo = 'Edición de Datos'
            mensaje = 'No ha selecionado Ningun Dato¡'
            messagebox.showerror(titulo,mensaje)
            
            
    def eliminar_datos(self):
        
        try:
            self.Id_inventario = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.Id_inventario)
                
            self.tabla_datos()
            self.id_inventario = None
        except:
            titulo = 'Eliminar Datos'
            mensaje = 'No ha selecionado Ningun Dato¡'
            messagebox.showerror(titulo,mensaje)