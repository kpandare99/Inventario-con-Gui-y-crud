import tkinter as tk
from Client.gui_app import Frame , barra_menu


def main ():
    root = tk.Tk()
    root.title("Inventario Aula") #nombre de titulo de ventana 
    #root.wm_iconbitmap(carpetalogo/nombrelogo)
    root.resizable(0,0) # modifica o bloquea el tamaño de interfaz de usuario
    
    barra_menu(root)

    #frame = tk.Frame(root) #contenedor de los elementos
    #frame.pack() #empaquetado, tamaño de la ventana al tamaño de frame
    #frame.config(width = 480, height = 320, bg = "blue" ) #configuracion de ventana
   
    app = Frame(root = root)
    app.root.mainloop()
    

if __name__ == "__main__":  
    main()