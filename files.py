# -*- coding: utf-8 -*-

from problema import Problema

# leerarchivo
def leerarchivo(fn = 'input.in'):
	"""Funcion para leer un archivo de entrada
	returna un objeto de la clase Problema

	Argumentos:
	- `fn`: nombre del archivo

	Retorna:
	- Una instacia de la clase Problema
	"""
	f = open(fn, 'r')
	p = Problema(int(f.readline()), int(f.readline()), int(f.readline()))
	p.set_suministros(cargarlista(f, p.m))
	p.set_demandas(cargarlista(f, p.j))
	p.set_costos(cargarcapacidadcosto(f, p.n))
	p.set_trans_a_bodega(cargarvaloresmultiples(f, p.n))
	p.set_trans_a_demanda(cargarvaloresmultiples(f, p.j))
	p.set_trans_bodega_a_demanda(cargarvaloresmultiples(f, p.j))

	return p


# cargarlista
def cargarlista(f, m):
	"""Funcion para cargar datos en forma de listas

	Argumentos:
	- `f`: objeto file
	- `m`: número de objetos a cargar
	"""
	s = []
	for i in range(m):
		el = int(f.readline())
		s.append(el)
	return s


# cargarcapacidadcosto
def cargarcapacidadcosto(f, n):
	"""Carga las lineas raras con el - de la capacidad :P

	Argumentos:
	- `f`: objeto file
	- `n`: número de objetos a cargar
	"""
	s = []
	for i in range(n):
		junk = f.readline().split()
		n = junk[0] # Debe sorporta números como IL (capacidad ilimitada)
		costo, tiempo = [int(x) for x in junk[-1].split('-')]
		s.append({'capacidad': n, 'costo': costo,  'tiempo':tiempo})
	return s


# cargarvaloresmultiples
def cargarvaloresmultiples(f, n):
	"""Carga las lineas del costo de transporte

	Argumentos:
	- `f`: objeto file
	-`n`: número de objetos a cargar
	"""
	s = []
	for i in range(n):
		t = [int(x) for x in f.readline().split()]
		s.append(t)
	return s

