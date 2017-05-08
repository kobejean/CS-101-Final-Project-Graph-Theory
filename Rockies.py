############################################################################
#                            Mountain                                      #
#                                                                          #
#   Programmed by Gabriela Rivera (10-30-2015)                             #
#                                                                          #
#   Description: This is scenery of a mountain.                            #
#                                                                          #
############################################################################
from tkinter import *

def mountain_scenery(c):
    c.create_rectangle(0,0, 410,410, fill="lightskyblue")
    c.create_oval(200,25, 300,125, fill="gray93", outline="gray93")
    c.create_polygon(0,275, 410,270,410,260, 410,105, 350,100, 335,130, 325,125, 320,127, 300,160, 290,160, 280,155, 275,165, 265,165, 255,185, 240,180, 225,190, 215,185, 215,200, 175,175, 160,185, 130,145, 125,150, 115,130, 100,125, 75,85, 50,120, 25,100, 0,125, 1,260, 0,275, fill="dimgray")
    c.create_polygon(75,85, 50,120, 25,100, 30,125, 50,150, 55,130, 75,140, 90,150, 75,115, 70,100, 75,85, fill="white")
    c.create_polygon(125,150, 115,130, 100,125, 103,135, 115,150, 120,160, 125,175, 130,160, 125,150, fill="white")
    c.create_polygon(175,175, 160,185, 175,200, fill="white")
    c.create_polygon(320,127, 300,160, 290,160, 280,155, 285,170, 284,190, 275,210, 310,180, 315,160, 325,135, 320,127, fill="white")
    c.create_line(90,150, 105,170, 125,185, 150,225, 175,220, 200,235, 240,260, smooth=1, fill="white")
    c.create_line(275,210, 265,215, 255,235, 245,245, 232,260, smooth=1, fill="white")
    c.create_rectangle(0,275, 410,410, fill="SpringGreen3")
    c.create_polygon(0,275, 410,270, 410,260, 410,325, 350,350, 290,370, 250,380, 225,375, 150,375, 115,350, 85,315, 40,300, 0,290, 0,260, 0,275, smooth=1, fill="deepskyblue") 
    c.create_polygon(0,275, 410,275, 410,272, 410,260, 300,260, 240,255, 185,265, 150,257, 120,262, 75,260, 55,250, 25,255, 0,260, 0,272, smooth=1, fill="SpringGreen4") 
    c.create_polygon(0,275, 410,275, 410,277, 410,290, 300,290, 240,295, 185,285, 150,293, 120,288, 75,290, 55,300, 25,295, 0,290, 0,277, smooth=1, fill="DeepSkyBlue3") 
    c.create_line(0,275, 410,275, width=2,fill='white')

