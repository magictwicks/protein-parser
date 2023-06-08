from prody import pathPDBFolder
from readscope import readScope
from createDomain import createDomain
from sse2vector import sse2vector
from SecStruct import getAngle, compareOrientation

def main():
	pathPDBFolder('./pdb_archive') # sets folder for PDB files to be downloaded to 
	filename = './dir.des.scope.2.07-stable copy.txt' # directory of domain descriptions
	pClass = 'a' # all alpha proteins

	domainList = readScope(filename, pClass)
	domain = createDomain(domainList[2])
	print(domain.size())

	testh = sse2vector(domainList[2]['pdbid'], domain.getStructs()[0])
	for helix in domain.getStructs():
		print(compareOrientation(sse2vector(domainList[2]['pdbid'], helix), testh))
		

if __name__ == '__main__':
	main()
