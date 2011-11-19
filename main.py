#!env python
# -*- coding: utf-8 -*-

import files
import modelo

# main 
if __name__=='__main__':
	import sys
	
	if len(sys.argv) == 2:
		modelo.solve(files.leerarchivo(sys.argv[1]))
	else:
		print 'Especifique el nombre del archivo.'
