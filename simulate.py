import pybullet as p 
import time 
import pybullet_data 
import pyrosim.pyrosim as pyrosim
import numpy as np 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)
for x in range(500): 
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("backleg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontleg")
    time.sleep(1/60) 
    #print(x)
print(backLegSensorValues)
np.save("data/backlegSensorValues", backLegSensorValues)
np.save("data/frontlegSensorValues", frontLegSensorValues)
p.disconnect