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
