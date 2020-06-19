# Tp7 – Capa Presentacion Socios
#
# Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .
#
# El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .
#
# Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
# Incluye  2 botones Guardar y Cancelar.
#
# Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .
#
# Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
# Incluye 2 botones Aceptar y Cancelar .


from tkinter import  *
from tkinter import ttk
import tkinter as tk
from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio
from capa_negocio import NegocioSocio

def agregar(a,b,c):
    x = arbol.insert("", tk.END, text=a,values=(b,c) )

def acept(a,b, c,v2):
    x = arbol.insert("", tk.END, text=a, values=(b, c))
    v2.destroy()

def cerrar(v2):
    v2.destroy()

def falta():
    v2 = Tk()
    v2.title('Alta Socio')
    n = Label(v2, width = 50, text = 'Ingrese Nombre:')
    ap = Label(v2, width = 50, text = 'Ingrese Apellido:')
    dni = Label(v2, width = 50, text = 'Ingrese DNI:')
    name = Entry(v2,  width=50)
    lname = Entry(v2,  width=50)
    dnie = Entry(v2, width=50)
    n.grid()
    name.grid()
    ap.grid()
    lname.grid()
    dni.grid()
    dnie.grid()
    ok = Button(v2, text = 'Aceptar', command = lambda: acept(name.get(), lname.get(), dnie.get(), v2))
    cancel = Button(v2, text = 'Cancelar', command = lambda: cerrar(v2))
    ok.grid()
    cancel.grid()
    v2.mainloop()

def fmodif(arbol):
    v2 = Tk()
    v2.title('Modificacion Socio')
    i = arbol.focus()
    m = arbol.item(i)
    uno = m['text']
    dos = m['values']
    n = Label(v2, width=50, text='Ingrese Nombre:')
    ap = Label(v2, width=50, text='Ingrese Apellido:')
    dni = Label(v2, width=50, text='Ingrese DNI:')
    name = Entry(v2, width=50)
    lname = Entry(v2, width=50)
    dnie = Entry(v2, width=50)
    name.insert(0, uno)
    lname.insert(0, dos[0])
    dnie.insert(0,dos[1])
    n.grid()
    name.grid()
    ap.grid()
    lname.grid()
    dni.grid()
    dnie.grid()
    ok = Button(v2, text='Aceptar', command=lambda: am(name.get(), lname.get(), dnie.get(), v2, i, arbol))
    cancel = Button(v2, text='Cancelar', command=lambda: cerrar(v2))
    ok.grid()
    cancel.grid()
    v2.mainloop()

def am(a,b,c,v2,id, arbol):
    arbol.item(id, text=a, values = [b,c])
    v2.destroy()

def fbaja(arbol):
    i=arbol.focus()
    arbol.delete(i)

window = Tk()
window.title('Socios')
arbol = ttk.Treeview()

arbol["columns"]=("one", "two", "three")

arbol.heading("#0",text="Nombre")
arbol.heading("#1",text="Apellido")
arbol.heading("#2",text="DNI")

alta = Button(window, text = 'Alta', command = falta)
modif = Button(window, text = 'Modificacion', command = lambda: fmodif(arbol))
baja = Button(window, text = 'Baja', command = lambda: fbaja(arbol))

arbol.grid()
alta.grid()
modif.grid()
baja.grid()


socios = NegocioSocio()
for i in socios.todos():
    agregar(i.nombre, i.apellido,i.dni)


window.mainloop()