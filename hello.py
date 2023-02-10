from math import sqrt
import sys

open = [[0]*295 for i in range(500)]
closed = [[0]*295 for i in range(500)]

class Node:
    def __init__(self, x, y, w, goalX, goalY, goalW):
        self.x = x
        self.y = y
        self.w = w                                                      #elevation value
        self.h = sqrt((goalX - x)**2 + (goalY - y)**2 + (goalW - w)**2)    #3D Euclidean Distance heuristic value
        self.g = None                                                   #distance from goal
        self.parent = None
        
    def __str__(self):
        return f'(x: {self.x}, y: {self.y})\n\tw: {self.w}, h(n): {self.h}, g(n): {self.g}, parent: {self.parent}'

if __name__ == "__main__":
    file = open('simple.txt')