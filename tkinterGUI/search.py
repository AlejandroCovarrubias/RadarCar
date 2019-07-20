# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:53:46 2019

@author: Alejandro Galindo
"""

import pyodbc
import connection as conn
import drawer as tzr

def obtenerRastreo():
    """
    Metodo que obtiene el numero de rastreos hechos en la DB y lo retorna
    """
    cursor = conn.creaConexion()

    rows = cursor.execute('SELECT MAX(ID) FROM Points')

    for i in rows:
        idmax = i[0]

    return idmax

def obtenerIDsRastreo():
    """
    Metodo que obtiene una lista de las IDs de rastreo de la DB y lo retorna
    """
    cursor = conn.creaConexion()
    rows = cursor.execute('SELECT ID FROM Points GROUP BY ID')
    ids = []
    for i in rows:
        ids.append(i[0])
        print(ids)
    return ids

def obtenerPoints(ID):
    """
    Metodo que obtiene los puntos guardados en la BD del sistema
    """
    cursor = conn.creaConexion()
    rows = cursor.execute('SELECT * FROM Points WHERE ID = ' + "'" + str(ID) + "'")
    return rows

def insertarPoints(points, idAct):
    """
    Metodo que inserta un array de puntos en la BD del sistema
    """
    cursor = conn.creaConexion()

    for i in points:
        cursor.execute(
            """
            INSERT INTO Points (ID, XCoordinate, YCoordinate, Angle, Distance)
            VALUES(?,?,?,?,?)
            """,
            (idAct, i[0],i[1],i[2],i[3])
        )
    cursor.commit()
    
