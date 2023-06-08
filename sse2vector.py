from prody import parsePDB
from SecStruct import SecStruct

# TODO: eventually use helix strand information to classify chirality, and maybe more information
def sse2vector(pdbid, sse) -> SecStruct:
    atomGroup = parsePDB(pdbid)
    
    TYPE = sse[0]
    CHAIN = sse[1]
    RES_START = sse[4]
    RES_END = sse[5]
    
    # calculate 3d position of beginning of structure
    coordSet1 = atomGroup[CHAIN, RES_START].getCoords() # this returns the coords from the residue RES_START in CHAIN 
    coord1 = tuple([round(sum(axis)/len(axis), 4) for axis in zip(*coordSet1)]) # calculates the average of the coordset

    coordSet2 = atomGroup[CHAIN, RES_END].getCoords()
    coord2 = tuple([round(sum(axis)/len(axis), 4) for axis in zip(*coordSet2)])

    structure = SecStruct(TYPE, coord1, coord2)

    return structure
    