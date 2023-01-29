from world import WORLD 
from robot import ROBOT 
import pybullet as p 
import pybullet_data 
import constants as c
import time

class SIMULATION: 
    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else: 
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8) 
        self.world = WORLD()
        self.robot = ROBOT() 

    def Get_Fitness(self): 
        self.robot.Get_Fitness()

    def Run(self): 
        for x in range(c.iterations): 
            p.stepSimulation() 
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act()
            #time.sleep(1/100)

    def __del__(self): 
        p.disconnect()
    
