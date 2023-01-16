import pybullet as p 
import time 
import pybullet_data 
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

amplitudebackleg = np.pi/3
frequencybackleg = 10
phaseOffSetbackleg = 0

amplitudefrontleg = np.pi/4
frequencyfrontleg = 11
phaseOffSetfrontleg = 0

targetAngles = np.linspace(0, 2*np.pi, 1000)
backValuesSin = np.linspace(0, 2*np.pi, 1000)
frontValuesSin = np.linspace(0, 2*np.pi, 1000)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for x in range(1000): 
    backValuesSin[x] = amplitudebackleg * np.sin(frequencybackleg * targetAngles[x] + phaseOffSetbackleg)
    frontValuesSin[x] = amplitudefrontleg * np.sin(frequencyfrontleg * targetAngles[x] + phaseOffSetfrontleg)

for x in range(1000): 
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "torso_backleg", 
    controlMode = p.POSITION_CONTROL, targetPosition = backValuesSin[x], maxForce = 25)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "torso_frontleg", 
    controlMode = p.POSITION_CONTROL, targetPosition = frontValuesSin[x], maxForce = 25)

    time.sleep(1/240) 
    #print(x)
print(backLegSensorValues)
print(frontLegSensorValues)
np.save("data/backValuesSin", backValuesSin)
np.save("data/frontValuesSin", frontValuesSin)
np.save("data/backlegSensorValues", backLegSensorValues)
np.save("data/frontlegSensorValues", frontLegSensorValues)
p.disconnect


