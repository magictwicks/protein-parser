from prody import pathPDBFolder
from readscope import readScope
from helixcount import hcount
from sse2vector import sse2vector
from SecStruct import getAngle, compareOrientation

def main():
	pathPDBFolder('./pdb_archive') # sets folder for PDB files to be downloaded to 
	filename = './dir.des.scope.2.07-stable copy.txt' # directory of domain descriptions
	pClass = 'a' # all alpha proteins

	domainList = readScope(filename, pClass)
	helices = hcount(domainList[2])
	print(len(helices))

	testh = sse2vector(domainList[2]['pdbid'], helices[0])
	for helix in helices:
		print(compareOrientation(sse2vector(domainList[2]['pdbid'], helix), testh))
		

if __name__ == '__main__':
	main()
