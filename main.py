from prody import pathPDBFolder
from readscope import readScope
from createDomain import createDomain
from Domain import genGraph, Domain
from SecStruct import getAngle, getStructDist

def printList(list):
	for l in list:
		print(l)


def main():
	pathPDBFolder('./pdb_archive') # sets folder for PDB files to be downloaded to 
	filename = './dir.des.scope.2.07-stable copy.txt' # directory of domain descriptions
	pClass = 'a' # all alpha proteins

	domainList = readScope(filename, pClass)
	domain = createDomain(domainList[3])
	printList(genGraph(domain))
	# structs = domain.getStructs()

	# print(getStructDist(structs[1], structs[4]))
		

if __name__ == '__main__':
	main()
