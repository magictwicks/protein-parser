from prody import parsePDBHeader, parsePDB
from sse2vector import sse2vector
from Domain import Domain
from SecStruct import SecStruct

# function just checks if two numbers are in a given range (tuple): TODO: implement multiple chain/neg range
def inrange(a, b, range):
    if range == -1:
        return True
    elif a >= range[0] and b <= range[1]:
        return True
    return False

def createDomain(domain_entry) -> Domain:
    """
        This function takes in a domain_entry dictionary 
    """
    PDBID = domain_entry['pdbid']
    DOMAIN_NAME = domain_entry['domain_name'] 
    CHAIN = domain_entry['chain']
    RANGE = domain_entry.get('range', -1) 

    # grab atom group and header from wwPDB
    atomGroup = parsePDB(PDBID)
    helix_list = parsePDBHeader(PDBID, 'helix_range')

    # check if
    structs = []
    for h in helix_list:
        if h[1] == CHAIN and inrange(h[4], h[5], RANGE):
            TYPE = h[0]
            CHAIN = h[1]
            RES_START = h[4]
            RES_END = h[5]
            
            # calculate 3d position of beginning of structure
            coordSet1 = atomGroup[CHAIN, RES_START].getCoords() # this returns the coords from the residue RES_START in CHAIN 
            coord1 = tuple([round(sum(axis)/len(axis), 4) for axis in zip(*coordSet1)]) # calculates the average of the coordset

            coordSet2 = atomGroup[CHAIN, RES_END].getCoords()
            coord2 = tuple([round(sum(axis)/len(axis), 4) for axis in zip(*coordSet2)])

            structure = SecStruct(TYPE, coord1, coord2)
            structs.append(structure)
    

    domain = Domain(PDBID, DOMAIN_NAME, CHAIN, RANGE, structs)
    return domain


    