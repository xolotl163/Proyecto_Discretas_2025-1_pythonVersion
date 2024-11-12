
class Trainstation:

    def __init__(self,  
                 name = None, 
                 neighbors = None,
                 predecessor = None, 
                 visitedState: bool = False):
        
        self.name = name
        self.visitedState = visitedState
        self.predecessor = predecessor
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    
    # Getters and Setters
    def get_id(self):
        return self.name
    
    def get_neighbors(self):
        return self.neighbors

    def get_predecessor(self):
        return self.predecessor

    def get_visited_state(self):
        return self.visitedState

    def setName(self, name):
        self.name = name

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    #general methods to the class
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_visited_state(self, visitedState):
        self.visitedState = visitedState

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor