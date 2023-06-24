import tkinter as tk
from tkinter import ttk, messagebox
from model.inventario_dao import crear_tabla, borrar_tabla
from model.inventario_dao import Inventario, guardar, listar, modificar, eliminar,buscar
 



def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height= 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label ='Inicio', menu = menu_inicio)
    
    
    menu_inicio.add_command(label = 'Crear Registro en BD', command=crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Registro en BD', command=borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command= root.destroy)
    
    barra_menu.add_cascade(label ='Consultas')
    barra_menu.add_cascade(label ='Configuración')
    barra_menu.add_cascade(label ='Ayuda')
    
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320 )
        self.root = root
        self.pack()
        #self.config( bg = 'blue')
        self.codigo_teni = None
        
        self.campos_de_inventario()
        self.desabilitar_campos()
        self.tabla_tenis()
        
    def campos_de_inventario(self):
        # labels de cada campo
        self.label_marca = tk.Label(self, text = 'Marca: ')
        self.label_marca.config(font = ('Arial', 12, 'bold'))
        self.label_marca.grid(row = 0, column = 0, padx = 8, pady =8)
                
        self.label_cantidad = tk.Label(self, text = 'Cantidad: ')
        self.label_cantidad.config(font = ('Arial', 12, 'bold'))
        self.label_cantidad.grid(row = 1, column = 0, padx = 8, pady =8)
        
        self.label_precio = tk.Label(self, text = 'Precio: ')
        self.label_precio.config(font = ('Arial', 12, 'bold'))
        self.label_precio.grid(row = 2, column = 0, padx = 8, pady =8)
        
        self.label_talla = tk.Label(self, text = 'Talla: ')
        self.label_talla.config(font = ('Arial', 12, 'bold'))
        self.label_talla.grid(row = 3, column = 0, padx = 8, pady =8)
        
        #self.label_marca1 = tk.Label(self, text = 'Buscar Marca: ')
        #self.label_marca1.config(font = ('Arial', 10, 'bold'))
        #self.label_marca1.grid(row = 0, column = 3, padx = 8, pady =8)

        #self.label_precio1 = tk.Label(self, text = 'Buscar Precio: ')
        #self.label_precio1.config(font = ('Arial', 10, 'bold'))
        #self.label_precio1.grid(row = 1, column = 3, padx = 8, pady =8)

        #self.label_talla1= tk.Label(self, text = 'Buscar Talla: ')
        #self.label_talla1.config(font = ('Arial', 10, 'bold'))
        #self.label_talla1.grid(row = 2, column = 3, padx = 8, pady =8)

        

        #Entry de los campos de entrada
        self.mi_marca = tk.StringVar()
        self.entry_marca = tk.Entry(self, textvariable= self.mi_marca)
        self.entry_marca.config(width= 40, font = ('Arial', 12))
        self.entry_marca.grid(row = 0, column = 1, padx = 8, pady =8, columnspan = 2)
        
        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable= self.mi_cantidad)
        self.entry_cantidad.config(width= 40, font = ('Arial', 12))
        self.entry_cantidad.grid(row = 1, column = 1, padx = 8, pady =8, columnspan = 2)
        
        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable= self.mi_precio)
        self.entry_precio.config(width= 40, font = ('Arial', 12))
        self.entry_precio.grid(row = 2, column = 1, padx = 8, pady =8, columnspan = 2)
        
        self.mi_talla = tk.StringVar()
        self.entry_talla = tk.Entry(self, textvariable= self.mi_talla)
        self.entry_talla.config(width= 40, font = ('Arial', 12))
        self.entry_talla.grid(row = 3, column = 1, padx = 8, pady =8, columnspan = 2)

        
    
        
        #Botones
        #boton nuevo
        self. boton_nuevo = tk.Button(self, text= "Ingresar Producto", command= self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#015E87', 
                                cursor = 'hand2', activebackground='#1394CD')
        self.boton_nuevo.grid(row = 4, column = 0, padx = 8, pady =8)
        
        #boton Guardar
        self. boton_guardar = tk.Button(self, text= "Guardar", command= self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#015E87', 
                                cursor = 'hand2', activebackground='#1394CD')
        self.boton_guardar.grid(row = 4, column = 1, padx = 8, pady =8)
        
        #boton cancelar
        self. boton_cancelar = tk.Button(self, text= "Cancelar", command= self.desabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#800101', 
                                cursor = 'hand2', activebackground='#C32222')
        self.boton_cancelar.grid(row = 4, column = 2, padx = 8, pady =8)
        
    
        
    def habilitar_campos(self):
        self.mi_marca.set('')
        self.mi_cantidad.set('')
        self.mi_precio.set('')
        self.mi_talla.set('')
        

        self.entry_marca.config(state='normal')
        self.entry_cantidad.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_talla.config(state='normal')
        
        
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')    
    
    def desabilitar_campos(self):
        self.codigo_teni = None
        self.mi_marca.set('')
        self.mi_cantidad.set('')
        self.mi_precio.set('')
        self.mi_talla.set('')
        
                        
        self.entry_marca.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_talla.config(state='disabled')
        

        self.boton_guardar.config(state='disable')
        self.boton_cancelar.config(state='disable')

    
   

    

    
    def guardar_datos(self):
        
        inventario = Inventario(
            self.mi_marca.get(),
            self.mi_cantidad.get(),
            self.mi_precio.get(),
            self.mi_talla.get(),
        )
        
        if self.codigo_teni == None:
            guardar(inventario)
        else:
            modificar(inventario, self.codigo_teni)
        
        self.tabla_tenis()
        
        self.desabilitar_campos()

    

        
    def tabla_tenis(self):
        #recuperar la lista de inventario
        self.lista_inventario = listar()
        self.lista_inventario.reverse()
        
        
        self.tabla = ttk.Treeview(self, 
        column =('Marca', 'Cantidad', 'Precio', 'Talla'))  
        self.tabla.grid(row= 5, column = 0, columnspan= 5, sticky = 'nse')
        
        # Scrollbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar( self, 
        orient = 'vertical', command = self.tabla.yview)
        self.scroll.grid(row = 5, column = 5, sticky = 'nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)
        
        
        self.tabla.heading('#0', text = 'CODIGO') 
        self.tabla.heading('#1', text = 'MARCA')
        self.tabla.heading('#2', text = 'CANTIDAD')   
        self.tabla.heading('#3', text = 'PRECIO') 
        self.tabla.heading('#4', text = 'TALLA')         

        #iterar la lista de inventario
        for i in self.lista_inventario:
            self.tabla.insert('', 0 , text=i[0], 
            values=(i[1], i[2], i[3], i[4]))

        
    
        
        
        #boton modificar
        self. boton_modificar = tk.Button(self, text= "Modificar", command = self.modificar_datos)
        self.boton_modificar.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#015E87', 
                                cursor = 'hand2', activebackground='#1394CD')
        self.boton_modificar.grid(row = 6, column = 0, padx = 8, pady =8)
        
        #boton buscar
        #self. boton_buscar = tk.Button(self, text= "Buscar", command= self.buscar)
        #self.boton_buscar.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#015E87', 
        #                      cursor = 'hand2', activebackground='#1394CD')
        #self.boton_buscar.grid(row = 6, column = 1, padx = 8, pady =8)
        
        #boton eliminar
        self. boton_eliminar = tk.Button(self, text= "Eliminar", command = self.eliminar_datos)
        self.boton_eliminar.config(width = 20, font = ('Arial', 12, 'bold'), fg ='#FFFFFF', bg ='#800101', 
                                cursor = 'hand2', activebackground='#C32222')
        self.boton_eliminar.grid(row = 6, column = 2, padx = 8, pady =8)

    
        
    def modificar_datos(self):
        
        try:
            self.codigo_teni = self.tabla.item(self.tabla.selection())['text']
            self.marca_teni = self.tabla.item(
                self.tabla.selection())['values'][0] 
            self.cantidad_teni = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.precio_teni = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.talla_teni = self.tabla.item(
                self.tabla.selection())['values'][3] 
            
            self.habilitar_campos()  
            
            self.entry_marca.insert(0, self.marca_teni)
            self.entry_cantidad.insert(0, self.cantidad_teni)
            self.entry_precio.insert(0, self.precio_teni)
            self.entry_talla.insert(0, self.talla_teni)

            
             
        except:
            titulo = 'Modificación de datos' 
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
            
   
       





    def eliminar_datos(self):
        try:
             self.codigo_teni = self.tabla.item(self.tabla.selection())['text']
             eliminar(self.codigo_teni)
             
             self.tabla_tenis()
             self.codigo_teni = None
        except:
          
            titulo = 'Eliminar un Registro'
            mensaje = 'No ha selecionado nigun registro'
            messagebox.showerror(titulo, mensaje)
            
    def buscar(self):
        try:
            self.habilitar_campos1()
             
            self.tabla_tenis()
            self.codigo_teni = None
        except:
          
            titulo = 'Eliminar un Registro'
            mensaje = 'No ha selecionado nigun registro'
            messagebox.showerror(titulo, mensaje)
    
                    