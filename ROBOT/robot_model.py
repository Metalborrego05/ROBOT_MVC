# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:52:21 2023

@author: jonat
"""

class RobotModel:
    def __init__(self):
        self.posicion = {"ELEVACION": 0, "ROTACION": 0, "LONGITUD": 0}
    
    def move_elevation(self,elev):
        self.posicion["ELEVACION"]=elev
        return self.posicion["ELEVACION"]
    
    def move_rotation(self,rota):
        self.posicion["ROTACION"]=rota
        return self.posicion["ROTACION"]
        
    def move_length(self,long):
        self.posicion["LONGITUD"]=long
        return self.posicion["LONGITUD"]
    
    def stop_movement(self):
        print("El brazo detuvo su moviento!!")
        self.posicion = {"ELEVACION": 0, "ROTACION": 0, "LONGITUD": 0}
        