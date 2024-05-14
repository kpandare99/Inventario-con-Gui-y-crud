import tkinter as tk

def barra_menu(root): #definicion de variables para barra de menu de inicio
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear un Reguistro nuevo en Base de Datos')
    menu_inicio.add_command(label='Eliminar un Reguistro nuevo en Base de Datos')
    menu_inicio.add_command(label='Exit', command= root.destroy)

    barra_menu.add_cascade(label='Consulta')
    barra_menu.add_cascade(label='Help')


class Frame(tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root, width = 480, height = 320) #heredar clase padre par el constructor            
        self.root = root
        self.pack()
        self.config(bg = "blue")
