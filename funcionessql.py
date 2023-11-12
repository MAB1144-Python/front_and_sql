import sqlite3
import pandas as pd
from openpyxl import Workbook

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
    return df["idusuario"].max()+ 1

def agregar_estudiante_sql(idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("insert into usuario (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario) values (?,?,?,?,?,?,?,?)", (idusuario,numerodocumento,nombres,apellidos,semestre,jornada, idprograma,idtipousuario))
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

def generar_idprestamo():
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    df = pd.read_sql_query("SELECT * from prestamo", conexion)
    print("++++++++++++++++++",len(df))
    idprestamo=0
    if len(df["idprestamo"])==0:
        idprestamo=1
    else:
        idprestamo=df["idprestamo"].max()+1
   
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    
    return idprestamo



def listado_prestamos(idusuario,fecha,programa):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    # cursor=conexion.execute("select * from usuario WHERE numerodocumento= "+ str(documento))
    if idusuario !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    elif fecha !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    elif programa !="":
        df = pd.read_sql_query("SELECT * from prestamo WHERE idusuario='"+str(idusuario)+"'", conexion)
    print(df)
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
def registrar_prestamo(descripcion,idusuario,idequipo,idauxiliar,fecha_entrada,fecha_salida):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    df = pd.read_sql_query("SELECT  * from prestamo", conexion)
    print(df)
    idprestamo = 1
    try:
        idprestamo = df["idprestamo"].max()+1
    except:
        idprestamo = 1
    print(idprestamo,type(idprestamo))
    cursor=conexion.execute("insert into prestamo (idprestamo,descripcion,idusuario,idequipo,idauxiliar,fecha_entrada,fecha_salida) values (?,?,?,?,?,?,?)", (int(idprestamo),descripcion,int(idusuario),int(idequipo),int(idauxiliar),"2023-01-01 T4:00:00","2023-01-01 T4:00:00"))#idprestamo,descripcion,3,4,int(idauxiliar),fecha_entrada,fecha_salida))
    conexion.commit()
    conexion.close()

#     """CREATE TABLE prestamo (
#   idprestamo integer auto_increment PRIMARY KEY,
#   descripcion text NOT NULL,
#   idusuario integer NOT NULL,
#   idequipo integer NOT NULL,
#   idauxiliar integer NOT NULL,
#   fecha_entrada TIMESTAMP  NULL, 
#   fecha_salida TIMESTAMP  NULL  
#print("muchos por",registrar_prestamo("hola",1,10,4,"2023-01-01 T4:00:00","2023-01-01 T4:00:00"))


