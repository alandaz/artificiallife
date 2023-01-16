import numpy as np 
import matplotlib.pyplot as matplot

# backpoints = np.load("data/backlegSensorValues.npy")
# frontpoints = np.load("data/frontlegSensorValues.npy")
sinbackpoints = np.load("data/backValuesSin.npy")
sinfrontpoints = np.load("data/frontValuesSin.npy")

# print(backpoints)
# print('hi')
# print(frontpoints)

matplot.plot(sinbackpoints, label = "Back Leg Data",)
matplot.plot(sinfrontpoints, label = "Front Leg Data")

matplot.legend()
matplot.show()