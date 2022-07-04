from random import randint
TileName = ["Forest","Tree","Medow","Sand","Water"]

ImageList = {
    "Forest" : "src/image/Forest.png",
    "Tree" : "src/image/Tree.png",
    "Medow" : "src/image/Medow.png",
    "Sand" : "src/image/Sand.png",
    "Water" : "src/image/Sea.png"
}

"""====================== Rules ======================"""
    # Forest can go with Tree
    # Tree can go with Forest and Medow
    # Grass can go with Tree and Sand
    # Sand can go with Medow and Water
    # Water can go with Sand
Rules = {
    "Forest" : ["Tree","Forest"],
    "Tree" : ["Forest","Medow","Tree"],
    "Medow" : ["Tree","Sand","Medow"],
    "Sand" : ["Medow","Water","Sand"],
    "Water" : ["Sand","Water"]
}

def isIn(lst,obj):
    for i in range(len(lst)):
        if lst[i] == obj:
            return True
    return False
    

class Tile():
    def __init__(self):
        self.generated = False
        self.possibility = ["Forest","Tree","Medow","Sand","Water"]
    
    def generate(self,number):
        self.typeName = self.possibility[number]
        self.imagePath = ImageList[self.typeName]
        self.possibility = [self.typeName]
        self.generated = True
    
    def updatePossibility(self,adjacent):
        print("Adjacent :",adjacent," | Old : ",self.possibility,end=" ")
        for i in range(len(self.possibility)):
            if not isIn(Rules[adjacent],self.possibility[i]):
                self.possibility[i] = "R"
        print("| new : ",self.possibility,end='')
        while (isIn(self.possibility,"R")):
            self.possibility.remove("R")
        print(" | final : ",self.possibility)

class Map():
    def __init__(self):
        self.map = [[Tile() for i in range(40)]for t in range(23)]

        self.coord = (0,0)
        self.map[self.coord[0]][self.coord[1]].generate(randint(0,4))
        self.updateAdjacent()
    
    def addTile(self):
        if self.coord[0]>=22:
            self.coord = (0,self.coord[1]+1)
        else : 
            self.coord = (self.coord[0]+1,self.coord[1])
        
        #print("coord : ",self.coord)
        random = randint(0,len(self.map[self.coord[0]][self.coord[1]].possibility)-1)
        self.map[self.coord[0]][self.coord[1]].generate(random)
        self.updateAdjacent()
    
    def updateAdjacent(self):
        testCoord = [self.coord[0],self.coord[1]]
        for d in range(-1,2):
            testCoord[0] = testCoord[0]+d
            if (testCoord[0]>0 and testCoord[0]<len(self.map) and (d!=0) and (not self.map[testCoord[0]][testCoord[1]].generated)):
                self.map[testCoord[0]][testCoord[1]].updatePossibility(self.map[self.coord[0]][self.coord[1]].typeName)
            testCoord = [self.coord[0],self.coord[1]]

        for d in range(-1,2):
            testCoord[1] = testCoord[1]+d
            if (testCoord[1]>0 and testCoord[1]<len(self.map[testCoord[0]]) and (d!=0) and (not self.map[testCoord[0]][testCoord[1]].generated)):
                self.map[testCoord[0]][testCoord[1]].updatePossibility(self.map[self.coord[0]][self.coord[1]].typeName)
            testCoord = [self.coord[0],self.coord[1]]
    """
    def updateAdjacent(self):
        testCoord = [self.coord[0],self.coord[1]]
        for l in range(-1,1):
            testCoord[0] = testCoord[0]+l
            if (testCoord[0]>0 and testCoord[0]<len(self.map) and (not self.map[testCoord[0]][testCoord[1]].generated)):
                for h in range(-1,1):
                    testCoord[1] = testCoord[1]+h
                    if (testCoord[1]>0 and testCoord[1]<len(self.map[testCoord[0]]) and (h!=0 and l!=0) and (not self.map[testCoord[0]][testCoord[1]].generated)):
                        self.map[testCoord[0]][testCoord[1]].updatePossibility(self.map[self.coord[0]][self.coord[1]].typeName)
                    testCoord[1] = self.coord[1]
            testCoord[0] = self.coord[0]
    """