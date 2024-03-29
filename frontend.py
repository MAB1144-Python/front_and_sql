from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from funcionessql import (
    llamar_usuarios,
    buscar_estudiante_documento,
    generar_idusuario,
    agregar_estudiante_sql,
    registrar_prestamo,
    generar_idprestamo,
    listado_sala,
    listado_auxiliares,
    listado_prestamos,
    listado_tipousuario,
    listado_usuario,
    listado_equipo,
    generar_idprestamo,
    buscar_id_auxiliar,
    descargar_usuarios,
    descargar_equipos,
    descargar_prestamos,
    buscar_usuario_sql,
    agregar_registro_sala,
    buscar_tipo_usuario,
    insert_estado_usuario,
    update_estado_usuario,
    buscar_estado_usuario,
    listado_idequipos,
    filtro_prestamo
)
from datetime import datetime

IDUSUARIO_GLOBAL = 0
fecha_prestamo = "-"
fecha_entrega = "-"
app = Tk()
app.title("ASIGNATOR GTM")
app.config(bg="white")
app.geometry("1500x800")

Ventana_principal = Frame(app, bg="#00acc9")
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

    entrada_nombre_registro["values"] = nombres
    entrada_documento_registro["values"] = documentos

def clean():
    entrada_NOM.delete(0, "end")
    entrada_APE.delete(0, "end")
    entrada_DOCMID.delete(0, "end")
    entrada_PROG.delete(0, "end")
    entrada_ingrese_semestre.delete(0, "end")
    entrada_ingrese_jornada.delete(0, "end")
    entrada_ingrese_programa.delete(0, "end")
    estado_usuario.delete(0, "end")
    entrada_telefono.delete(0, "end")


def agregar_prestamo():
    if entrada_IDequipo.get() != "" and entrada_nombre_auxiliar.get() != "" and entrada_ingrese_programa.get() != "" and entrada_DOCMID.get() != "" and entrada_Sala.get() != "" and entrada_ubicacion.get() != "":
        Buscar_usuario()
        global IDUSUARIO_GLOBAL
        estadousuario = estado_usuario.get()
        fecha_registro = "-"
        descripcion_registro = ""
        def fecha_entrada_l():
            fecha_entrada = (
                entrada_ano.get()
                + "-"
                + entrada_Mes.get()
                + "-"
                + entrada_dia.get()
                + " "
                + entrada_Hora.get()
                + ":"
                + entrada_Minuto.get()
                + ":00"
            )
            return fecha_entrada

        def fecha_salida_l():
            fecha_salida = (
                salida_Año.get()
                + "-"
                + salida_Mes.get()
                + "-"
                + salida_dia.get()
                + " "
                + salida_Hora.get()
                + ":"
                + salida_Minuto.get()
                + ":00"
            )
            return fecha_salida

        def cerrar_ventana():
            # if salida_Año.get() != "" and salida_Mes.get() != "" and salida_dia.get() != "" and salida_Hora.get() != "" and  salida_Minuto.get() != "":
            #     fecha_entrega_equipo = fecha_salida_l()
            fecha_prestamo_equipo = "-"
            if entrada_ano.get() != "" and entrada_Mes.get() != "" and entrada_dia.get() != "" and entrada_Hora.get() != "" and  entrada_Minuto.get() != "":
                fecha_prestamo_equipo = fecha_entrada_l()
            print(fecha_prestamo_equipo)
            if fecha_prestamo_equipo != "-" and entrada_descripcion.get() != "":
                fecha_registro = fecha_prestamo_equipo
                descripcion_registro = entrada_descripcion.get()
                if entrada_DOCMID.get() != "" and entrada_IDequipo.get() != "" and entrada_nombre_auxiliar.get() != "" and entrada_ingrese_programa.get()  != "":
                    registro(fecha_registro,descripcion_registro)
                else:
                    messagebox.showerror("Error", "Debe ingresar todos los datos")
                ventana_agregar_prestamos.destroy()
            else:
                messagebox.showerror("Error", "Debe ingresar una de las fechas")

        def registro(fecha_registro,descripcion_registro):
            print(entrada_ingrese_programa.get())
            if descripcion_registro == "Entrega equipo":
                registrar_prestamo(descripcion_registro,entrada_DOCMID.get(),entrada_IDequipo.get(),entrada_nombre_auxiliar.get(),fecha_registro,entrada_ingrese_programa.get(),entrada_Sala.get(),entrada_ubicacion.get())  
                #update_estado_usuario(entrada_DOCMID.get(), "Deshabilitado")
            else:
                registrar_prestamo(descripcion_registro,entrada_DOCMID.get(),entrada_IDequipo.get(),entrada_nombre_auxiliar.get(),fecha_registro,entrada_ingrese_programa.get(),entrada_Sala.get(),entrada_ubicacion.get())
                #update_estado_usuario(entrada_DOCMID.get(), "Habilitado")

        if estadousuario != "Deshabilitado":
            fechaentregausuario = "-"
            fechaentregasala = "-"
            app.geometry("1500x800")
            ventana_agregar_prestamos = Toplevel(app, bg="#00acc9")
            ventana_agregar_prestamos.title("Prestamos")
            fecha_entrada_text = Label(
                ventana_agregar_prestamos,
                text="Fecha y Hora de Entrada:",
                font="arial 8 bold",
                bg="mint cream",
            )
            fecha_entrada_text.grid(column=6, row=6, sticky=(N, W))

            fecha_entrada_text = Label(
                ventana_agregar_prestamos, text="Dia:", font="arial 8 bold", bg="mint cream"
            )
            fecha_entrada_text.grid(column=9, row=6, sticky=(N, W))
            entrada_dia = Entry(ventana_agregar_prestamos, width=5)
            entrada_dia.grid(column=9, row=7, sticky="w")
            fecha_entrada_text = Label(
                ventana_agregar_prestamos, text="Mes:", font="arial 8 bold", bg="mint cream"
            )
            fecha_entrada_text.grid(column=8, row=6, sticky=(N, W))
            entrada_Mes = ttk.Combobox(
                ventana_agregar_prestamos,
                values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                width=5,
            )
            entrada_Mes.grid(column=8, row=7, sticky="w")


            fecha_entrada_text = Label(
                ventana_agregar_prestamos, text="Año:", font="arial 8 bold", bg="mint cream"
            )
            fecha_entrada_text.grid(column=7, row=6, sticky=(N, W))
            entrada_ano = ttk.Combobox(
                ventana_agregar_prestamos,
                values=[2023, 2024, 2025, 2026, 2027, 2028],
                width=5,
            )
            entrada_ano.grid(column=7, row=7, sticky="w")

            fecha_entrada_text = Label(
                ventana_agregar_prestamos,
                text="Hora:",
                font="arial 8 bold",
                bg="mint cream",
            )
            fecha_entrada_text.grid(column=10, row=6, sticky=(N, W))
            entrada_Hora = ttk.Combobox(
                ventana_agregar_prestamos,
                values=list(range(24)),
                width=5,
            )
            entrada_Hora.grid(column=10, row=7, sticky="w")


            fecha_entrada_text = Label(
                ventana_agregar_prestamos,
                text="Minuto:",
                font="arial 8 bold",
                bg="mint cream",
            )
            fecha_entrada_text.grid(column=11, row=6, sticky=(N, W))
            entrada_Minuto = ttk.Combobox(
                ventana_agregar_prestamos,
                values=list(range(60)),
                width=5,
            )
            entrada_Minuto.grid(column=11, row=7, sticky="w")

            exit_button = Button(
                ventana_agregar_prestamos, text="Registrar", command=cerrar_ventana
            )
            exit_button.grid(column=6, row=13, pady=5, sticky="w")

            DOCMID_text = Label(
            ventana_agregar_prestamos, text="Descripcion:", font="arial 8 bold", bg="mint cream"
            )
            DOCMID_text.grid(column=6, row=11, sticky=(N, W))
            entrada_descripcion = ttk.Combobox(
            ventana_agregar_prestamos, values=["Entrega equipo", "Retorno equipo"], width=15
            )
            entrada_descripcion.grid(column=7, row=11, sticky="w")
        else:
            messagebox.showerror(
                "Error", "Usuario no habilitado para realizar nuevos prestamos"
            )
    else:
            messagebox.showerror(
                "Error", "Debe ingresar el idequipo el ausxiliar, documento, sala, "
            )

def cambiar_estado():
    documento = entrada_DOCMID.get()
    if estado_usuario.get() != "" and documento != "":
        update_estado_usuario(documento, estado_usuario.get())
        messagebox.showinfo(
            message="Estado actualizado", title="Actualización de datos"
        )
    else:
        messagebox.showinfo(
            message="Agrege la identificación y seleccione el estado que desea registrar",
            title="Flatan datos",
        )

def agregar_estudiante():
    global IDUSUARIO_GLOBAL
    nombre = entrada_NOM.get()
    apellido = entrada_APE.get()
    documento = entrada_DOCMID.get()
    programa = entrada_ingrese_programa.get()
    semestre = entrada_ingrese_semestre.get()
    jornada = entrada_ingrese_jornada.get()
    tipodeusuario = tipo_usuario.get()
    estadousuario = estado_usuario.get()
    celular = entrada_telefono.get()
    print(nombre, apellido, documento, programa, semestre, jornada, tipodeusuario)
    habilitar_clean = False
    if (
        tipodeusuario == "invitado"
        and nombre != ""
        and apellido != ""
        and documento != ""
        and programa != ""
    ):
        habilitar_clean = True
        data_usuarios = buscar_estudiante_documento(documento)
        if len(data_usuarios) == 0:
            idusuario = generar_idusuario()
            print(idusuario)
            agregar_estudiante_sql(
                int(idusuario),
                int(documento),
                nombre,
                apellido,
                "-",
                "-",
                programa,
                tipodeusuario,
                "-"
            )  # idprograma,idtipousuario
            data_usuarios = buscar_estudiante_documento(documento)
        if len(data_usuarios) == 0:
            idusuario = generar_idusuario()
            print(idusuario)
            agregar_estudiante_sql(
                int(idusuario),
                int(documento),
                nombre,
                apellido,
                semestre,
                jornada,
                programa,
                tipodeusuario,
                celular
            )  # idprograma,idtipousuario
            insert_estado_usuario(int(documento), estadousuario)
    elif (
        tipodeusuario != "invitado"
        and nombre != ""
        and apellido != ""
        and documento != ""
        and programa != ""
        and semestre != ""
        and jornada != ""
        and tipodeusuario != ""
        and celular != ""
    ):
        habilitar_clean = True
        data_usuarios = buscar_estudiante_documento(documento)
        if len(data_usuarios) == 0:
            idusuario = generar_idusuario()
            print(idusuario)
            agregar_estudiante_sql(
                int(idusuario),
                int(documento),
                nombre,
                apellido,
                semestre,
                jornada,
                programa,
                tipodeusuario,
                celular
            )  # idprograma,idtipousuario
            insert_estado_usuario(int(documento), estadousuario)
        data_usuarios = buscar_estudiante_documento(documento)
        data_usuarios = list(data_usuarios[0])
        entrada_NOM.delete(0, "end")
        entrada_APE.delete(0, "end")
        entrada_DOCMID.delete(0, "end")
        entrada_PROG.delete(0, "end")
        entrada_ingrese_semestre.delete(0, "end")
        entrada_ingrese_jornada.delete(0, "end")
        entrada_telefono.delete(0, "end")

        print(data_usuarios)
        IDUSUARIO_GLOBAL = data_usuarios[0]
        entrada_IDusuario.insert(INSERT, str(IDUSUARIO_GLOBAL))
        print("este es idusuario global", IDUSUARIO_GLOBAL)
        entrada_NOM.insert(INSERT, str(data_usuarios[2]))
        entrada_APE.insert(INSERT, str(data_usuarios[3]))
        entrada_DOCMID.insert(INSERT, str(data_usuarios[1]))
        entrada_ingrese_programa.insert(INSERT, str(data_usuarios[4]))
        entrada_ingrese_semestre.insert(INSERT, str(data_usuarios[6]))
        entrada_ingrese_jornada.insert(INSERT, str(data_usuarios[7]))
        entrada_nombre_registro.insert(INSERT, str(data_usuarios[2]))
        entrada_telefono.insert(INSERT, str(data_usuarios[8]))
    else:
        messagebox.showinfo(message="faltan datos", title="Selección")

# deletes de todas las entradas
def clean_formulario():
    entrada_NOM.delete(0, "end")
    entrada_APE.delete(0, "end")
    entrada_DOCMID.delete(0, "end")
    entrada_PROG.delete(0, "end")
    entrada_ingrese_semestre.delete(0, "end")
    entrada_ingrese_jornada.delete(0, "end")
    entrada_nombre_auxiliar.delete(0, "end")
    entrada_idauxiliar.delete(0, "end")
    entrada_IDequipo.delete(0, "end")
    entrada_ingrese_jornada.delete(0, "end")
    entrada_ingrese_programa.delete(0, "end")
    entrada_ingrese_semestre.delete(0, "end")
    entrada_Sala.delete(0, "end")
    tipo_usuario.delete(0, "end")
    entrada_ingrese_programa.delete(0, "end")
    estado_usuario.delete(0, "end")
    tipo_usuario.delete(0, "end")


def Descargar_usuarios():
    print("descargar usuarios")
    filename = fd.askdirectory()
    print(filename)
    descargar_usuarios(filename)


def Descargar_equipos():
    print("descargar equipos")
    filename = fd.askdirectory()
    print(filename)
    descargar_equipos(filename)


def Buscar_usuario():
    global IDUSUARIO_GLOBAL
    tipo_usuario.delete(0, "end")
    documento_usuario = entrada_DOCMID.get()
    print(documento_usuario)
    Usuario_recibido = buscar_usuario_sql(documento_usuario)
    print(Usuario_recibido)
    print(Usuario_recibido)

    if len(Usuario_recibido) == 0:
        print("usuario no existente")
        tipo_usuario.insert(INSERT, "invitado")
        messagebox.showerror(
            message="Usuario no existente, si se va a registrar como invitado solo ingrese nombre, apellido y programa de interés, si se va a registrar como estudiante o profesor debe llenar todos los datos' ",
            title="informacion",
        )
    else:
        clean()
        Usuario_recibido = Usuario_recibido[0]
        IDUSUARIO_GLOBAL = Usuario_recibido[0]
        print("***************************************", IDUSUARIO_GLOBAL,Usuario_recibido)
        if buscar_estado_usuario(Usuario_recibido[1]) == "Deshabilitado":
            messagebox.showinfo(
                message="Usuario deshabilitado", title="Alerta"
            )

        # entrada_IDusuario.insert(INSERT, str(IDUSUARIO_GLOBAL))
        print("este es idusuario global", IDUSUARIO_GLOBAL)
        entrada_NOM.insert(INSERT, str(Usuario_recibido[2]))
        entrada_APE.insert(INSERT, str(Usuario_recibido[3]))
        entrada_DOCMID.insert(INSERT, str(Usuario_recibido[1]))
        entrada_ingrese_programa.insert(INSERT, str(Usuario_recibido[6]))
        entrada_ingrese_semestre.insert(INSERT, str(Usuario_recibido[4]))
        entrada_ingrese_jornada.insert(INSERT, str(Usuario_recibido[5]))
        estado_usuario.insert(INSERT, buscar_estado_usuario(Usuario_recibido[1]))
        tipo_usuario.insert(INSERT, str(Usuario_recibido[7]))
        entrada_telefono.insert(INSERT, str(Usuario_recibido[8]))

def Registrar_en_sala():
    global IDUSUARIO_GLOBAL
    print("registrar en sala")
    idusuario = IDUSUARIO_GLOBAL
    idauxiliar = buscar_id_auxiliar(entrada_nombre_auxiliar.get())
    entrada_idauxiliar.insert(INSERT, str(idauxiliar))
    fecha = fecha_entrada()
    descripcion_sala = entrada_descripcion.get()
    if idusuario != "" and idauxiliar != "" and fecha != "" and descripcion_sala:
        agregar_registro_sala(idusuario, idauxiliar, fecha, descripcion_sala)
    else:
        messagebox.showerror("Error", "Por favor, ingrese los datos")

def mostrar_estudiantes():
    print("entro linea 105")
    ventana_estudiantes = Toplevel(app)
    ventana_estudiantes.title("Estudiantes registrados")
    print(llamar_usuarios())
    print("salio linea 78")

    # Crear etiquetas para mostrar los detalles de cada estudiante
    if True:
        # Crear un Treeview con columnas
        tabla = ttk.Treeview(
            ventana_estudiantes,
            columns=(
                "id usuario",
                "documento",
                "nombres",
                "apellidos",
                "semestre",
                "jornada",
                "id programa",
                "id tipousuario",
            ),
        )
        # ("idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario")
        # Definir encabezados de columnas
        tabla.heading("id usuario", text="ID")
        tabla.heading("documento", text="Documento")
        tabla.heading("nombres", text="Nombre")
        tabla.heading("apellidos", text="Apellidos")
        tabla.heading("semestre", text="Semestre")
        tabla.heading("jornada", text="Jornada")
        tabla.heading("id programa", text="Programa")
        tabla.heading("id tipousuario", text="Tipo de Usuario")
        # Agregar datos a la tabla
        # Puedes reemplazar esto con tus propios datos
        for data_usuario in listado_usuario():
            print(data_usuario)
            data_usuario = list(data_usuario)
            tabla.insert(
                "",
                "end",
                text="1",
                values=(
                    data_usuario[0],
                    data_usuario[1],
                    data_usuario[2],
                    data_usuario[3],
                    data_usuario[4],
                    data_usuario[5],
                    data_usuario[6],
                    data_usuario[7],
                ),
            )
        tabla.pack()
        # Ejecutar el bucle principal
        ventana_estudiantes.mainloop()


def mostrar_equipos():
    ventana_equipos = Toplevel(app)
    ventana_equipos.title("Equipos")

    # Crear etiquetas para mostrar los detalles de cada equipo
    if True:
        # Crear un Treeview con columnas
        tabla = ttk.Treeview(
            ventana_equipos, columns=("id equipo", "descripcion", "sala")
        )
        # ()
        # Definir encabezados de columnas
        tabla.heading("id equipo", text="ID Equipo")
        tabla.heading("descripcion", text="Descripcion")
        tabla.heading("sala", text="Sala")
        for data_equipo in listado_equipo():
            print(data_equipo)
            data_equipo = list(data_equipo)
            tabla.insert(
                "",
                "end",
                text="1",
                values=(data_equipo[0], data_equipo[1], data_equipo[2]),
            )
        tabla.pack()
        # Ejecutar el bucle principal
        ventana_equipos.mainloop()


def registrar_estudiante_en_sala():
    # Obtener la sala seleccionada del Combobox
    nombre_registro = entrada_nombre_registro.get()
    documento_registro = entrada_documento_registro.get()
    sala_seleccionada = lista_salas_registrar.get()

    # Verificar si se seleccionó una sala
    if sala_seleccionada:
        estudiante_seleccionado = next(
            (
                e
                for e in estudiantes
                if e.nombre == nombre_registro and e.documento == documento_registro
            ),
            None,
        )
        fecha_entrada = entrada_fecha_entrada.get()
        fecha_salida = entrada_fecha_salida.get()

        if estudiante_seleccionado and sala_seleccionada:
            registro = Registro(
                estudiante_seleccionado,
                sala_seleccionada,
                fecha_entrada,
                fecha_salida,
            )
            registros.append(registro)

            # Resto del código de limpieza de entradas
            entrada_nombre_registro.set("")
            entrada_documento_registro.set("")
            entrada_fecha_entrada.delete(0, "end")
            entrada_fecha_salida.delete(0, "end")
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

def informacion():

    def fecha_entrada_l():
            fecha_entrada2 = (
                entrada2_ano.get()
                + "-"
                + entrada2_Mes.get()
                + "-"
                + entrada2_dia.get()
                + " "
                + entrada2_Hora.get()
                + ":"
                + entrada2_Minuto.get()
                + ":00"
            )
            return fecha_entrada2

    def fecha_salida_l():
            fecha_salida = (
                salida_Año.get()
                + "-"
                + salida_Mes.get()
                + "-"
                + salida_dia.get()
                + " "
                + salida_Hora.get()
                + ":"
                + salida_Minuto.get()
                + ":00"
            )
            return fecha_salida


    def Descargar_prestamos():
        print("descargar prestamos")
        filename = fd.askdirectory()
        print(filename)
        fecha_start, fecha_end = fecha_entrada_l(), fecha_salida_l()
        df_prestamos = filtro_prestamo(fecha_start, fecha_end, documento_informes.get(), programa_informes.get())
        descargar_prestamos(filename,df_prestamos )


    def mostrar_prestamos():
        ventana_prestamos = Toplevel(app)
        ventana_prestamos.title("Prestamos")

        # Crear etiquetas para mostrar los detalles de cada equipo
        print(listado_prestamos("", "", ""))
        if True:
            # Crear un Treeview con columnas
            tabla = ttk.Treeview(
                ventana_prestamos,
                columns=(
                    "ID prestamo",
                    "Descripcion",
                    "ID usuario",
                    "ID equipo",
                    "ID auxiliar",
                    "Fecha prestamo",
                    "Fecha prestamo2",
                    "Ubicacion", 
                    "Sala",
                ),
            )
            # ()
            # Definir encabezados de columnas
            tabla.heading("ID equipo", text="ID Equipo")
            tabla.heading("Descripcion", text="Descripcion")
            tabla.heading("ID usuario", text="ID usuario")
            tabla.heading("ID equipo", text="ID equipo")
            tabla.heading("ID auxiliar", text="ID auxiliar")
            tabla.heading("Fecha prestamo", text="Fecha prestamo")
            tabla.heading("Fecha prestamo2", text="Fecha prestamo2")
            tabla.heading("Ubicacion", text="Ubicacion")
            tabla.heading("Sala", text="Sala")

            # Agregar datos a la tabla
            # Puedes reemplazar esto con tus propios datos
            fecha_start, fecha_end = fecha_entrada_l(), fecha_salida_l()
            for data_prestamos in filtro_prestamo(fecha_start, fecha_end, documento_informes.get(), programa_informes.get()).values:
                data_prestamos = list(data_prestamos)
                tabla.insert(
                    "",
                    "end",
                    text="1",
                    values=(
                        data_prestamos[0],
                        data_prestamos[1],
                        data_prestamos[2],
                        data_prestamos[3],
                        data_prestamos[4],
                        data_prestamos[5],
                        data_prestamos[6],
                    ),
                )
            tabla.pack()
            # Ejecutar el bucle principal
            ventana_prestamos.mainloop()


    ventana_informes = Toplevel(app, bg="#00acc9")
    ventana_informes.title("Informes y descargas") 
    
    titulo_sala = Label(ventana_informes, text="Filtros para prestamo", font="arial 10 bold", bg="#132740", fg="white",  width=24)
    titulo_sala.grid(row=1, column=0, columnspan=1, sticky=(N, W))

    cck_informe_documento = Checkbutton(ventana_informes, text="Informe por documento", font="arial 8 bold", command=informe_documento)
    cck_informe_documento.grid(row=19, column=1, columnspan=1, pady=0)

    cck_informe_fechas = Checkbutton(ventana_informes, text="Informe por fechas", font="arial 8 bold", command=informe_fechas)
    cck_informe_fechas.grid(row=19, column=2, columnspan=1, pady=0)

    cck_informe_programa= Checkbutton(ventana_informes, text="Informe por programa", font="arial 8 bold", command=informe_programa)
    cck_informe_programa.grid(row=19, column=3, columnspan=1, pady=0)

    fecha_entrada2_text = Label(
       ventana_informes,
        text="Fecha y Hora de entrada2:",
        font="arial 8 bold",
        bg="mint cream",
    )
    fecha_entrada2_text.grid(column=0, row=6, sticky=(N, W))

    fecha_salida_text = Label(
       ventana_informes,
        text="Fecha y Hora de Salida:",
        font="arial 8 bold",
        bg="mint cream",
    )
    fecha_salida_text.grid(column=0, row=9, sticky=(N, W))

    fecha_entrada2_text = Label(
       ventana_informes, text="Dia:", font="arial 8 bold", bg="mint cream"
    )
    fecha_entrada2_text.grid(column=3, row=6, sticky=(N, W))
    entrada2_dia = Entry(ventana_informes, width=5)
    entrada2_dia.grid(column=3, row=7, sticky="w")

    fecha_salida_text = Label(
       ventana_informes, text="Dia:", font="arial 8 bold", bg="mint cream"
    )
    fecha_salida_text.grid(column=3, row=9, sticky=(N, W))
    salida_dia = Entry(ventana_informes, width=5)
    salida_dia.grid(column=3, row=10, sticky="w")


    fecha_entrada2_text = Label(
       ventana_informes, text="Mes:", font="arial 8 bold", bg="mint cream"
    )
    fecha_entrada2_text.grid(column=2, row=6, sticky=(N, W))
    entrada2_Mes = ttk.Combobox(
       ventana_informes, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], width=5
    )
    entrada2_Mes.grid(column=2, row=7, sticky="w")

    fecha_salida_text = Label(
       ventana_informes, text="Mes:", font="arial 8 bold", bg="mint cream"
    )
    fecha_salida_text.grid(column=2, row=9, sticky=(N, W))
    salida_Mes = ttk.Combobox(
       ventana_informes, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], width=5
    )
    salida_Mes.grid(column=2, row=10, sticky="w")


    fecha_entrada2_text = Label(
       ventana_informes, text="Año:", font="arial 8 bold", bg="mint cream"
    )
    fecha_entrada2_text.grid(column=1, row=6, sticky=(N, W))
    entrada2_ano = ttk.Combobox(
       ventana_informes, values=[2023, 2024, 2025, 2026, 2027, 2028], width=5
    )
    entrada2_ano.grid(column=1, row=7, sticky="w")

    fecha_salida_text = Label(
       ventana_informes, text="Año:", font="arial 8 bold", bg="mint cream"
    )
    fecha_salida_text.grid(column=1, row=9, sticky=(N, W))
    salida_Año = ttk.Combobox(
       ventana_informes, values=[2023, 2024, 2025, 2026, 2027, 2028], width=5
    )
    salida_Año.grid(column=1, row=10, sticky="w")

    fecha_entrada2_text = Label(
       ventana_informes, text="Hora:", font="arial 8 bold", bg="mint cream"
    )
    fecha_entrada2_text.grid(column=4, row=6, sticky=(N, W))
    entrada2_Hora = ttk.Combobox(
       ventana_informes,
        values = list(range(24)),
        width=5,
    )
    entrada2_Hora.grid(column=4, row=7, sticky="w")

    fecha_salida_text = Label(
       ventana_informes, text="Hora:", font="arial 8 bold", bg="mint cream"
    )
    fecha_salida_text.grid(column=4, row=9, sticky=(N, W))
    salida_Hora = ttk.Combobox(
       ventana_informes,
        values=list(range(24)),
        width=5,
    )
    salida_Hora.grid(column=4, row=10, sticky="w")

    fecha_entrada2_text = Label(
       ventana_informes, text="Minuto:", font="arial 8 bold", bg="mint cream"
    )
    fecha_entrada2_text.grid(column=5, row=6, sticky=(N, W))
    entrada2_Minuto = ttk.Combobox(
       ventana_informes,
        values=list(range(60)),
        width=5,
    )
    entrada2_Minuto.grid(column=5, row=7, sticky="w")

    fecha_salida_text = Label(
       ventana_informes, text="Minuto:", font="arial 8 bold", bg="mint cream"
    )
    fecha_salida_text.grid(column=5, row=9, sticky=(N, W))
    salida_Minuto = ttk.Combobox(
       ventana_informes,
        values=list(range(60)),
        width=5,
    )
    salida_Minuto.grid(column=5, row=10, sticky="w")

    documento_informes_text = Label(ventana_informes, text="Documento:", font="arial 8 bold", bg="mint cream")
    documento_informes_text.grid(column=0, row=12, sticky=(N, W))
    documento_informes = Entry(ventana_informes, width=20)
    documento_informes.grid(row=12, column=1, sticky="w")

    programa_informes_text = Label(ventana_informes, text="Seleccione el programa:", font="arial 8 bold", bg="mint cream",)
    programa_informes_text.grid(column=0, row=13, sticky=(N, W))
    programa_informes = ttk.Combobox(
    ventana_informes,
    values=[
        "Administracion de empresas",
        "Derecho",
        "Psicologia",
        "Comercio Internacional",
        "Contaduria Publica",
        "Ingenieria Ambiental",
        "Ingenieria Industrial",
        "Ingenieria de Sistemas",
    ],
    width=23,
    )
    programa_informes.grid(column=1, row=13, sticky="w")

    titulo_sala = Label(ventana_informes, text="Descargas y visualización", font="arial 10 bold", bg="#132740", fg="white",  width=24)
    titulo_sala.grid(row=16, column=0, columnspan=1, sticky=(N, W))

    btn_ver_estudiantes = Button(
    ventana_informes,
    text="Ver Usuarios",
    font="arial 8 bold",
    command=mostrar_estudiantes,
    )
    btn_ver_estudiantes.grid(row=1, column=1, columnspan=1, pady=0)

    btn_ver_equipos = Button(
    ventana_informes, text="Ver Equipos", font="arial 8 bold", command=mostrar_equipos
    )   
    btn_ver_equipos.grid(row=1, column=2, columnspan=1, pady=0)

    btn_ver_prestamos = Button(
    ventana_informes,
    text="Ver Prestamos",
    font="arial 8 bold",
    command=mostrar_prestamos,
    )
    btn_ver_prestamos.grid(row=18, column=2, columnspan=1, pady=0)

    btn_descargar_usuarios = Button(ventana_informes, text="Descargar Usuarios", font="arial 8 bold", command=Descargar_usuarios)
    btn_descargar_usuarios.grid(row=2, column=1, columnspan=1, pady=0)

    btn_descargar_equipos = Button(ventana_informes, text="Descargar Equipos", font="arial 8 bold", command=Descargar_equipos)
    btn_descargar_equipos.grid(row=2, column=2, columnspan=1, pady=0)

    btn_descargar_prestamos = Button(ventana_informes, text="Descargar Prestamos", font="arial 8 bold", command=Descargar_prestamos)
    btn_descargar_prestamos.grid(row=18, column=3, columnspan=1, pady=0)



numsala_text = Label(
    Ventana_principal, text="Salas:", font="arial 8 bold", bg="mint cream"
)
numsala_text.grid(row=17, column=0, sticky=(N, W))
entrada_Sala = ttk.Combobox(Ventana_principal, values=listado_sala(), width=15)
entrada_Sala.grid(column=1, row=17, sticky="w")

tipo_usuario_text = Label(
    Ventana_principal, text="Tipo de usuario:", font="arial 8 bold", bg="mint cream"
)
tipo_usuario_text.grid(column=0, row=8, sticky=(N, W))
tipo_usuario = ttk.Combobox(Ventana_principal, values=listado_tipousuario(), width=20)

tipo_usuario.grid(column=1, row=8, sticky="w")

telefono_text = Label(
    Ventana_principal, text="Telefono:", font="arial 8 bold", bg="mint cream"
)
telefono_text.grid(column=0, row=10, sticky=(N, W))
entrada_telefono = Entry(Ventana_principal, width=15)
entrada_telefono.grid(column=1, row=10, sticky="w")

estado_usuario_text = Label(
    Ventana_principal, text="Estado:", font="arial 8 bold", bg="mint cream"
)
estado_usuario_text.grid(column=0, row=11, sticky=(N, W))
estado_usuario = ttk.Combobox(
    Ventana_principal, values=["Habilitado", "Deshabilitado"], width=20
)
estado_usuario.grid(column=1, row=11, sticky="w")


def informe_documento():
    ()


def informe_fechas():
    ()


def informe_programa():
    ()


# Widgets de texto
NOM_text = Label(
    Ventana_principal, text="Ingrese el nombre:", font="arial 8 bold", bg="mint cream"
)
NOM_text.grid(column=0, row=2, sticky=(N, W))
APE_text = Label(
    Ventana_principal, text="Ingrese el apellido:", font="arial 8 bold", bg="mint cream"
)
APE_text.grid(column=0, row=3, sticky=(N, W))
DOCMID_text = Label(
    Ventana_principal,
    text="Ingrese el documento de identidad:",
    font="arial 8 bold",
    bg="mint cream",
)
DOCMID_text.grid(column=0, row=4, sticky=(N, W))
PROG_text = Label(
    Ventana_principal,
    text="Seleccione el programa:",
    font="arial 8 bold",
    bg="mint cream",
)
PROG_text.grid(column=0, row=5, sticky=(N, W))
SEMES_text = Label(
    Ventana_principal,
    text="Seleccione el semestre:",
    font="arial 8 bold",
    bg="mint cream",
)
SEMES_text.grid(column=0, row=6, sticky=(N, W))
JOR_text = Label(
    Ventana_principal,
    text="Seleccione la jornada:",
    font="arial 8 bold",
    bg="mint cream",
)
JOR_text.grid(column=0, row=7, sticky=(N, W))
entrada_NOM = Entry(Ventana_principal, width=15)
entrada_NOM.grid(column=1, row=2, sticky="w")
entrada_APE = Entry(Ventana_principal, width=15)
entrada_APE.grid(column=1, row=3, sticky="w")
entrada_DOCMID = Entry(Ventana_principal, width=15)
entrada_DOCMID.grid(column=1, row=4, sticky="w")
entrada_PROG = Entry(Ventana_principal, width=15)
entrada_ingrese_programa = ttk.Combobox(
    Ventana_principal,
    values=[
        "Administracion de empresas",
        "Derecho",
        "Psicologia",
        "Comercio Internacional",
        "Contaduria Publica",
        "Ingenieria Ambiental",
        "Ingenieria Industrial",
        "Ingenieria de Sistemas",
    ],
    width=23,
)
entrada_ingrese_programa.grid(column=1, row=5, sticky="w")
entrada_ingrese_semestre = ttk.Combobox(
    Ventana_principal,
    values=list(range(1,10,1)),
    width=6,
)
entrada_ingrese_semestre.grid(column=1, row=6, sticky="w")
entrada_ingrese_jornada = ttk.Combobox(
    Ventana_principal, values=["Diurna", "Nocturna"], width=8
)
entrada_ingrese_jornada.grid(column=1, row=7, sticky="w")

# btn_mostrar_registros = Button(
#     Ventana_principal,
#     text="Mostrar registros",
#     font="arial 8 bold",
#     command=mostrar_registros,
# )
# btn_mostrar_registros.grid(column=2, row=19, columnspan=1, pady=0, sticky="w")

btn_agregar_estudiante = Button(
    Ventana_principal,
    text="Agregar Usuario",
    font="arial 8 bold",
    command=agregar_estudiante,
)
btn_agregar_estudiante.grid(row=15, column=1, columnspan=1, pady=15)

btn_cambiar_estado = Button(
    Ventana_principal,
    text="Cambiar Estado",
    font="arial 8 bold",
    command=cambiar_estado,
)
btn_cambiar_estado.grid(row=15, column=2, columnspan=1, pady=15)

btn_agregar_prestamos = Button(
    Ventana_principal,
    text="Agregar Prestamo",
    font="arial 8 bold",
    command=agregar_prestamo,
)
btn_agregar_prestamos.grid(row=22, column=1, columnspan=1, pady=15)

btn_buscar_usuario = Button(
    Ventana_principal,
    text="Buscar Usuario",
    font="arial 8 bold",
    command=Buscar_usuario,
)
btn_buscar_usuario.grid(row=15, column=0, columnspan=1, pady=2)

btn_registrar_en_sala = Button(
    Ventana_principal,
    text="Registrar en sala",
    font="arial 8 bold",
    command=Registrar_en_sala,
)
btn_registrar_en_sala.grid(row=22, column=0, columnspan=1, pady=0)

btn_informes = Button(Ventana_principal, text="Informes", font="arial 8 bold", command=informacion)
btn_informes.grid(row=24, column=1, columnspan=1, pady=0)

titulo_sala = Label(
    Ventana_principal,
    text="Datos Estudiantes",
    font="arial 10 bold",
    bg="#132740",
    fg="white",
    width=16,
)
titulo_sala.grid(row=1, column=0, columnspan=1, sticky=(N, W))


titulo_sala = Label(
    Ventana_principal,
    text="Crear registros o Prestamos",
    font="arial 10 bold",
    bg="#132740",
    fg="white",
    width=24,
)
titulo_sala.grid(row=16, column=0, columnspan=1, sticky=(N, W))

APE_text = Label(
    Ventana_principal, text="ID Equipo:", font="arial 8 bold", bg="mint cream"
)
APE_text.grid(column=0, row=18, sticky=(N, W))
entrada_IDequipo = ttk.Combobox(Ventana_principal, values=list(listado_idequipos()), width=15)
entrada_IDequipo.grid(row=18, column=1, sticky="w")
DOCMID_text = Label(
    Ventana_principal, text="Auxiliar:", font="arial 8 bold", bg="mint cream"
)
DOCMID_text.grid(column=0, row=19, sticky=(N, W))
entrada_nombre_auxiliar = ttk.Combobox(
    Ventana_principal, values=listado_auxiliares(), width=15
)
entrada_nombre_auxiliar.grid(column=1, row=19, sticky="w")
NOM_text = Label(
    Ventana_principal, text="ID Auxiliar:", font="arial 8 bold", bg="mint cream"
)
NOM_text.grid(column=2, row=19, sticky=(N, W))
entrada_idauxiliar = Entry(Ventana_principal, width=20)
entrada_idauxiliar.grid(row=20, column=2, sticky="w")

DOCMID_text = Label(
    Ventana_principal, text="Ubicacion:", font="arial 8 bold", bg="mint cream"
)
DOCMID_text.grid(column=0, row=20, sticky=(N, W))
entrada_ubicacion = ttk.Combobox(
    Ventana_principal, values=["Bibilioteca", "Area de T.I"], width=15
)
entrada_ubicacion.grid(column=1, row=20, sticky="w")

img = PhotoImage(file="UCC.png")
imagen_redimensionada = img.subsample(10)
label_imagen = Label(Ventana_principal, image=imagen_redimensionada)
label_imagen.grid(column=13, row=1)

etiqueta = Label(
    Ventana_principal, text="Developer Maria Jose Noreña, Alexandra Otero and Samuel."
)
etiqueta.grid(column=13, row=2, sticky=(W, E))


btn_limpiar_formulario = Button(
    Ventana_principal,
    text="Limpiar Formulario",
    font="arial 8 bold",
    command=clean_formulario,
)
btn_limpiar_formulario.grid(row=22, column=2, columnspan=1, pady=0)


app.mainloop()
