# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:51:00 2023

@author: jonat
"""

class RobotView:
    def __init__(self):
        pass
    
    def display_message(self, mensaje):
        print(mensaje)
        print("")
    
    def  get_user_input(self):
        print("DATOS PARA MOVIMIENTO DEL BRAZO")
        rota=input("ROTACION(GRADOS): ")
        elev=input("ELEVACION(GRADOS): ")
        long=input("LONGITUD(cm): ")
        return {"ELEVACION": elev, "ROTACION": rota, "LONGITUD": long}