from math import sqrt, acos, degrees

class SecStruct:
    
    def __init__(self, stype: str, p1: tuple, p2: tuple) -> None:
        self._stype = stype
        self._p1 = p1
        self._p2 = p2

    def getType(self) -> str:
        return self._stype

    def getP1(self) -> float:
        return self._p1
    
    def getP2(self) -> float:
        return self._p2

    def __str__(self) -> str:
        temp = self._stype
        temp += "\n"
        temp += str(self._p1)
        temp += "\n"
        temp += str(self._p2)
        return temp

"""
    @params: s1, and s2 both SecStruct objects
    @return: the angle between them 
"""
def getAngle(s1 : SecStruct, s2: SecStruct) -> float:
    # find vector representations by translating the segments to be about the origin
    v1 = tuple(x - y for x, y in zip(s1.getP1(), s1.getP2()))
    v2 = tuple(x - y for x, y in zip(s2.getP1(), s2.getP2()))
    x1, y1, z1 = v1 
    x2, y2, z2 = v2 
    # divide dot product by the length of each vector and take arccos to find angle in radians
    dot = x1*x2 + y1*y2 + z1*z2 
    lenv1 = sqrt(x1**2 + y1**2 + z1**2)
    lenv2 = sqrt(x2**2 + y2**2 + z2**2)
    # convert to degrees
    return degrees(acos(dot / (lenv1 * lenv2)))

"""
    @params: s1, s2 both SecStruct objects
    @return: the distance between the midpoints of s1 and s2 in Angstroms
"""
def getStructDist(s1: SecStruct, s2: SecStruct) -> float:
    return getDistance(getMidpoint(s1), getMidpoint(s2))

"""
    @params: s1, a SecStruct object
    @return: the midpoint of s1
"""
def getMidpoint(s1: SecStruct) -> tuple:
    return tuple(sum(x)/2 for x in zip(s1.getP1(), s1.getP2()))

"""
    @params p1, p2 two tuples
    @return: the distance between them
"""
def getDistance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def compareOrientation(s1: SecStruct, s2: SecStruct):
    VALID_DIST = 23 # TODO: find good dist value (probably bruteforce)
    MIXED_MARGIN = 15
    PARALLEL_MARGIN = 25
    
    structDist = getStructDist(s1, s2)
    
    if structDist > VALID_DIST:
        return -1
    
    angleBetween = getAngle(s1, s2)

    if angleBetween < PARALLEL_MARGIN:
        return "PARALLEL"
    elif angleBetween > 90 - MIXED_MARGIN and angleBetween < 90 + MIXED_MARGIN:
        return "MIXED"
    elif angleBetween > 180 - PARALLEL_MARGIN:
        return "ANTIPARALLEL"
    else:
        return "NONE"
