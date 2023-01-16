import numpy as np 
import matplotlib.pyplot as matplot

backpoints = np.load("data/backlegSensorValues.npy")
frontpoints = np.load("data/frontlegSensorValues.npy")

print(backpoints)
print('hi')
print(frontpoints)

matplot.plot(backpoints, label = "Back Leg Data", linewidth = 4)
matplot.plot(frontpoints, label = "Front Leg Data")

matplot.legend()
matplot.show()