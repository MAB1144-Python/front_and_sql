import numpy as np
from tkinter import PhotoImage
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import filedialog as fd




primeramedida = []
segundamedida = []

###### formula para calcular la media 
def resultado_media():
    print(" obtuve el resultado")
    median_uno = np.median(primeramedida)
    print(
        "la mediana de la primera  medida es: ",
        median_uno,
    )
    median_dos = np.median(segundamedida)
    print("la mediana de la segunda media es: ", median_dos)
    salida_media_uno.insert(INSERT,str(median_uno))
    salida_media_dos.insert(INSERT,str(median_dos))


 ###### formula para calcular la desviacion estandar 
def resultado_desviacion():
    resultado_desviacion_uno= np.std(primeramedida)
    print("la desviacion estandar de las primera medida es: ",resultado_desviacion_uno)
    resultado_desviacion_dos=np.std(segundamedida)
    print("la desviacion estandar de la segunda medida es: ",resultado_desviacion_dos)
    salida_desviacion_uno.insert(INSERT,str(resultado_desviacion_uno))
    salida_desviacion_dos.insert(INSERT,str(resultado_desviacion_dos))
#cargar el archivo formula#
#lo que hicimos es abrir una ventana de busqueda y seleccionamos el archivo y el programa me retorna la ruta y los datos que contiene el archivo#

def cargar_file():
  filename = fd.askopenfilename()
  error_text3.config(text="")
  print(filename)
  with open(filename) as archivo:
    ach = []
    for linea in archivo:
        ach.append(linea.replace("\n",""))
    linea_1 = ach[0].split(",")
    linea_2 = ach[1].split(",")
    for dt in linea_1:
      try:
        primeramedida.append(float(dt))
      except:
        error_text3.config(text="Error de valores en el archivo")
        continue
    for dt in linea_2:
      try:
        segundamedida.append(float(dt))
      except:
        error_text3.config(text="Error de valores en el archivo")
        continue

  
# ******************************#
#!/usr/bin/python
# -- coding: utf-8 --
# www.pythondiario.com

import sys
from tkinter import *


# //////////////////////////////////////////////////////////////////////////////////////////////////////


def cargar_parejas():
    try:
        valor1 = float(entrada_primervalor.get())
        valor2 = float(entrada_segundovalor.get())
        _n = int(entrada_n.get())
        if(len(primeramedida)!=_n):
            primeramedida.append(valor1)
            segundamedida.append(valor2)
        #len es la funcion que se encarga de medir el vector
        print("primera medida", primeramedida, )

        print("segunda medida", segundamedida)
        error_text1.config(text="")
        error_text2.config(text="")
    except:
        error_text1.config(text="Error de valor")
        error_text2.config(text="Error de valor")


app = Tk()
app.title("Calculadora de Media y Desviacion Estandar ")

# Ventana Principal
vp = Frame(app)
vp.grid(column=6, row=12, padx=(10, 10), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)
vp.config(bg='#84BF04')



# button load file
bt4 = Button(vp, text="load file", command=cargar_file)
bt4.grid(column=1, row=10)
bt4.config(bg='#FFD700')
bt4 = Button(vp, text="cargar parejas", command=cargar_parejas)
bt4.grid(column=1, row=8)
bt4.config(bg='#FFD700')
# ++++++++++++++
# button salir
bt1 = Button(vp, text="Salir", command=quit)
bt1.grid(column=1, row=13)
bt1.config(bg='#FFD700')
# +++++++++++++#


bt2 = Button(vp, text="calculate average", command=resultado_media)
bt2.grid(column=1, row=12)
bt2.config(bg='#FFD700')
bt3 = Button(vp, text="calculate stander", command=resultado_desviacion)
bt3.grid(column=1, row=11)
bt3.config(bg='#FFD700')
# text ingrese n
n_text = Label(vp, text="Ingrese el número de parejas")
n_text.grid(column=0, row=1, sticky=(W, E))
n_text.config(bg='#FFD700')
error_text1 = Label(vp, text="")
error_text1.grid(column=2, row=2, sticky=(W, E))
error_text1.config(bg='#84BF04')
error_text2 = Label(vp, text="")
error_text2.grid(column=2, row=3, sticky=(W, E))
error_text2.config(bg='#84BF04')
error_text3 = Label(vp, text="")
error_text3.grid(column=2, row=10, sticky=(W, E))
error_text3.config(bg='#84BF04')
# ++++++++++++++#
# input ingrese n
n = ""
entrada_n = Entry(vp, width=10, textvariable=n)
entrada_n.grid(column=1, row=1)
# ++++++++++++++++
etiqueta = Label(vp, text="Resultado de la Media")
etiqueta.grid(column=0, row=5, sticky=(W, E))
etiqueta.config(bg='#FFD700')
####################
etiqueta = Label(vp, text="primera medida")
etiqueta.grid(column=1, row=4, sticky=(W, E))
etiqueta.config(bg='#FFDAB9')
###################
etiqueta = Label(vp, text="segunda medida")
etiqueta.grid(column=2, row=4, sticky=(W, E))
etiqueta.config(bg='#FFDAB9')



# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')

etiqueta = Label(vp, text="Primer Valor")
etiqueta.grid(column=0, row=2, sticky=(W, E))
etiqueta.config(bg='#FFD700')

etiqueta = Label(vp, text="Segundo Valor")
etiqueta.grid(column=0, row=3, sticky=(W, E))
etiqueta.config(bg='#FFD700')
etiqueta = Label(vp, text="Resultado de la Desviacion Estándar")
etiqueta.grid(column=0, row=6, sticky=(W, E))
etiqueta.config(bg='#FFD700')


etiqueta = Label(vp, text="Developer Maria Jose Noreña and Alexandra Otero")
etiqueta.grid(column=0, row=14, sticky=(W, E))

# Crear un widget Label para mostrar la imagen
img = PhotoImage(file='UCC.png')
imagen_redimensionada = img.subsample(16)
label_imagen = Label(vp, image=imagen_redimensionada)
label_imagen.grid(column=0, row=10)

primer_valor = ""
entrada_primervalor = Entry(vp, width=10, textvariable=primer_valor)
entrada_primervalor.grid(column=1, row=2)

segundo_valor = ""
entrada_segundovalor = Entry(vp, width=10, textvariable=segundo_valor)
entrada_segundovalor.grid(column=1, row=3)

media = ""
salida_media_uno = Entry(vp, width=10, textvariable=media)
salida_media_uno.grid(column=1, row=5)

media = ""
salida_media_dos = Entry(vp, width=10, textvariable=media)
salida_media_dos.grid(column=2, row=5)

desviacion = ""
salida_desviacion_uno = Entry(vp, width=10, textvariable=desviacion)
salida_desviacion_uno.grid(column=1, row=6)

desviacion = ""
salida_desviacion_dos = Entry(vp, width=10, textvariable=desviacion)
salida_desviacion_dos.grid(column=2, row=6)


app.mainloop()