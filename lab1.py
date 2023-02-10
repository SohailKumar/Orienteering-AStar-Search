from math import sqrt
from PIL import Image, ImageDraw
import sys

# openL = [[0]*395 for i in range(500)]
# closedL = [[0]*395 for i in range(500)]
elevationL = [[0]*395 for i in range(500)]

class Node:
    x = -1
    y = -1
    w = -1
    h = -1
    g = -1
    parent = -1
    f = -1
    def __init__(self, x, y, goalX, goalY, g, parent):
        self.x = x
        self.y = y
        self.w = elevationL[y][x]                                           #elevation value
        self.h = sqrt((goalX - x)**2 + (goalY - y)**2 + (elevationL[goalY][goalX] - self.w)**2)     #3D Euclidean Distance heuristic value
        self.g = g                                                          #distance from goal
        self.parent = parent
        self.f = self.g + self.w * self.h                                                   
        
    def __str__(self):
        return f'(x: {self.x}, y: {self.y})\n\tw: {self.w}, h(n): {self.h}, g(n): {self.g}, parent: {self.parent}'


def SetupElevationList(elevationFile):
    with open(elevationFile) as elev:
        y = 0
        for line in elev.readlines():
            x = 0
            for m in line.rstrip().split(" "):
                if m == "":
                    continue
                elevationL[y][x] = float(m)
                x+=1
                if(x==395):
                    break
            y+=1
    # To print Elevation:
    # e = 0 
    # for a in elevationL[0]:
    #     print(e, a)
    #     e+=1


def DrawPath(path, imgNew):
    drawNew = ImageDraw.Draw(imgNew)
    i = 0
    for i in range(len(path)-1):
        drawNew.line([(path[i][0], path[i][1]),(path[i+1][0], path[i+1][1])], fill='red', width=1)
    
def Path(node):
    totPath = []
    totPath.append((node.x, node.y))
    while(node.parent is not None):
        totPath.append((node.parent.x, node.parent.y))
        node = node.parent
    return totPath


def GetNeighbors(node, end):
    neighbors = []
    if(node.x >= 0):
        neighbors.append(Node(node.x+1, node.y, end[0], end[1], node.g+10.29, node))
    if(node.x <= 394):
        neighbors.append(Node(node.x-1, node.y, end[0], end[1], node.g+10.29, node))
    if(node.y >= 0):
        neighbors.append(Node(node.x, node.y+1, end[0], end[1], node.g+7.55, node))
    if(node.y <= 499):
        neighbors.append(Node(node.x, node.y-1, end[0], end[1], node.g+7.55, node))
    return neighbors

def AStarSetup(start, end):
    openL = {}
    closedL = {}
    openL[(start[0],start[1])] = Node(start[0], start[1], end[0], end[1], 0, None)
    while len(openL)>0:
        min = 999999999999
        minJ = -1 
        for j in openL: #find smallest f
            # print("J: ", j, ", openL ", openL[j])
            if openL[j].f < min:
                min = openL[j].f
                minJ = j
        
        n = openL[minJ]
        # print("N: ", n, ", type: ", type(n))
        del openL[minJ]
        neighs = GetNeighbors(n, end)
        for i in neighs:
            if i.x == end[0] and i.y == end[1]:
                return Path(i)
            # if openL.setdefault((i.x,i.y)) is not None:
            #     print("TYPE1: ", type(openL[(i.x,i.y)].f))
            #     print("TYE2:", i.f)
            #     print("TYPE3: ", type(closedL[(i.x,i.y)]))
            #     if openL[(i.x,i.y)].f > i.f or closedL[(i.x,i.y)].f > i.f:
            #         openL[(i.x,i.y)] = i
            # else:
            #     openL[(i.x,i.y)] = i
            if (openL.get((i.x,i.y)) is not None and openL[(i.x,i.y)].f < i.f) or (closedL.get((i.x,i.y)) is not None and closedL[(i.x,i.y)].f < i.f):
                continue
            else:
                openL[(i.x,i.y)] = i
        closedL[(i.x,i.y)] = i
    return []
    print("Start: ", start)

if __name__ == "__main__":
    # terrainImage = sys.argv[1]
    # elevationFile = sys.argv[2]
    # pathFile = sys.argv[3]
    # outputImageFileName = sys.argv[4]

    # terrainImage = "terrain.png"
    # elevationFile = "elevation.txt"
    # pathFile = "TestCourses/brown.txt"
    # outputImageFileName = "output.png"

    terrainImage = "testcases/stripElevation/terrain.png"
    elevationFile = "testcases/stripElevation/mpp.txt"
    pathFile = "testcases/stripElevations/path.txt"
    outputImageFileName = "output.png"

    SetupElevationList(elevationFile)

    destinations = []
    with open(pathFile) as f:
        for line in f.readlines():
            destinations.append([int(m) for m in line.split(" ")])

    img = Image.open(terrainImage)
    imgNew = img.copy()
    # print("PATH: ", AStarSetup((0,0),(1,1)))
    for i in range(len(destinations)-1):
        print("Destination", i, destinations[i], "Destination", i+1, destinations[i+1])
        path = AStarSetup(destinations[i], destinations[i+1])
        print("PATH: ", path)
        DrawPath(path,imgNew)
        # imgNew.show()
    imgNew.show()
    


