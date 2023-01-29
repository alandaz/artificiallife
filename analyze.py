import numpy as np 
import matplotlib.pyplot as matplot

sinbackpoints = np.load("data/backValuesSin.npy")
sinfrontpoints = np.load("data/frontValuesSin.npy")



matplot.plot(sinbackpoints, label = "Back Leg Data",)
matplot.plot(sinfrontpoints, label = "Front Leg Data")

matplot.legend()
matplot.show()