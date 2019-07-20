# -*- coding: utf-8 -*-
"""
main.py
Creado el dia Jueves 27 de Junio a las 17:53:46 2019

@author: Alejandro Galindo, Francisco Felix, Alberto Grajeda

Modulo que crea una conexion simple con SQLSERVER utilizando el driver pyodbc
"""

import pyodbc 

def creaConexion():
    """
    Metodo que inicializa y retorna la conexión con SQLSERVER usando pyodbc
    """
    conn = pyodbc.connect('Driver={SQL Server};''Server=localhost;'
                      'Database=RadarDB;''Trusted_Connection=yes;')
    return conn
