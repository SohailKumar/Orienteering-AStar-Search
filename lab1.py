from math import sqrt
import sys

openL = [[0]*395 for i in range(500)]
closedL = [[0]*395 for i in range(500)]
elevationL = [[0]*395 for i in range(500)]

class Node:
    def __init__(self, x, y, goalX, goalY):
        self.x = x
        self.y = y
        self.w = elevationL[y][x]                                           #elevation value
        self.h = sqrt((goalX - x)**2 + (goalY - y)**2 + (elevationL[goalY][goalX] - self.w)**2)     #3D Euclidean Distance heuristic value
        self.g = None                                                       #distance from goal
        self.parent = None
        
    def __str__(self):
        return f'(x: {self.x}, y: {self.y})\n\tw: {self.w}, h(n): {self.h}, g(n): {self.g}, parent: {self.parent}'


def setupElevation(elevationFile):
    with open(elevationFile) as elev:
        y = 0
        for line in elev.readlines():
            x = 0
            for m in line.rstrip().split("   "):
                if m == "":
                    continue
                elevationL[y][x] = float(m)
                x+=1
                if(x==395):
                    break
            y+=1
    # To print Elevation:
    e = 0 
    for a in elevationL[0]:
        print(e, a)
        e+=1


def aStarSetup(start, end):
    start = Node(start[0], start[1], end[0], end[1])
    print("Start: ", start)

if __name__ == "__main__":
    # terrainImage = sys.argv[1]
    # elevationFile = sys.argv[2]
    # pathFile = sys.argv[3]
    # outputImageFileName = sys.argv[4]
    terrainImage = "terrain.png"
    elevationFile = "elevation.txt"
    pathFile = "TestCourses/simple.txt"
    outputImageFileName = "output.png"

    setupElevation(elevationFile)

    with open(pathFile) as f:
        start = [int(m) for m in f.readline().split(" ")]
        end = [int(l) for l in f.readline().split(" ")]
    aStarSetup((0,0),(1,1))

