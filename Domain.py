import SecStruct

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
    
