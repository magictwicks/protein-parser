from SecStruct import SecStruct, compareOrientation

class Domain:
    
    def __init__(self, pdbid: str, domain: str, chain: str, range, structs: SecStruct) -> None:
        self._pdbid = pdbid
        self._domain = domain
        self._range = range
        self._structs = structs
        
    def size(self) -> int:
        return len(self._structs)
    
    # getters 
    def getPDBId(self) -> str:
        return self._pdbid 
    
    def getDomain(self) -> str:
        return self._domain
    
    def getRange(self):
        return self._range
    
    def getStructs(self) -> list:
        return self._structs
    
# TODO: implement generateGraph() function which will take a domain and generate a graph based on the structures in that graph

def genGraph(dom: Domain):
    size = dom.size()
    graphMat = [['0' for j in range(size)] for i in range(size)] # create a 2d array
    structs = dom.getStructs()

    # compare every SecStruct to each other
    for i in range(size):
        for j in range(size):
            if structs[i] != structs[j]: # don't compare the same SecStruct objects
                match compareOrientation(structs[i], structs[j]):
                    case "ANTIPARALLEL":
                        graphMat[i][j] = 'A'
                    case "PARALLEL":
                        graphMat[i][j] = 'P'
                    case "MIXED":
                        graphMat[i][j] = 'M'
    
    return graphMat