# -*- coding: utf-8 -*-
"""
main.py
Creado el dia Jueves 27 de Junio a las 17:53:46 2019

@author: Alejandro Galindo, Francisco Felix, Alberto Grajeda

Modulo que despliega una interfaz de radar para iniciar una animación del
contenido de la Base De Datos
"""

from tkinter import *
from tkinter import ttk
import math
import drawer as tz
import time
import search as sc

animation = False #variable global para parar animación
rastreos = sc.obtenerIDsRastreo() #Consulta DB

def centrar(win):
    """
    Metodo que centra el frame en el centro de la pantalla de la computadora
    """
    window_width = 1200
    window_height = 700 #460
    
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    
    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def prepareDBToPlay(win, canvas, combo):
    """
    Metodo que prepara la base de datos para ser reproducida
    """
    global animation
    animation = True
    global rastreos
    index = combo.current()
    if index == -1:
        return
    index = index + 1
    canvas.delete("rect")
    i = 45
    points = sc.obtenerPoints(index)
    lista = []

    for j in points:
        lista.append(j)

    playDB(win, canvas, i, lista)

def playDB(win, canvas, i, points):
    """
    Metodo que reproduce la Base de datos de manera iterativa con el metodo
    after() de Tk
    """
    
    #si la animación debe suceder
    if animation: 
        C = (600, 650) #centro del canvas
        B = tz.encuentraPuntoB((600, 650), 1200/2, i)
        if B == None:
            if len(points) > 0:
                canvas.delete("rect")
                canvas.update()
                i = 40
            else:
                return
        else:
            if len(points) > 0:
                P = (int(points[0][1]), int(points[0][2])) #punto a animar
                #tz.trazaLinea(canvas, C, P, "#0892d0", "lineaRadar")
                #tz.trazaLinea(canvas, P, B, "#ff4e4e", "lineaRadar")
                #tz.dibujaPunto(canvas, P, "#0892d0")
                #dibuja rectangulo
                tz.dibujaRectangulo(canvas, P, int(points[0][4]), "#ff4e4e")
                del points[0]
        i = i + 5   
        win.after(80, lambda: playDB(win, canvas, i, points))

def pararAnimacion():
    """
    Metodo que cambia el estado de animation
    """
    global animation
    animation = False

def abrirVentana():
    """
    Metodo que inicializa y abre la ventana
    """
    win = Toplevel()
    win.title("Un radar, un carro con joystick y SQLSERVER")
    win.resizable(False, False)
    centrar(win)

    rastreos = sc.obtenerIDsRastreo()

    canvas = Canvas(win)
    canvas.config(width = 1200, height = 650, bg = '#1a1a1a')
    canvas.pack(side = 'top', anchor = 'n', fill = 'x')
    tz.dibujarCanvasRadar(canvas, "#0892d0")

    canvas2 = Canvas(win)
    canvas2.config(width = 1200, height = 40, bg = '#1a1a1a')
    canvas2.pack(side = 'bottom', anchor = 's', fill = 'both')

    photo = PhotoImage(file = 'play.gif')

    textF = ('SansSerif', '16', "bold")
    combo = ttk.Combobox(win, state = "readonly", font = textF)
    combo.configure(width = 20, height = 20)
    combo["values"] = rastreos
    combo_window = canvas2.create_window(100, 0, anchor = 'nw', window = combo)
    
    button = Button(win, anchor = 'nw',
                    image = photo,
                    command = lambda:
                    prepareDBToPlay(win, canvas, combo))
    button.configure(width = 40, height = 40, activebackground = "#bababa", relief = RAISED)
    button_window = canvas2.create_window(0, 0, anchor = 'nw', window = button)

    photo2 = PhotoImage(file = 'stop.gif')

    button2 = Button(win, text = 'Stop', anchor = 'nw',
                    image = photo2,
                    command = lambda:
                    pararAnimacion())
    button2.configure(width = 40, height = 40, activebackground = "#bababa", relief = RAISED)
    button_window = canvas2.create_window(50, 0, anchor = 'nw', window = button2)
    
    win.mainloop()
    
if __name__ == '__main__':
    win = Tk()
    win.title("Un radar, un carro con joystick y SQLSERVER")
    win.resizable(False, False)
    centrar(win)

    canvas = Canvas(win)
    canvas.config(width = 1200, height = 650, bg = '#1a1a1a')
    canvas.pack(side = 'top', anchor = 'n', fill = 'x')
    tz.dibujarCanvasRadar(canvas, "#0892d0")

    canvas2 = Canvas(win)
    canvas2.config(width = 1200, height = 40, bg = '#1a1a1a')
    canvas2.pack(side = 'bottom', anchor = 's', fill = 'both')

    photo = PhotoImage(file = 'play.gif')

    combo = ttk.Combobox(win, state = "readonly")
    combo.configure(width = 20, height = 20)
    combo["values"] = rastreos
    combo_window = canvas2.create_window(100, 0, anchor = 'nw', window = combo)
    
    button = Button(win, anchor = 'nw',
                    image = photo,
                    command = lambda:
                    prepareDBToPlay(win, canvas, combo))
    button.configure(width = 40, height = 40, activebackground = "#bababa", relief = RAISED)
    button_window = canvas2.create_window(0, 0, anchor = 'nw', window = button)

    photo2 = PhotoImage(file = 'stop.gif')

    button2 = Button(win, text = 'Stop', anchor = 'nw',
                    image = photo2,
                    command = lambda:
                    pararAnimacion())
    button2.configure(width = 40, height = 40, activebackground = "#bababa", relief = RAISED)
    button_window = canvas2.create_window(50, 0, anchor = 'nw', window = button2)

    win.mainloop()








