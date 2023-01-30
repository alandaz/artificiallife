from solution import SOLUTION 
import constants as c
import copy 

class PARALLEL_HILL_CLIMBER: 
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0 
        for x in range(c.populationSize): 
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1 
    
    def Evolve(self):
        for x in range(c.populationSize):
            self.parents[x].Evaluate("GUI")

          #self.parent.Evaluate("GUI")
        #  for x in range(c.numberOfGenerations): 
        #     self.Evolve_For_One_Generation()
    
    def Show_Best(self): 
        pass
        # self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn() 
        self.Mutate()
        self.child.Evaluate("DIRECT") 
        self.Print()
        self.Select()

    def Spawn(self): 
        self.child = copy.deepcopy(self.parent)

    def Mutate(self): 
        self.child.Mutate()

    def Select(self): 
        if self.parent.fitness < self.child.fitness: 
            self.parent = self.child 

    def Print(self): 
        print("parent: ", self.parent.fitness, "child:", self.child.fitness)