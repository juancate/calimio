# -*- coding: utf-8 -*-

from problema import Problema

"""
Funcion para leer un archivo de entrada
@return un diccionario con los datos cargados
"""

def leerarchivo(fn = 'input.in'):
	f = open(fn, 'r')
	p = Problema(int(f.readline()), int(f.readline()), int(f.readline()))
	p.set_suministros(cargarlista(f, p.m))
	p.set_demandas(cargarlista(f, p.j))
	p.set_costos(cargarcapacidadcosto(f, p.n))
	p.set_trans_a_bodega(cargarvaloresmultiples(f, p.n, p.m))
	p.set_trans_a_demanda(cargarvaloresmultiples(f, p.j, p.m))
	p.set_trans_bodega_a_demanda(cargarvaloresmultiples(f, p.j, p.n))

	return p

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
		c = int(junk[0])
		costo, tiempo = [int(x) for x in junk[-1].split('-')]
		s.append({'capacidad': c, 'costo': costo,  'tiempo':tiempo})
	return s

"""
Carga las lineas del costo de transporte
"""
def cargarvaloresmultiples(f, n, m):
	s = []
	for i in range(n):
		t = [int(x) for x in f.readline().split()]
		s.append(t)
	return s

