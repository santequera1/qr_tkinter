import os
from tkinter import *
from tkinter import messagebox as MessageBox
import qrcode
import tkinter as tk
from PIL import Image
os.system("cls")


#Funcion principal para generar el codigo QR y guardar la imagen
def crearQr():
    cadena = contenidoqr.get() #Obteniendo datos de la entrada principal
    nombre_imagen = nombredelarchivo.get() #Nombre del archivo
    nombre_imagen_final = nombre_imagen + ".png" # Agreando en formato Png al Nombre del Archivo
    imagen = qrcode.make(cadena) #Creando QR
    archivo_imagen = open(nombre_imagen_final, 'wb') #Creando imagen
    imagen.save(archivo_imagen) #Guardando imagen
    archivo_imagen.close()
    #Ventana Emergente
    MessageBox.showinfo(message="Tu Código QR se creó exitosamente", title="QR Generado")
    print("QR Generado Exitosamente")
    Image.open(nombre_imagen_final).show() #Abriendo imagen en el visor del sistema



#Función para borrar los textos de las entradas
def limpiarCampos():
        contenidoqr.delete(0, 'end')
        nombredelarchivo.delete(0, 'end')


#iniciando ventana principal y sus configuraciones
root = Tk()
root.config(bd=15) #Tamaño del borde
root['bg'] = '#004F9E' #Color de fondo de la ventana principal
root.geometry("275x410") #Ancno y alto de la ventana
root.iconbitmap("img/ventana-ico.ico") #icono de la ventana
root.title("Generador de QR") #Título de la ventana
entry = tk.Entry(
    # Color del fondo.
    background="#ff0000",
    # Color del texto.
    foreground="#0000ff",
)

#Imagen de personaje para adornar la ventana
imagen = PhotoImage(file="img/logo-inicio.png") #Ruta de la imagen
foto = Label(root, image=imagen, bd=0)
foto.grid(row=1, column=0, pady=30)
foto['bg'] = '#004F9E' #Color del fondo

#Titulo de Bienvenida
instrucciones = Label(text="BIENVENIDO")
instrucciones.config(font=("Montserrate", 18, "bold"),fg="#FFFFFF")
instrucciones.grid(row=0,column=0, padx=0, pady=20)
instrucciones['bg'] = '#004F9E'

#Texto que acompaña al título
texto_adicional = Label(text="Genera tus QR manera fácil y rápida")
texto_adicional.config(fg="#FFFFFF")
texto_adicional.grid(row=1,column=0, padx=0, pady=0)
texto_adicional.place(x=25, y=50) #Centrando el texto
texto_adicional['bg'] = '#004F9E' #Color de fondo

#Texto para indicar donde ingresar el nombre de la imagen
nombre_instruccion = Label(text="ingresa nombre de la imagen")
nombre_instruccion.config(fg="#FFFFFF")
nombre_instruccion.grid(row=1,column=0, padx=0, pady=0)
nombre_instruccion.place(x=0, y=200)
nombre_instruccion['bg'] = '#004F9E'

#Texto para indicar donde ingresar el contenido del QR
nombre_instruccion2 = Label(text="Ingresa contenido")
nombre_instruccion2.config(fg="#FFFFFF")
nombre_instruccion2.grid(row=1,column=0, padx=0, pady=10)
nombre_instruccion2.place(x=0, y=250)
nombre_instruccion2['bg'] = '#004F9E'

#Entrada de texto que va a recibir el nombre de la imagen
nombredelarchivo = Entry(root)
nombredelarchivo.grid(row=2,column=0, pady=5)
nombredelarchivo.config(width=40)

#Entrada de texto que va a recibir los datos del codigo QR
contenidoqr = Entry(root)
contenidoqr.grid(row=3,column=0, pady=25)
contenidoqr.config(width=40)
contenidoqr['bg'] = '#fff'

#Botón principal para generar QR, asociado a la función "crearQR"
boton_generador_qr = Button(root, text="Generar QR ✅", command=crearQr)
boton_generador_qr.grid(row=4,column=0, pady=0)
boton_generador_qr.config(width=20, height=2) #Alto y ancho del botón
boton_generador_qr['bg'] = '#E20613' #Color de fondo del boton
boton_generador_qr['fg'] = '#FFFFFF' #Color del texto
boton_generador_qr.place(x=0, y=320) #Posicionamiento del botón



#Botón para limpiar los campos, asociado a la función "limpiar_campos"
boton_limpiar = Button(root, text="limpiar ↩",command=limpiarCampos)
boton_limpiar.grid(row=4, column=1)
boton_limpiar.config(width=10, height=2)
boton_limpiar['bg'] = '#FFFFFF' #Color del texto
boton_limpiar.place(x=160, y=320)


#Correr la ventana
root.mainloop()