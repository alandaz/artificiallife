# import pybullet as p 
# import time 
# import pybullet_data 
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import random
# import constants as c 
from simulation import SIMULATION
import sys 

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness() 

# pyrosim.Prepare_To_Simulate(robotId)

# amplitudebackleg = np.pi/4
# frequencybackleg = 10
# phaseOffSetbackleg = 0


# amplitudefrontleg = np.pi/3
# frequencyfrontleg = 11
# phaseOffSetfrontleg = 0

# targetAngles = np.linspace(0, 2*np.pi, 1000)
# backValuesSin = np.linspace(0, 2*np.pi, 1000)
#


# for x in range(1000): 



# print(backLegSensorValues)
# print(frontLegSensorValues)
# np.save("data/backValuesSin", backValuesSin)
# np.save("data/frontValuesSin", frontValuesSin)
# np.save("data/backlegSensorValues", backLegSensorValues)
# np.save("data/frontlegSensorValues", frontLegSensorValues)
# p.disconnect


