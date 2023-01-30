from solution import SOLUTION 
import constants as c
import copy 
import os

class PARALLEL_HILL_CLIMBER: 
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0 
        for x in range(c.populationSize): 
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1 
    
    def Evolve(self): 
        self.Evaluate(self.parents)
        for x in range(c.numberOfGenerations): 
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        for x in solutions: 
            solutions[x].Start_Simulation("DIRECT")
        for y in solutions: 
            solutions[y].Wait_For_Simulation_To_End()
    
    def Show_Best(self): 
        lowest = 0 
        for x in self.parents: 
            if self.parents[x].fitness < self.parents[lowest].fitness: 
                lowest = x
        self.parents[lowest].Start_Simulation("GUI")

    def Evolve_For_One_Generation(self):
         self.Spawn() 
         self.Mutate()
         self.Evaluate(self.children) 
         self.Print()
         self.Select()

    def Spawn(self): 
        self.children = {}
        for x in self.parents.keys(): 
            self.children[x] = copy.deepcopy(self.parents[x])
            self.children[x].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for x in self.children: 
            self.children[x].Mutate() 
        #self.child.Mutate()

    def Select(self): 
        for x in self.parents: 
            if self.parents[x].fitness > self.children[x].fitness: 
                self.parents[x] = self.children[x]

    def Print(self): 
        for x in self.parents.keys(): 
            print("parent: ", self.parents[x].fitness, 
            "child: ", self.children[x].fitness)