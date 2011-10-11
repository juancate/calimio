#!env python

"""
Funcion para leer un archivo de entrada
@return un diccionario con los datos cargados
"""

def leerarchivo(fn = 'input.in'):
	f = open(fn, 'r')

	d = dict()
	d['n'] = int(f.readline())
	d['m'] = int(f.readline())
	d['j'] = int(f.readline())
	
	d['suministros'] = cargarlista(f, d['m'])
	d['demandas'] = cargarlista(f, d['j'])
	d['costos'] = cargarcapacidadcosto(f, d['n'])
	d['transbodega'] = cargarvaloresmultiples(f, d['n'], d['m'])
	d['transdemanda'] = cargarvaloresmultiples(f, d['j'], d['m'])
	d['tbodegademanda'] = cargarvaloresmultiples(f, d['j'], d['n'])

	return d


"""
Funcion para cargar datos 
en forma de listas
"""
def cargarlista(f, m):
	s = []
	for i in range(m):
		el = int(f.readline())
		s.append(el)
	return s

"""
Carga las lineas raras con el - de la capacidad :P
"""
def cargarcapacidadcosto(f, n):
	s = []
	for i in range(n):
		junk = f.readline().split()
		n = int(junk[0])
		costo, tiempo = [int(x) for x in junk[-1].split('-')]
		s.append({'capacidad': n, 'costo': costo,  'tiempo':tiempo})
	return s

def cargarvaloresmultiples(f, n, m):
	s = []
	for i in range(n):
		t = [int(x) for x in f.readline().split()]
		s.append(t)
	return s

for i in leerarchivo().iteritems():
	print i
