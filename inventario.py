import tkinter as tk
from Client.gui_app import Frame , barra_menu 


def main():
    root = tk.Tk()
    root.title("Inventario Aula") #nombre de titulo de ventana 
    root.iconbitmap('img/ing.ico')#cambiar icono de programa
    root.resizable(0,0) # modifica o bloquea el tamaño de interfaz de usuario
    
    barra_menu(root) #llama a la funcion de la barra menu 



    app = Frame(root = root)
    
    app.root.mainloop()
    

if __name__ == "__main__":  
    main() 