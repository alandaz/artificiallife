
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name = "Box", pos = [0,0,0.5], size = [1,1,1])
pyrosim.End() 


Create_World() 
Create_Robot() 