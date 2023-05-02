# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:52:51 2023

@author: jonat
"""

from robot_model import RobotModel
from robot_view import RobotView
from robot_controller import RobotController

model = RobotModel()
view = RobotView()
controller = RobotController(model, view)

#view.set_controller(controller)

controller.run()