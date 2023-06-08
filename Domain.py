import SecStruct

class Domain:
    
    def __init__(self, pdbid: str, domain: str, structs: SecStruct) -> None:
        self._pdbid = pdbid
        self._domain = domain
        self._structs = structs
    
    def size(self) -> int:
        return len(self._structs)