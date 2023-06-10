import tkinter as tk
from Client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Inventario de Tenis')
    root.iconbitmap('img/klipartz.com.ico')
    root.resizable(0,0)
    
    barra_menu(root)
    
    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()