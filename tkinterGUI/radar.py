# -*- coding: utf-8 -*-
"""
main.py
Creado el dia Jueves 27 de Junio a las 17:53:46 2019

@author: Alejandro Galindo, Francisco Felix, Alberto Grajeda

Modulo que lee el puerto serie constantemente para generar una salida en un 
radar gráfico utilizando tkinter y modulos propios.
"""

from tkinter import *
from tkinter import messagebox
import math
import drawer as tz
import time
import search as sc
import serial as sl
import re

#crea conexión con el puerto serie
arduino = sl.Serial('COM3', 9600, timeout = 1)
#variable global booleana para saber si se guardan los datos o no
noDatos = False 
#obtiene el ID actual de la base de datos
idRastreo = sc.obtenerRastreo()

#En caso de que la BD esté vacia
if idRastreo == None:
    idRastreo = 1
    print(str(idRastreo))
else:
    idRastreo = idRastreo + 1
    print(str(idRastreo))

def centrar(win):
    """
    Metodo que centra el frame en el centro de la pantalla de la computadora
    """
    window_width = 1200 #ancho del frame
    window_height = 700 #alto del frame
    
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) #ubica la pantalla

def leePuertoSerie(win, canvas, regex, noDatos):
    """
    Metodo que lee el puerto serie y dibuja un rectángulo en la ubicación leida por un sensor ultrasonico
    """
    angulo = distancia = 0
    scan = arduino.readline() #lee una linea, la decodifica y quita los saltos de linea
    scan = scan.decode("utf-8")
    scan = scan.replace("\r\n", "")

    #si la linea corresponde a un escaneo
    if scan == "scan":
        angulo = arduino.readline() #lee el angulo
        distancia = arduino.readline() #lee la distancia
        angulo = angulo.decode("utf-8")
        distancia = distancia.decode("utf-8")
        angulo = angulo.replace("\r\n", "")
        distancia = distancia.replace("\r\n", "")

        #si ambas distancias son valores enteros según un regex
        if regex.match(angulo) and regex.match(distancia):
            if distancia != 0:
                if int(angulo) == 45:
                    canvas.delete("punto", "rect")

                lista = []
                #print(str(angulo))
                #print(str(distancia))
                C = (600, 650)
                #print(C)
                B = tz.encuentraPuntoB(C, (int(distancia)*10), int(angulo))
                #print(B)
                #F = tz.encuentraPuntoB(B, 600 - (int(distancia)*10), int(angulo))
                #print(F)
                #tz.trazaLinea(canvas, C, B, "#0892d0", "linea")
                #tz.trazaLinea(canvas, B, F, "#ff4e4e", "linea")
                #tz.dibujaPunto(canvas, B, "#0892d0")
                tz.dibujaRectangulo(canvas, B, int(distancia), "#ff4e4e")

                if noDatos:
                    tupla = (B[0], B[1], int(angulo), int(distancia))
                    lista.append(tupla)
                    sc.insertarPoints(lista, idRastreo)
                    
    win.after(1, lambda: leePuertoSerie(win, canvas, regex, noDatos))

def abrirVentana():
    win = Tk() #Crea la ventana
    win.title("Un radar, un carro con joystick y el Arduino UNO") #asigna un titulo
    win.resizable(False, False) #impide que sea reescalada
    centrar(win) #la centra

    canvas = Canvas(win) #crea el canvas donde va el radar
    canvas.config(width = 1200, height = 650, bg = '#1a1a1a') #llama al metodo config() y configura las option width, height y bg
    canvas.pack(side = 'top', anchor = 'n', fill = 'x') #asigna el canvas al frame win, y configura las option side, anchor y fill
    tz.dibujarCanvasRadar(canvas, "#0892d0") #Usa el modulo trazador

    box = messagebox.askyesno("Aviso de Información", "¿Desea guardar información en la Base de Datos?")
    noDatos = box

    r = re.compile("^\d\S*$") #regex para numeros enteros
    A = (600, 650) #centro del canvas

    #Aqui NO va un while que lea en Serial constantemente
    leePuertoSerie(win, canvas, r, noDatos)
    
    win.mainloop()

if __name__ == '__main__':
    win = Tk() #Crea la ventana
    win.title("Un radar, un carro con joystick y el Arduino UNO") #asigna un titulo
    win.resizable(False, False) #impide que sea reescalada
    centrar(win) #la centra

    canvas = Canvas(win) #crea el canvas donde va el radar
    canvas.config(width = 1200, height = 650, bg = '#1a1a1a') #llama al metodo config() y configura las option width, height y bg
    canvas.pack(side = 'top', anchor = 'n', fill = 'x') #asigna el canvas al frame win, y configura las option side, anchor y fill
    tz.dibujarCanvasRadar(canvas, "#0892d0") #Usa el modulo trazador

    box = messagebox.askyesno("Aviso de Información", "¿Desea guardar información en la Base de Datos?")
    noDatos = box

    r = re.compile("^\d\S*$") #regex para numeros enteros
    A = (600, 650) #centro del canvas

    #Aqui NO va un while que lea en Serial constantemente
    leePuertoSerie(win, canvas, r,  noDatos)
    
    win.mainloop()


