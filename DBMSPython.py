from tkinter import *
from tkinter import messagebox
import pymysql

# Conector al servidor de la base de datos.

miConexion = pymysql.connect( host='tu_host', user='tu_usuario', passwd='tu_contraseña', db='tu_bd' )

# Ventana madre 

ventana = Tk()
ventana.geometry("400x350")
ventana.title("Administrador de base de datos")
miframe = Frame(ventana, width=1200, height=600)
miframe.pack()

#funciones

def crearBD():
    try:
        cursor = miConexion.cursor()
        cursor.execute("CREATE TABLE datosusuarios (id INT PRIMARY KEY AUTO_INCREMENT, nombre varchar(20) not null, password varchar (20) not null, apellido varchar(20) not null, direccion varchar(50) not null, comentario varchar(100))")
        messagebox.showinfo("Base de datos","La base de datos fue creada con exito.")
    except:
        messagebox.showinfo("Base de datos","La base de datos ya ha sido creada.")

def create():
    text1 = nombre.get()
    text2 = passw.get()
    text3 = apellido.get()
    text4 = direccion.get()
    text5 = comentario.get("1.0",'end-1c')

    lista=[(text1,text2,text3,text4,text5)]
    
    if len(nombre.get()) > 3 and nombre.get() and len(apellido.get()) > 4 and apellido.get():
        try:
            order = "INSERT INTO datosusuarios (id, nombre, password, apellido, direccion, comentario) VALUES (NULL,%s,%s,%s,%s,%s)"
            cursor = miConexion.cursor()
            cursor.executemany(order, lista)
            miConexion.commit()
            messagebox.showinfo("Crear lista","La creacion del registro ha sido exitosa.")
            id.delete(0, END)
            nombre.delete(0, END)
            apellido.delete(0, END)
            direccion.delete(0, END)
            passw.delete(0, END)
            comentario.delete("1.0",'end-1c')
        except:
            messagebox.showerror("Completar campos","Debe al menos tener un nombre.")
    else:
        messagebox.showerror("Completar campos","Complete los campos de nombre y apellido como corresponde.")

def read():
    cursor = miConexion.cursor()
    cursor.execute("SELECT * FROM datosusuarios")
    for i in cursor.fetchall():
        print(i)

def update():
    datos=[nombre.get(),
    passw.get(),
    apellido.get(),
    direccion.get(),
    comentario.get("1.0",'end-1c')]

    if len(nombre.get()) > 2 and nombre.get() and len(apellido.get()) > 3 and apellido.get():
        cursor = miConexion.cursor()
        cursor.execute("UPDATE datosusuarios SET nombre=%s,password=%s, apellido=%s, direccion=%s, comentario=%s WHERE id = " + id.get(),(datos))
        messagebox.showinfo("Actualizacion de registro","Los campos correspondiente al ID han sido actualizados con exito.")
        miConexion.commit()
    else:
        messagebox.showerror("Completar campos","Complete los campos de nombre y apellido como corresponde.")

def Delete():
    nombre.get()
    passw.get()
    apellido.get()
    direccion.get()
    comentario.get("1.0",'end-1c')

    cursor = miConexion.cursor()
    cursor.execute("DELETE FROM datosusuarios WHERE id =" + id.get())
    miConexion.commit()
    messagebox.showinfo("Borrar registro","Los campos correspondientes la ID han sido eliminados con exito.")

def Salir():
    valor=messagebox.askyesno("Cerrar programa","¿Desea salir del programa?")
    if valor:
        ventana.destroy()

def Ayuda():
    messagebox.showinfo("Licencia","Info aun no autorizada")

def sobreNosotros():
    messagebox.showinfo("Acerca de Nosotros","Somos una empresa encargada a ofrecer ayuda al desarrollo de nuevas tecnologias y adecuado modo de uso de estas")

def Borrar():
    id.delete(0, END)
    nombre.delete(0, END)
    apellido.delete(0, END)
    direccion.delete(0, END)
    passw.delete(0, END)
    comentario.delete("1.0",'end-1c')

# barra de menu

barraMenu = Menu(miframe)
ventana.config(menu=barraMenu, width=300, height=300)

opcionBBDD = Menu(barraMenu, tearoff=0)
opcionBBDD.add_command(label="Conectar", command=crearBD)
opcionBBDD.add_command(label= 'Salir', command=Salir)

opcionBorrar = Menu(barraMenu, tearoff=0)
opcionBorrar.add_command(label='Borrar campos', command=Borrar)

opcionCRUD = Menu(barraMenu, tearoff=0)
opcionCRUD.add_command(label="Crear", command= create)
opcionCRUD.add_command(label= 'Leer', command= read)
opcionCRUD.add_command(label="Actualizar", command=update)
opcionCRUD.add_command(label= 'Borrar', command=Delete)

opcionAyuda = Menu(barraMenu, tearoff=0)
opcionAyuda.add_command(label='Licencia', command=Ayuda)
opcionAyuda.add_command(label='Sobre nosotros', command=sobreNosotros)

barraMenu.add_cascade(label="BBDD", menu=opcionBBDD)
barraMenu.add_cascade(label="Borrar", menu=opcionBorrar)
barraMenu.add_cascade(label="CRUD",menu=opcionCRUD)
barraMenu.add_cascade(label="Ayuda",menu=opcionAyuda)

# CAJAS de datos

# caja id

etiqueta_id = Label(miframe, text="Id:")
etiqueta_id.grid(row=0, pady=7, sticky="e")
id = Entry(miframe)
id.grid(row= 0, column=1,pady=7)

# caja nombre

etiqueta_nombre = Label(miframe, text="Nombre:")
etiqueta_nombre.grid(row=1, pady=7, sticky="e")
nombre = Entry(miframe)
nombre.grid(row= 1, column=1, pady=10, padx=10)

# caja contrasena

etiqueta_passw = Label(miframe, text="password:")
etiqueta_passw.grid(row=2, pady=7, sticky="e")
passw = Entry(miframe)
passw.grid(row= 2, column=1, pady=10, padx=10)
passw.config(show='*')

# caja apellido

etiqueta_apellido = Label(miframe, text="Apellido:")
etiqueta_apellido.grid(row=3, pady=7, sticky="e")
apellido = Entry(miframe)
apellido.grid(row= 3, column=1, pady=10, padx=10)

# caja direccion

etiqueta_direccion = Label(miframe, text="Direccion:")
etiqueta_direccion.grid(row=4, pady=7, sticky="e")
direccion = Entry(miframe)
direccion.grid(row= 4, column=1, pady=10, padx=10)

# caja comentrios y scrollbar de la caja comentarios

etiqueta_comentario = Label(miframe, text="Comentario:")
etiqueta_comentario.grid(row=5, column=0, sticky="w")
comentario = Text(miframe, width=18, height=7)
comentario.grid(row=5, column=1, pady=10, padx=10)
scrollvert = Scrollbar(miframe, command=comentario.yview)
scrollvert.grid(row=5, column=2, sticky='nsew')

comentario.config(yscrollcommand=scrollvert.set)

# Creacion de espacio para la creacion de los botones

miframe2 = Frame(ventana)
miframe2.pack()

# Botones

botonCrear = Button(miframe2, text="Create", command= create, cursor='hand2')
botonCrear.grid(row=7, column=0, padx=16)

botonRead = Button(miframe2, text="Read", command= read, cursor='hand2')
botonRead.grid(row=7, column=1, padx=16)

botonUpdate = Button(miframe2, text="Update", command= update, cursor='hand2')
botonUpdate.grid(row=7, column=2, padx=16)

botonDelete = Button(miframe2, text="Delete", command= Delete, cursor='hand2')
botonDelete.grid(row=7, column=3, padx=16)

ventana.mainloop()