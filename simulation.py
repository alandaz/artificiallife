from world import WORLD 
from robot import ROBOT 
import pybullet as p 
import pybullet_data 
import constants as c
import time

class SIMULATION: 
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8) 
        self.world = WORLD()
        self.robot = ROBOT() 

    def Run(self): 
        for x in range(c.iterations): 
            p.stepSimulation() 
            self.robot.Sense(x)
            self.robot.Act(x)
            time.sleep(1/60)

    def __del__(self): 
        p.disconnect()
    

        # for x in range(1000): 
#     p.stepSimulation()
#     backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
#     frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    

#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "torso_frontleg", 
#     controlMode = p.POSITION_CONTROL, targetPosition = frontValuesSin[x], maxForce = 400)

#     time.sleep(1/120) 
#     #print(x)
