def readScope(filename, pClass):
		"""
		@params
			filename (str): name of the file to be parsed
			pClass (str): the name of the desired class of domains ie. a, b, etc.

		@return
			domainArray: array of (pdbid, chain, range)
				pdbid (str): the id the domain is found in
				chain (str): the specific chain the domain is found in 
				range (tuple -> (int, int)): if present the specific residue range the domain lies on

		Here is an example of the lines that the function is parsing
			46457	cf	a.1	-	Globin-like
			113449	px	a.1.1.1	d1ux8a_	1ux8 A:
			^0      ^1      ^2      ^3   ^4   ^5
			Five tab-delimited columns:
				0. sunid
				1. level: cl - class; cf - fold; sf - superfamily; fa - family; dm - protein; sp - species; px - domain
				2. sccs
				3. sid or "-"
				4. pdbid
				5. chain and sometimes residue range
		"""
		domainList = []

		FUNKYRANGECOUNTER = 0

		with open(filename, 'r') as file:
			# defining variables in outer scope
			line = file.readline()
			# continue until end of file
			while line:
				domain_entry = dict()
				domain = line.split()
				# all we are only looking for lines describing the domain as well as the class we want... also getting rid of potentially funky lines?
				if domain[1] == 'px' and domain[2][0] == pClass and len(domain) == 6:
					# grabs class, domain name, and pdbid name
					domain_entry['class_id'] = domain[2]
					domain_entry['domain_name'] = domain[3]
					domain_entry['pdbid'] = domain[4]
					
					# description might look like 'A:1-25'
					description = domain[5].split(':')		
					domain_entry['chain'] = description[0]
					range = description[1]
					
					# sanitize range if present
					if range != '':
						try:
							domain_entry['range'] = tuple(int(x) for x in range.split('-'))
						except:
							# Dr. Song's code seemed to suggest that a multi-domain range was possible... has not been proven or disproven (at least for alpha proteins)
							# TODO: fix this so that it can handle multiple domain stuff like: b:1-38,b:152-190
							FUNKYRANGECOUNTER += 1
				
				domainList.append(domain_entry) # TODO: make sure that you aren't adding things that don't need to be added
				line = file.readline()
		
		print("# of funky ranges", FUNKYRANGECOUNTER)
		return domainList
		