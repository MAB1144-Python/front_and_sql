from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from funcionessql import llamar_usuarios, buscar_estudiante_documento,generar_idusuario,agregar_estudiante_sql,registrar_prestamo,generar_idprestamo,listado_sala,listado_auxiliares,listado_prestamos,listado_tipousuario
from datetime import datetime

app = Tk() 
app.title("MODULOS SALAS")
app.config(bg="white")
app.geometry("800x600")

Ventana_principal = Frame(app, bg='cadetblue4')
Ventana_principal.pack(fill="both", expand="true")

# Listas para almacenar estudiantes , registros y salas 
estudiantes = []
salas = []
registros = []

class Estudiante:
    def __init__(self, nombre, apellido, documento, programa, semestre, jornada):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.programa = programa
        self.semestre = semestre
        self.jornada = jornada

    def __str__(self):
        return self.nombre + " " + self.apellido

class Sala:
    def __init__(self, numsala, numequipo):
        self.numsala = numsala
        self.numequipo = numequipo

    def __str__(self):
        return "Sala: " + self.numsala + ", Equipo: " + self.numequipo

class Registro:
    def __init__(self, estudiante, sala, fecha_entrada, fecha_salida):
        self.estudiante = estudiante
        self.sala = sala
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

# Funciones de actualización
def actualizar_dropdown_estudiantes():
    nombres = [e.nombre for e in estudiantes]
    documentos = [e.documento for e in estudiantes]
    
    entrada_nombre_registro['values'] = nombres
    entrada_documento_registro['values'] = documentos


def agregar_estudiante():
    nombre = entrada_NOM.get()
    apellido = entrada_APE.get()
    documento = entrada_DOCMID.get()
    programa = entrada_PROG.get()
    semestre = entrada_SEMES.get()
    jornada = entrada_JOR.get()
    if nombre !="" and apellido !="" and documento !="" and  programa !="" and semestre !="" and jornada !="":# en la 81
        data_usuarios = buscar_estudiante_documento(documento)
        print("/*/*/*/*/*/*/*/*/*/*/*/*",len(data_usuarios))
        if  len(data_usuarios)==0:
            idusuario = generar_idusuario()
            print(idusuario)
            agregar_estudiante_sql(int(idusuario),int(documento),nombre,apellido,semestre,jornada,1,1)  #idprograma,idtipousuario
        data_usuarios = buscar_estudiante_documento(documento)
        data_usuarios = list(data_usuarios[0])
        entrada_NOM.delete(0, 'end')
        entrada_APE.delete(0, 'end')
        entrada_DOCMID.delete(0, 'end')
        entrada_PROG.delete(0, 'end')
        entrada_SEMES.delete(0, 'end')
        entrada_JOR.delete(0, 'end')

        print(data_usuarios)
        entrada_NOM.insert(INSERT,str(data_usuarios[2]))
        entrada_APE.insert(INSERT,str(data_usuarios[3]))
        entrada_DOCMID.insert(INSERT,str(data_usuarios[1]))
        entrada_PROG.insert(INSERT,str(data_usuarios[4]))
        entrada_SEMES.insert(INSERT,str(data_usuarios[6]))
        entrada_JOR.insert(INSERT,str(data_usuarios[7]))
    else:
        print("faltan datos")


def agregar_prestamo():# en la 74
    IDusuario = entrada_IDusuario.get()
    IDequipo= entrada_IDequipo.get()
    IDauxiliar = entrada_IDauxiliar.get()
    Descripcion = entrada_Descripcion.get()
    idprestamo= generar_idprestamo()
    fecha_prestamo = datetime.fromisoformat('2011-11-04T00:05:23')
    try:
        registrar_prestamo(int(idprestamo),Descripcion,int(IDusuario),int(IDequipo),int(IDauxiliar),fecha_prestamo)
    except:
        print("se genero un error en agregrar_prestamo linea 98")







def mostrar_estudiantes():
    print("entro linea 105")
    ventana_estudiantes = Toplevel(app)
    ventana_estudiantes.title("Estudiantes registrados")
    print(llamar_usuarios())
    print("salio linea 78")

# Crear etiquetas para mostrar los detalles de cada estudiante
    for idx, estudiante in enumerate(estudiantes):
        detalles_estudiante = f"Nombre: {estudiante.nombre}\n"
        detalles_estudiante += f"Apellido: {estudiante.apellido}\n"
        detalles_estudiante += f"Documento: {estudiante.documento}\n"
        detalles_estudiante += f"Programa: {estudiante.programa}\n"
        detalles_estudiante += f"Semestre: {estudiante.semestre}\n"
        detalles_estudiante += f"Jornada: {estudiante.jornada}"

        Label(ventana_estudiantes, text=detalles_estudiante).grid(row=idx * 7, column=0, sticky="w")

def agregar_sala():
    numsala = entrada_numsala.get()
    numequipo = entrada_numequipo.get()

    sala = Sala(numsala, numequipo)
    salas.append(sala)

    actualizar_dropdown_salas()

    entrada_numsala.delete(0, 'end')
    entrada_numequipo.delete(0, 'end')

def actualizar_dropdown_salas():
    lista_salas_registrar['values'] = [str(s) for s in salas]

def mostrar_salas():
    ventana_salas = Toplevel(app)
    ventana_salas.title("Salas registradas")
 # Crear etiquetas para mostrar los detalles de cada sala
    for idx, sala in enumerate(salas):
        detalles_sala = f"Sala: {sala.numsala}\n"
        detalles_sala += f"Equipos: {sala.numequipo}\n"

        Label(ventana_salas, text=detalles_sala).grid(row=idx * 3, column=0, sticky="w")

def registrar_estudiante_en_sala():
    
# Obtener la sala seleccionada del Combobox
    nombre_registro = entrada_nombre_registro.get()
    documento_registro = entrada_documento_registro.get()
    sala_seleccionada = lista_salas_registrar.get()

# Verificar si se seleccionó una sala
    if sala_seleccionada:
        estudiante_seleccionado = next((e for e in estudiantes if e.nombre == nombre_registro and e.documento == documento_registro), None)
        fecha_entrada = entrada_fecha_entrada.get()
        fecha_salida = entrada_fecha_salida.get()

        if estudiante_seleccionado and sala_seleccionada:
            registro = Registro(estudiante_seleccionado, sala_seleccionada, fecha_entrada, fecha_salida)
            registros.append(registro)

 # Resto del código de limpieza de entradas
            entrada_nombre_registro.set('')
            entrada_documento_registro.set('')
            entrada_fecha_entrada.delete(0, 'end')
            entrada_fecha_salida.delete(0, 'end')
        else:
 # Mostrar un mensaje de error si no se encuentra el estudiante
            messagebox.showerror("Error", "Estudiante no encontrado.")
    else:
# Mostrar un mensaje de error si no se selecciona una sala
        messagebox.showerror("Error", "Por favor, seleccione una sala.")

def mostrar_registros():
    ventana_registros = Toplevel(app)
    ventana_registros.title("Registros")

    # Crear una lista para almacenar los registros como cadenas
    registros_str = []
    for registro in registros:
        registro_str = f"{registro.estudiante} - {registro.sala} - Entrada: {registro.fecha_entrada} - Salida: {registro.fecha_salida}"
        registros_str.append(registro_str)

    # Crear una etiqueta para cada registro en la ventana de registros
    for idx, registro_str in enumerate(registros_str):
        Label(ventana_registros, text=registro_str).grid(row=idx, column=0, sticky="w")

# Combobox para seleccionar una sala
sala_registro_text = Label(Ventana_principal, text="Seleccione una sala:", font="arial 8 bold", bg="mint cream")
sala_registro_text.grid(column=0, row=26, sticky=(N, W))
lista_salas_registrar = ttk.Combobox(Ventana_principal, values=[str(s) for s in salas], width=20)
lista_salas_registrar.grid(column=1, row=26, sticky="w")

nombre_registro_text = Label(Ventana_principal, text="Nombre del Estudiante:", font="arial 8 bold", bg="mint cream")
nombre_registro_text.grid(column=0, row=27, sticky=(N, W))
entrada_nombre_registro = ttk.Combobox(Ventana_principal, values=[], width=15)
entrada_nombre_registro.grid(column=1, row=27, sticky="w")

documento_registro_text = Label(Ventana_principal, text="Documento del Estudiante:", font="arial 8 bold", bg="mint cream")
documento_registro_text.grid(column=0, row=28, sticky=(N, W))
entrada_documento_registro = ttk.Combobox(Ventana_principal, values=[], width=15)
entrada_documento_registro.grid(column=1, row=28, sticky="w")

# Llamar a la función para actualizar las opciones iniciales
actualizar_dropdown_salas()

# Agregar las etiquetas y entradas para la fecha y hora al registrar un estudiante en una sala
fecha_entrada_text = Label(Ventana_principal, text="Fecha y Hora de Entrada:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=6, row=6, sticky=(N, W))

fecha_salida_text = Label(Ventana_principal, text="Fecha y Hora de Salida:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=6, row=9, sticky=(N, W))

fecha_entrada_text = Label(Ventana_principal, text="Dia:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=7, row=6, sticky=(N, W))
entrada_fecha_DD = Entry(Ventana_principal, width=5)
entrada_fecha_DD.grid(column=7, row=7, sticky="w")

fecha_salida_text = Label(Ventana_principal, text="Dia:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=7, row=9, sticky=(N, W))
salida_fecha_DD = Entry(Ventana_principal, width=5)
salida_fecha_DD.grid(column=7, row=10, sticky="w")


fecha_entrada_text = Label(Ventana_principal, text="Mes:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=8, row=6, sticky=(N, W))
entrada_Mes = ttk.Combobox(Ventana_principal, values=[1,2,3,4,5,6,7,8,9,10,11,12], width=5)
entrada_Mes.grid(column=8, row=7, sticky="w")

fecha_salida_text = Label(Ventana_principal, text="Mes:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=8, row=9, sticky=(N, W))
salida_Mes = ttk.Combobox(Ventana_principal, values=[1,2,3,4,5,6,7,8,9,10,11,12], width=5)
salida_Mes.grid(column=8, row=10, sticky="w")


fecha_entrada_text = Label(Ventana_principal, text="Año:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=9, row=6, sticky=(N, W))
entrada_Año = ttk.Combobox(Ventana_principal, values=[2023,2024,2025,2026,2027,2028], width=5)
entrada_Año.grid(column=9, row=7, sticky="w")

fecha_salida_text = Label(Ventana_principal, text="Año:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=9, row=9, sticky=(N, W))
salida_Año = ttk.Combobox(Ventana_principal, values=[2023,2024,2025,2026,2027,2028], width=5)
salida_Año.grid(column=9, row=10, sticky="w")

fecha_entrada_text = Label(Ventana_principal, text="Hora:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=10, row=6, sticky=(N, W))
entrada_Hora = ttk.Combobox(Ventana_principal, values=[00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], width=5)
entrada_Hora.grid(column=10, row=7, sticky="w")

fecha_salida_text = Label(Ventana_principal, text="Hora:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=10, row=9, sticky=(N, W))
salida_Hora = ttk.Combobox(Ventana_principal, values=[00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], width=5)
salida_Hora.grid(column=10, row=10, sticky="w")

fecha_entrada_text = Label(Ventana_principal, text="Minuto:", font="arial 8 bold", bg="mint cream")
fecha_entrada_text.grid(column=11, row=6, sticky=(N, W))
entrada_Minuto = ttk.Combobox(Ventana_principal, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60], width=5)
entrada_Minuto.grid(column=11, row=7, sticky="w")

fecha_salida_text = Label(Ventana_principal, text="Minuto:", font="arial 8 bold", bg="mint cream")
fecha_salida_text.grid(column=11, row=9, sticky=(N, W))
salida_Minuto = ttk.Combobox(Ventana_principal, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60], width=5)
salida_Minuto.grid(column=11, row=10, sticky="w")


# Widgets de texto
NOM_text = Label(Ventana_principal, text="Ingrese el nombre:", font="arial 8 bold", bg="mint cream")
NOM_text.grid(column=0, row=2, sticky=(N, W))
APE_text = Label(Ventana_principal, text="Ingrese el apellido:", font="arial 8 bold", bg="mint cream")
APE_text.grid(column=0, row=3, sticky=(N, W))
DOCMID_text = Label(Ventana_principal, text="Ingrese el documento de identidad:", font="arial 8 bold", bg="mint cream")
DOCMID_text.grid(column=0, row=4, sticky=(N, W))
PROG_text = Label(Ventana_principal, text="Ingrese el programa:", font="arial 8 bold", bg="mint cream")
PROG_text.grid(column=0, row=5, sticky=(N, W))
SEMES_text = Label(Ventana_principal, text="Ingrese el semestre:", font="arial 8 bold", bg="mint cream")
SEMES_text.grid(column=0, row=6, sticky=(N, W))
JOR_text = Label(Ventana_principal, text="Ingrese la jornada:", font="arial 8 bold", bg="mint cream")
JOR_text.grid(column=0, row=7, sticky=(N, W))
# Etiquetas y entradas para salas
numsala_text = Label(Ventana_principal, text="Salas:", font="arial 8 bold", bg="mint cream")
numsala_text.grid(row=8, column=0, sticky=(N, W))
entrada_Sala = ttk.Combobox(Ventana_principal, values=listado_sala(), width=15)
entrada_Sala.grid(column=1, row=8, sticky="w")

numequipo_text = Label(Ventana_principal, text="Equipos:", font="arial 8 bold", bg="mint cream")
numequipo_text.grid(row=9, column=0, sticky=(N, W))
entrada_numequipo = Entry(Ventana_principal,width=15)
entrada_numequipo.grid(row=9, column=1, sticky="w")

# Entradas de texto
entrada_NOM = Entry(Ventana_principal, width=15)
entrada_NOM.grid(column=1, row=2, sticky="w")
entrada_APE = Entry(Ventana_principal, width=15)
entrada_APE.grid(column=1, row=3, sticky="w")
entrada_DOCMID = Entry(Ventana_principal, width=15)
entrada_DOCMID.grid(column=1, row=4, sticky="w")
entrada_PROG = Entry(Ventana_principal, width=15)
entrada_PROG.grid(column=1, row=5, sticky="w")
entrada_SEMES = Entry(Ventana_principal, width=15)
entrada_SEMES.grid(column=1, row=6, sticky="w")
entrada_JOR = Entry(Ventana_principal, width=15)
entrada_JOR.grid(column=1, row=7, sticky="w")
entrada_JOR = Entry(Ventana_principal, width=15)
entrada_JOR.grid(column=1, row=8, sticky="w")



# Reemplace los Entry por ttk.Combobox
#entrada_nombre_registro = ttk.Combobox(Ventana_principal, values=[], width=15)
#entrada_nombre_registro.grid(column=1, row=19, sticky="w")

#entrada_documento_registro = ttk.Combobox(Ventana_principal, values=[], width=15)
#entrada_documento_registro.grid(column=1, row=18, sticky="w")

#entrada_fecha_entrada = Entry(Ventana_principal, width=20)
#entrada_fecha_entrada.grid(column=1, row=20, sticky="w")

#entrada_fecha_salida = Entry(Ventana_principal, width=20)
#entrada_fecha_salida.grid(column=1, row=21, sticky="w")

# Botones de registro
btn_mostrar_registros = Button(Ventana_principal, text="Mostrar registros", font="arial 8 bold", command=mostrar_registros)
btn_mostrar_registros.grid(column=2, row=15, sticky="w")

btn_agregar_estudiante = Button(Ventana_principal, text="Agregar Estudiantes", font="arial 8 bold", command=agregar_estudiante)
btn_agregar_estudiante.grid(row=1, column=7, columnspan=2, pady=15)

btn_agregar_sala = Button(Ventana_principal, text="Agregar Sala", font="arial 8 bold", command=agregar_sala)
btn_agregar_sala.grid(row=10, column=0, columnspan=2, pady=15)

btn_registrar = Button(Ventana_principal, text="Registrar Estudiante en Sala", font="arial 8 bold", command=registrar_estudiante_en_sala)
btn_registrar.grid(row=1, column=7, columnspan=2, pady=15)

btn_ver_estudiantes = Button(Ventana_principal, text="Ver Usuarios", font="arial 8 bold", command=mostrar_estudiantes)
btn_ver_estudiantes.grid(row=12, column=7, columnspan=2, pady=15)

btn_ver_salas = Button(Ventana_principal, text="Ver Salas", font="arial 8 bold", command=mostrar_salas)
btn_ver_salas.grid(row=13, column=7, columnspan=2, pady=15)

btn_agregar_prestamos = Button(Ventana_principal, text="Agregar Prestamo", font="arial 8 bold", command=agregar_prestamo)
btn_agregar_prestamos.grid(row=35, column=0, columnspan=2, pady=15)


# Titulos
titulo_sala = Label(Ventana_principal, text="Datos Estudiantes", font="arial 8 bold", bg="mint cream",  width=16)
titulo_sala.grid(row=1, column=0, columnspan=1, sticky=(N, W))

#titulo_sala = Label(Ventana_principal, text="Crear Salas", font="arial 10 bold", bg="mint cream",  width=50)
#titulo_sala.grid(row=12, column=0, columnspan=1, sticky=(N, W))

titulo_sala = Label(Ventana_principal, text="Crear registros", font="arial 8 bold", bg="mint cream",  width=14)
titulo_sala.grid(row=16, column=0, columnspan=1, sticky=(N, W))

titulo_sala = Label(Ventana_principal, text="Prestamos", font="arial 8 bold", bg="mint cream",  width=10)
titulo_sala.grid(row=29, column=0, columnspan=1, sticky=(N, W))

#label de prestamos
NOM_text = Label(Ventana_principal, text="ID Usuario:", font="arial 8 bold", bg="mint cream")
NOM_text.grid(column=0, row=30, sticky=(N, W))
entrada_IDusuario = Entry(Ventana_principal,width=15)
entrada_IDusuario.grid(row=30, column=1, sticky="w")
APE_text = Label(Ventana_principal, text="ID Equipo:", font="arial 8 bold", bg="mint cream")
APE_text.grid(column=0, row=32, sticky=(N, W))
entrada_IDequipo = Entry(Ventana_principal,width=15)
entrada_IDequipo.grid(row=32, column=1, sticky="w")
DOCMID_text = Label(Ventana_principal, text="ID Auxiliar:", font="arial 8 bold", bg="mint cream")
DOCMID_text.grid(column=0, row=33, sticky=(N, W))
entrada_IDauxiliar = ttk.Combobox(Ventana_principal, values=[], width=5)
entrada_IDauxiliar.grid(column=1, row=33, sticky="w")
DOCMID_text = Label(Ventana_principal, text="Descripcion:", font="arial 8 bold", bg="mint cream")
DOCMID_text.grid(column=0, row=34, sticky=(N, W))
entrada_Descripcion = Entry(Ventana_principal,width=20)
entrada_Descripcion.grid(row=34, column=1, sticky="w")





app.mainloop()
