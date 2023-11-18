import sqlite3
import pandas as pd
import numpy as np
from openpyxl import Workbook
from datetime import datetime

def llamar_usuarios():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    sql_query = """SELECT name FROM sqlite_master 
	WHERE type='table';"""
    cursor=conexion.execute("select * from usuario ")
    print("entro 6")
    filas = []
    for fila in cursor:
        filas.append(fila)
    conexion.close()
    return filas



def buscar_estudiante_documento(documento):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    filas = []
    for fila in cursor:
        print(fila)
        filas.append(fila)
    conexion.close()
    return filas
    
def generar_idusuario():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT idusuario from usuario", conexion)

    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df["idusuario"].max()+ 1)
    try:
        idusuario = int(df["idusuario"].max()+ 1)
    except:
        idusuario = 1  
    return idusuario

def agregar_estudiante_sql(idusuario,numerodocumento,nombres,apellidos,semestre,jornada, programa,tipousuario,celular):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("insert into usuario (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, programa,tipousuario, celular) values (?,?,?,?,?,?,?,?,?)", (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, programa,tipousuario, celular))
    conexion.commit()
    conexion.close()
#conexion.execute("insert into usuario (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario) values (?,?,?,?,?,?,?,?)", (1,147,'jhon','cano',None,None,1,1))
#print(buscar_elementos())

def listado_de_sala():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT descripcion from sala", conexion)
    print(df)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df["descripcion"]==0)
    return df["descripcion"].values
    
def listado_idequipos():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    df = pd.read_sql_query("SELECT * from equipo", conexion)
    return df["idequipo"].values
    
def buscar_equipos():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    df = pd.read_sql_query("SELECT * from equipo", conexion)
    return df["descripcion"].values

def generar_idprestamo():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from prestamo", conexion)
    print("++++++++++++++++++",len(df))
    idprestamo=1
    if len(df["idprestamo"])==0:
        idprestamo=1
    else:
        idprestamo=df["idprestamo"].max()+1
   
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    
    return idprestamo

def listado_prestamos(idusuario="",fecha="",programa=""):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    if idusuario !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    elif fecha !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    elif programa !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    else:
        df = pd.read_sql_query("SELECT * from prestamo", conexion)
    print(df)
    df =list(df.values)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    return df


def listado_auxiliares():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from auxiliar", conexion)
    df =list(df["nombres"].values)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df

#parametros
def buscar_id_auxiliar(nombre_auxiliar):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT  idauxiliar from auxiliar WHERE nombres='"+nombre_auxiliar+"'", conexion)
    df =list(df["idauxiliar"].values)
    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/",df)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df[0]

def listado_sala():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from sala", conexion)
    df = list(df["descripcion"].values)
    return df

def listado_tipousuario():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))

    if True:# idtipousuario==0:
        df = pd.read_sql_query("SELECT * from tipousuario", conexion)
        df = list(df["descripcion"].values)
    # else:
    #     df = pd.read_sql_query("SELECT * from tipousuario WHERE idtipousuario ='"+str(idtipousuario)+"'", conexion)
    #     df = df["descripcion"].values   
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df

def buscar_tipo_usuario(idtipousuario):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
   
    if True:# idtipousuario==0:
        df = pd.read_sql_query("SELECT descripcion from tipousuario WHERE idtipousuario ="+idtipousuario+"'", conexion)
        df = list(df["descripcion"].values)
    print(df)
    return df

def listado_equipo():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from equipo", conexion)
    # df = list(df["descripcion"].values)
    return list(df.values)

def listado_usuario():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from usuario", conexion)
    return df.values

def descargar_usuarios(filename):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from usuario", conexion)
    df.to_excel(filename+"/datos_usuario.xlsx",sheet_name="usuarios")
    #convierte el data frame a archivo de excel

def descargar_equipos(filename):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from equipo", conexion)
    df.to_excel(filename+"/datos_equipos.xlsx",sheet_name="equipos")
    #convierte el data frame a archivo de excel

def descargar_prestamos(filename):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from prestamo", conexion)
    df.to_excel(filename+"/datos_prestamos.xlsx",sheet_name="prestamos")
    #convierte el data frame a archivo de excel

def buscar_usuario_sql(documento_usuario):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT  * from usuario WHERE numerodocumento='"+str(documento_usuario)+"'", conexion)
    df =list(df.values)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df

def agregar_registro_sala(idusuario,idauxiliar,fecha,descripcion):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    df = pd.read_sql_query("SELECT  * from registro_ingreso_sala", conexion)
    print(fecha)
    try:
        idregistro = df["idregistro"].max()+1
    except:
        idregistro = 1
    cursor=conexion.execute("insert into registro_ingreso_sala (idregistro,idusuario,idauxiliar,fecha,descripcion) values (?,?,?,?,?)", (int(idregistro),int(idusuario),int(idauxiliar),fecha,descripcion))
    conexion.commit()
    conexion.close()
#conexion.execute("insert into usuario (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario) values (?,?,?,?,?,?,?,?)", (1,147,'jhon','cano',None,None,1,1))
#print(buscar_elementos())
def registrar_prestamo(descripcion,documento,idequipo,auxiliar,fecha,carrera,sala,ubicacion):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("insert into prestamo (idprestamo,descripcion,documento,idequipo,auxiliar,fecha,carrera,sala,ubicacion) values (?,?,?,?,?,?,?,?,?)", (int(generar_idprestamo()),descripcion,int(documento),int(idequipo),auxiliar,fecha,carrera,sala,ubicacion))#idprestamo,descripcion,3,4,int(idauxiliar),fecha_entrada,fecha_salida))
    conexion.commit()
    conexion.close()

def dato_inicial_datatime(ini_Date, end_Date):
    print(ini_Date,end_Date)
    if ini_Date != None and ini_Date != "" and ini_Date !='-- ::00':
        ini_Date = datetime.strptime(str(ini_Date), "%Y-%m-%d %H:%M:%S")
    else:
        ini_Date = datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        
    if end_Date != None and end_Date != "" and end_Date !='-- ::00':
        end_Date = datetime.strptime(str(end_Date), "%Y-%m-%d %H:%M:%S")
    else:
        end_Date = datetime.now()
    return ini_Date,end_Date
    
def clean_T(A):
    try:
        a_l = A.split("T")
        print("/*-*/*-*/-*/-*/-*/-*",a_l)
        A = a_l[0]+a_l[1]
        return A
    except:
        return A

def filtro_prestamo(fecha_start, fecha_end, documento, carrera):
    fecha_start, fecha_end = dato_inicial_datatime(fecha_start, fecha_end)
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    df_filtro_prestamo = pd.read_sql_query("SELECT * from prestamo", conexion)
    #df_filtro_prestamo =list(df_filtro_prestamo.values)
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    # if fecha_start != "-":
    #     df_filtro_prestamo["fecha_entrada"] = df_filtro_prestamo["fecha_entrada"].apply(clean_T)
    #     df_filtro_prestamo["fecha_entrada"] = pd.to_datetime(df_filtro_prestamo["fecha_entrada"])
    #     filtro_cl1_ini, filtro_cl1_end = dato_inicial_datatime(fecha_start, fecha_end)
    #     df_filtro_prestamo = df_filtro_prestamo[df_filtro_prestamo["fecha_entrada"] >= fecha_start]

    # if fecha_end != "-":
    #     df_filtro_prestamo["fecha_salida"] = df_filtro_prestamo["fecha_salida"].apply(clean_T)
    #     df_filtro_prestamo["fecha_salida"] = pd.to_datetime(df_filtro_prestamo["fecha_salida"])
    #     filtro_cl1_ini, filtro_cl1_end = dato_inicial_datatime(fecha_start, fecha_end)
    #     df_filtro_prestamo = df_filtro_prestamo[df_filtro_prestamo["fecha_salida"] <= fecha_end]

    if documento != "":
        df_filtro_prestamo["documento"] = df_filtro_prestamo["documento"].astype("string")
        df_filtro_prestamo = df_filtro_prestamo[df_filtro_prestamo["documento"] == documento]

    if carrera != "":
        df_filtro_prestamo["carrera"] = df_filtro_prestamo["carrera"].astype("string")
        df_filtro_prestamo = df_filtro_prestamo[df_filtro_prestamo["carrera"] == carrera]
    print("115599",df_filtro_prestamo)    
    return df_filtro_prestamo.values

def buscar_estado_usuario(documento_usuario):
    #verifica si el usuario esta bloqueado
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT  estado from registro_bloqueados WHERE documento='"+str(documento_usuario)+"'", conexion)
    df =list(df.values)[0][0]
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df

def insert_estado_usuario(documento, estado):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("insert into registro_bloqueados  (documento, estado) values (?,?)", (documento, estado))
    conexion.commit()
    conexion.close()
    
def update_estado_usuario(documento, estado):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("UPDATE registro_bloqueados set estado='"+estado+"' WHERE documento='"+str(documento)+"'")
    conexion.commit()
    conexion.close()

tabla10= """CREATE TABLE registro_bloqueados (
 documento integer auto_increment PRIMARY KEY,
 estado text NOT NULL
)"""
#print("muchos por",filtro_prestamo("2023-01-01 4:00:00","2023-01-01 4:00:00","1064427622"))
print("6+879+/-*",update_estado_usuario(323165423,"Deshabilitado"))


