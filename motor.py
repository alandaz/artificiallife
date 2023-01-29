import pyrosim.pyrosim as pyrosim
import pybullet as p 
import constants as c 
import numpy as np

class MOTOR: 
    def __init__(self, jointName): 
        self.jointName = jointName
        #self.Prepare_To_Act()

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, 
        controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForce)

    # def Save_Values(self):
    #     np.save("data/" + self.jointName, self.motorValues)