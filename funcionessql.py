import sqlite3
import pandas as pd

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

def registrar_prestamo(idprestamo,descripcion,idusuario,idequipo,idauxiliar,fecha):
    conexion=sqlite3.connect("control_de_modulo_salas.db")
    cursor=conexion.execute("insert into prestamo (idprestamo,descripcion,idusuario,idequipo,idauxiliar,fecha_prestamo) values (?,?,?,?,?,?)", (idprestamo,descripcion,idusuario,idequipo,idauxiliar,fecha))
    conexion.commit()
    conexion.close()

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
    #nos sirve para crear el id busca los id identificas cual es el mayor y le suma uno para garantizar que el id no existe
    print(df)
    return df

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


print("muchos por",buscar_id_auxiliar("majo auxiliar"))


