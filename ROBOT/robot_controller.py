# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:52:05 2023

@author: jonat
"""

class RobotController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        
    def run(self):
        while True:
            self.view.display_message("""mover
detener
salir""")
            self.view.display_message("Ingrese un comando:")
            comando = input().lower()
            if comando == "mover":
                self.mover_robot()
            elif comando == "detener":
                self.detener_robot()
            elif comando == "salir":
                break
            else:
                self.view.display_message("Comando no válido")
            
    def mover_robot(self):
        entrada_usuario = self.view.get_user_input()
        elevacion = float(entrada_usuario["ELEVACION"])
        giro = float(entrada_usuario["ROTACION"])
        longitud = float(entrada_usuario["LONGITUD"])
        self.model.move_elevation(elevacion)
        self.model.move_rotation(giro)
        self.model.move_length(longitud)
        
    def detener_robot(self):
        self.model.stop_movement()