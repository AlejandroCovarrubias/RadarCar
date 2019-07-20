# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:53:46 2019

@author: Alejandro Galindo
"""

from tkinter import *
import math

def dibujarCanvasRadar(canvas, rgbHexa):
    """
    Metodo que dibuja un radar en un canvas de dimensiones 1200, 650 
    con un color asignado en sus parametros.
    """
    centro = (600, 650) #centro del canvas
    #traza lineas divisoras de angulos
    trazaLinea(canvas, centro, encuentraPuntoB(centro, 600 + 10, 45), 
               rgbHexa, "45") 
    trazaLinea(canvas, centro, encuentraPuntoB(centro, 600 + 10, 135), 
               rgbHexa, "135")
    trazaLinea(canvas, centro, encuentraPuntoB(centro, 600 + 10, 90), 
               rgbHexa, "90")

    #traza los arcos y escribe distancias
    for i in range(0, 6 + 1):
        creaArco(canvas, (i*(600/6),650), (1200-(i*(600/6)),650), rgbHexa)
        if i != 6:
            canvas.create_text((i*(600/6)) + 30, 650 - 15, 
                               text = str(int((60-(i*10)))) + 'cm',
                           font = ("SansSerif", 12, "bold"), fill = rgbHexa)
            canvas.create_text(1200-(i*(600/6)) - 30, 650 - 15, 
                               text = str(int((60-(i*10)))) + 'cm',
                           font = ("SansSerif", 12, "bold"), fill = rgbHexa)

    #asigna angulos en la parte superior del radar
    for i in range(0, 18 + 1):
        canvas.create_text(encuentraPuntoB(centro, 600 + 20, (45 + 5*i)), 
                           text = str((45 + 5*i)) + 'º',
                           font = ("SansSerif", 12, "bold"), fill = rgbHexa)
    canvas.update()

def creaArco(canvas, p0, p1, rgbHexa):
    """
    Metodo que crea un arco segun un canvas dado, un punto inicial y un punto 
    final con un color dado.
    """
    x = (distancia(p0,p1) -(p1[0]-p0[0]))/2 
    y = (distancia(p0,p1) -(p1[1]-p0[1]))/2
    angulo = math.atan2(p0[0] - p1[0], p0[1] - p1[1]) *180 / math.pi   
    canvas.create_arc(p0[0]-x, p0[1]-y, p1[0]+x, p1[1]+y, 
                      extent=180, start=90+angulo, style= "arc", 
                      outline = rgbHexa, width = 1)

def distancia(p0, p1):
    """
    Metodo que calcula la distancia entre dos puntos
    """
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def encuentraPuntoB(A, distancia, angulo):
    """
    Metodo que utiliza principios del teorema de pitagoras para encontrar un 
    punto B segun A, una distancia y un angulo.
    Retorna valores convenientes para un sistema coordenado totalmente 
    positivo y ubicado en el 4to cuadrante.
    """
    x0 = math.cos(math.radians(angulo+180))*distancia
    y0 = math.sin(math.radians(angulo+180))*distancia

    if(angulo >= 45 and angulo < 90):
        return (A[0]-x0, A[1]+y0)
    elif(angulo > 90 and angulo <= 135):
        return (A[0]-x0, A[1]+y0)
    elif (angulo == 90):
        return (A[0]+x0, A[1]+y0)

def dibujaPunto(canvas, C, rgbHexa):
    """
    Metodo que dibuja un punto en un canvas dado, segun unas coordenadas 
    y un color dado.
    """
    punto = canvas.create_oval(C[0]-6, C[1]-6, C[0]+6, C[1]+6, 
                               fill = rgbHexa, outline = rgbHexa, tag = "punto")
    canvas.update()
    return punto

def dibujaRectangulo(canvas, C, rango, rgbHexa):
    """
    Metodo que dibuja un rectángulo en un canvas dado, según unas 
    coordenadas y un color dado.    
    """
    rangox = rangoy = 0
    if rango >= 1 and rango < 20:
        rangox = 15
        rangoy = 3
    elif rango >= 20 and rango < 40:
        rangox = 20
        rangoy = 7
    elif rango >= 40 and rango <= 60:
        rangox = 25
        rangoy = 10
        
    rectangulo = canvas.create_rectangle(C[0] - rangox, C[1] - rangoy, 
                                         C[0] + rangox, C[1] + rangoy, 
                                         fill = rgbHexa, outline = rgbHexa, 
                                         tag = "rect")
    canvas.update()
    return rectangulo

def trazaLinea(canvas, A, B, rgbHexa, etiqueta):
    """
    Metodo que traza una linea en un canvas dado, según un punto A, 
    un punto B, un color y una etiqueta.
    """
    linea = canvas.create_line(A[0], A[1], B[0], B[1], 
                               tag = etiqueta, fill = rgbHexa, width = 2)
    canvas.update()
    return linea
