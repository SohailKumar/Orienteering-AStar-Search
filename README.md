# Orienteering-AStar-Search


This program calculates the most optimal path through a given set of points for
a given image describing terrain taking into account the elevation of the land
(also passed into the program).

It uses a Weighted A* Search to find this path:
COST: 
    The cost of going from one pixel to the next is calculated using the
    following formula:
    cost = distance from parent pixel * terrain weight value
    eg. cost from footpath to a walk-forest pixel to the right would be:
    
    The total cost of a pixel is calculated as follows:
    totalCost = parent cost + distance from parent pixel * terrain weight 

    The terrain weights are given as follows:
    Out of Bounds = 9999999999
    Footpath = 1
    Paved Road = 2
    Lake/Swamp/Marsh = 20
    Impassible Vegeation = 10
    Walk Forest = 7
    Slow Run Forest = 5
    Easy Movement Forest = 4
    Rough Meadow = 6
    Open Land = 3
    

HEURISTIC:
    The heuristic function used by the Weighted A* Search is the 3D Euclidean
    Distance from the pixel to the goal:
    pixel heuristic = 
        sqrt(   (goalX - currX)**2 + (goalY - currY)**2 + 
                (elevation of goal pixel - elevation of current pixel)**2   )
    
    This heuristic is *admissible* because the most ideal path from the current
    pixel to the goal pixel is a straight path. There can be no path shorter
    than one that goes straight from the current pixel to the goal. All paths
    will either be the same or be longer since there are elevation changes which
    inherently increase path length or there are terrain changes which make
    certain paths more inefficient due to the "cost" of using them.

    This heuristic is also *consistent* because the cost of going from one pixel
    to another plus the cost of going from that pixel to the goal will always be
    less than or equal to the cost of going from the first pixel to the goal.
    That is just inherent in the nature of the formula. 

