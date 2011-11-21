# -*- coding: utf-8 -*-

def output(resp):
	""" Funcion para imprimir en consola la solucion
	    
	Argumentos
	- 'resp': Diccionario con la informacion de la bodega escogida
	"""
	if resp['feasible'] == False:
		print 'El problema no tiene solución.'
		return

	n = resp['n']
	j = resp['j']
	m = resp['m']
	ancho = j + 2
	unidadesEnviadas = unidadesSuministroDemanda(resp['variables'],n,m,j,resp['bodega'])
	unidadesBodega = unidadesSuministroBodegaDemanda(resp['variables'],n,m,j,resp['bodega'])
	
	# imprime en consola el encabezado de 
	print ''	
	print '...........................................'
	print ' funcion objetivo: ', resp['funobj']
	
	if resp['bodega'] == n:
		print ' bodega: ninguna',
	else:
		print ' bodega: ', resp['bodega'] + 1 
	
	print ' capacidad: ', resp['capacidad']
	print ' unidades almacenadas: ', unidadesAlmacenadas(unidadesBodega)
	print '...........................................'
	print ''
	
	# imprime en consola el encabezado de la tabla
	lineaHorizontal(ancho)
	print ' |sum\dem|',
	for i in range(1,j+1):
		print '    ', i,'     |',
	print '  total  |'
	lineaHorizontal(ancho)

	# imprime en consola la cantidad de unidades enviadas desde los puntos de 
	# suministro a demanda directamente/pasando por la bodega
	for k in range(0,m):
		print ' |  ', (k+1), ' ',
		for l in range(0,j):	
			print '| ', unidadesEnviadas[k][l],'/',unidadesBodega[k][l],
		print '|  ', unidadesSuministro(k,unidadesEnviadas)+unidadesSuministro(k,unidadesBodega) , '  |'		
		lineaHorizontal(ancho)
	
	# imprime en consola la ultima fila de la tabla
	print ' | total |',
	for i in range(0,j):
		print '   ', unidadesDemanda(i,unidadesEnviadas)+unidadesDemanda(i,unidadesBodega),'   |',
	print '         |'
	lineaHorizontal(ancho)
	
	print ''

def unidadesSuministroDemanda(variables,n,m,j,bodega):
	""" Funcion para calcular la lista de unidades enviadas del suministro directamente a la demanda
	    
	Argumentos
	- 'variables': Lista con la solucion a las variables no binarias del problema
	- 'n': cantidad de bodegas
	- 'm': cantidad de puntos de suministro
	- 'j': cantidad de puntos de demanda
	- 'bodega': indice de la posición de la bodega elegida
	"""
	unidades = []
	sublista = []
	indice = bodega*m*j
	
	for i in range(0,m):
		for k in range (0,j):
			sublista.append(variables[indice])
			indice = indice + 1
		unidades.append(sublista)
		sublista = []
	
	return unidades

def unidadesSuministroBodegaDemanda(variables,n,m,j,bodega):
	""" Funcion para calcular la lista de unidades enviadas del suministro a la demanda pasando por la bodega
	    
	Argumentos
	- 'variables': Lista con la solucion a las variables no binarias del problema
	- 'n': cantidad de bodegas
	- 'm': cantidad de puntos de suministro
	- 'j': cantidad de puntos de demanda
	- 'bodega': indice de la posición de la bodega elegida
	"""
	unidades = []
	sublista = []
	indice = (n+1)*m*j+bodega*m*j
	
	for i in range(0,m):
		for k in range (0,j):
			sublista.append(variables[indice])
			indice = indice + 1
		unidades.append(sublista)
		sublista = []
	
	return unidades
	
def lineaHorizontal(l):
	""" Funcion para imprimir en consola una linea horizontal de ancho l
	    
	Argumentos
	- 'l': ancho de la linea horizontal 
	"""
	print ' ',
	for j in range(0,l):
		for k in range(1,7):
			print '-',
	print ''

def unidadesAlmacenadas(matriz):
	""" Funcion para calcular el numero total de unidades almacenadas en la bodega
	    
	Argumentos
	- 'matriz': lista de listas con la cantidad de unidades enviadas a través de la bodega
	"""
	unidades = 0

	for i in matriz:
		for j in i:
			unidades = unidades + j

	return unidades

def unidadesSuministro(index,matriz):
	""" Funcion para calcular el numero total de unidades despachada desde el punto de suministro index
	    
	Argumentos
	- 'matriz': lista de listas con la cantidad de unidades enviadas
	"""
	suma = 0
	
	for i in matriz[index]:
		suma = suma + i
	
	return suma
	
def unidadesDemanda(index,matriz):
	""" Funcion para calcular el numero total de unidades recibidas desde el punto de demanda
	    
	Argumentos
	- 'matriz': lista de listas con la cantidad de unidades enviadas
	"""
	suma = 0
	
	for i in matriz:
		suma = suma + i[index]
	return suma
