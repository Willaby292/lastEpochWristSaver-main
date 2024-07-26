
from Node import *
from Direction import Direction
import math

def findNeighbors(currPlace, POI): #this can be never nested
    x = POI[currPlace].getX()
    y = POI[currPlace].getY()

    distOldNorthNeighbor = float('inf')
    distOldSouthNeighbor = float('inf')
    distOldEastNeighbor = float('inf')
    distOldWestNeighbor = float('inf')

    slopeC = 100 #no idea what i want this to be

    for place in POI: #TODO// handle overlapping neighbor regions
        dx = POI[place].getX() - x
        dy = POI[place].getY() - y
        if dx != 0 and dy != 0:
            if abs(dx) < math.log10(abs(dy) + 1) * slopeC:
                if dy < 0:
                    if distOldNorthNeighbor < abs(dy):
                        break
                    POI[currPlace].setNeighbor(place, Direction.UP)
                    distOldNorthNeighbor = abs(dy)
                else:
                    if distOldSouthNeighbor < dy:
                        break
                    POI[currPlace].setNeighbor(place, Direction.DOWN)
                    distOldSouthNeighbor = abs(dy)
            elif abs(dy) < math.log10(abs(dx) + 1) * slopeC:
                if dx < 0:
                    if distOldWestNeighbor < abs(dx):
                        break
                    POI[currPlace].setNeighbor(place, Direction.LEFT)
                    distOldWestNeighbor = abs(dx)
                else:
                    if distOldEastNeighbor < dx:
                        break
                    distOldEastNeighbor = dx
                    POI[currPlace].setNeighbor(place, Direction.RIGHT)


def buildGraph(POI):
    for place in POI:
        findNeighbors(place, POI)
    return POI

def createNodePOI(POI) -> dict:
    nodePOI = {}
    for count, node in enumerate(POI):
        nodePOI[count] = Node(node.get('x'), node.get('y'))
    return nodePOI

class Graph:
    def __init__(self, POI: list):
        nodePOI = createNodePOI(POI)
        self.graph = buildGraph(nodePOI)

    def getGraph(self):
        return self.graph