from prody import parsePDBHeader, parsePDB
from sse2vector import sse2vector

# function just checks if two numbers are in a given range (tuple): TODO: implement multiple chain/neg range
def inrange(a, b, range):
    if range == -1:
        return True
    elif a >= range[0] and b <= range[1]:
        return True
    return False

def hcount(domain_entry):
    """
        This function takes in a domain_entry dictionary 
    """
    PDBID = domain_entry['pdbid']
    CHAIN = domain_entry['chain']
    RANGE = domain_entry.get('range', -1) 

    # grab header from wwPDB
    helix_list = parsePDBHeader(PDBID, 'helix_range')

    domain_helices = []
    for h in helix_list:
        if h[1] == CHAIN and inrange(h[4], h[5], RANGE):
            domain_helices.append(h)

    return domain_helices


    