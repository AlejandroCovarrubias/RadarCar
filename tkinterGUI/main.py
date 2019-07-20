# -*- coding: utf-8 -*-
"""
main.py
Creado el dia Jueves 27 de Junio a las 17:53:46 2019

@author: Alejandro Galindo, Francisco Felix, Alberto Grajeda

Modulo principal que despliega una interfaz con dos botones para escoger entre 
las dos funciones principales del sistema.

Este codigo no funcionara si un arduino no esta conectado al puerto serie
"""

#Librerias
from tkinter import *
from tkinter import messagebox
import math
import Trazador as tz
import time
import Scans as sc
import serial as sl
import re
import radar as rc
import radarDB as rcbd

def centrar(win):
    """
    Metodo que centra el frame en el centro de la pantalla de la computadora
    """
    window_width = 600 #ancho del frame
    window_height = 350 #alto del frame
    
    screen_width = win.winfo_screenwidth() #obtiene el ancho de la pantalla
    screen_height = win.winfo_screenheight() #obtiene el alto de la pantalla
    
    x_cordinate = int((screen_width/2) - (window_width/2)) #calcula pos en X
    y_cordinate = int((screen_height/2) - (window_height/2)) #calcula pos en Y

    #ubica la pantalla
    win.geometry("{}x{}+{}+{}".format(
        window_width, window_height, x_cordinate, y_cordinate))

if __name__ == '__main__':
    #crea una ventana y la configura
    win = Tk()
    win.title("Un menu principal y la decisión del siglo")
    win.config(bg = '#313131')
    win.resizable(False, False)
    centrar(win) #la centra

    #imagen y boton de Radar con auto
    photo1 = PhotoImage(file = 'RadarAuto.gif')
    buttonA = Button(win, anchor = 'c',
                     image = photo1,
                     command = lambda: rc.abrirVentana())
    
    buttonA.config(width = 200, height = 200,
                   activebackground = '#313131', 
                   bg = '#1a1a1a', 
                   relief = RAISED)
    #coloca posición en el grid, junto al padding de cada lado
    buttonA.grid(row = 0, column = 1, padx = 48, pady = (75, 10))
    #crea un label
    lab = Label(win, text = 'Probar radar con auto',
                font=("SansSerif", 12), bg = '#313131', fg = "#0892d0")
    #coloca el label debajo del botón que se creo anteriormente
    lab.grid(row = 1, column = 1, padx = 10, pady = 0) 

    #imagen y boton de radar con base de datos
    photo2 = PhotoImage(file = 'RadarData.gif')
    buttonB = Button(win, anchor = 'c',
                     image = photo2,
                     command = lambda: rcbd.abrirVentana())
    
    buttonB.config(width = 200, height = 200,
                   activebackground = '#313131', 
                   bg = '#1a1a1a', 
                   relief = RAISED)
    buttonB.grid(row = 0, column = 2, padx = 48, pady = (75, 10))
    lab2 = Label(win, text = 'Reproducir Base de Datos',
                 font=("SansSerig", 12), bg = '#313131', fg = "#0892d0")
    lab2.grid(row = 1, column = 2, padx = 10, pady = 0)
