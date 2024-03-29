# -*- coding: utf-8 -*-

from lpsolve55 import *
from problema import Problema

total_variables = 0

def solve(p):
    """ Función para resolver el problema
    retorna una lista con la información de la bodega escogida

    Argumentos:
    - `p`: Instancia del problema
    """
    global total_variables
    total_variables   = (p.n + 1 + p.j * p.m * (p.n + 1) + p.j * p.m * (p.n + 1))
    cantRestricciones = (p.n + 1) + ((p.n + 1) * p.m) + ((p.n + 1) * p.j)
    funobj            = crearFuncionObjetivo(p)

    lp  = lpsolve('make_lp', cantRestricciones, total_variables)
    ret = lpsolve('set_lp_name', lp, 'calimio')
    lpsolve('set_verbose','calimio',IMPORTANT)

    lpsolve('set_obj_fn', 'calimio', funobj)

    for i in range(p.n+1):
        if i < p.n:
            restriccion = agregarRestriccionSuminitroDemanda(p, i)
            lpsolve('add_constraint', 'calimio', restriccion, LE, 0)

        for j in range(p.m):
            restriccion = agregarRestriccionSuministro(p, i, j)
            lpsolve('add_constraint', 'calimio', restriccion, LE, 0)

        for j in range(p.j):
            restriccion = agregarRestriccionDemanda(p, i, j)
            lpsolve('add_constraint', 'calimio', restriccion, EQ, 0)

    lpsolve('add_constraint', 'calimio', [val for x in [[1]*(p.n+1), [0]*(total_variables - p.n - 1)] for val in x], EQ, 1)

    for i in range(p.n+2,total_variables+1):
        lpsolve('set_int', lp, i, True)

    for i in range(1,p.n+2):
        lpsolve('set_binary', lp, i, True)

    ret = lpsolve('solve', lp)

    resp = dict()

    if ret == 2: # La solución no es FEASIBLE
        resp['feasible']  = False
    elif ret == 0: # Solución óptima
        resp['feasible']  = True
        resp['n']         = p.n # Cantidad de Bodegas
        resp['m']         = p.m # Cantidad de puntos de suministro
        resp['j']         = p.j # Cantidad de puntos de demanda
        resp['funobj']    = round(lpsolve('get_objective', lp)) # Valor de la función objetivo
        resp['binarias']  = lpsolve('get_variables', lp)[0][:p.n+1] # Guardo el conjunto de variables binarias
        resp['variables'] = lpsolve('get_variables', lp)[0][p.n+1:total_variables+1] # Guarda el conjunto de variables no binarias
        resp['bodega']    = [i for i,x in enumerate(resp['binarias']) if x == 1][0] # Escojo la bodega que fue solución, se indexa desde 0

        if resp['bodega'] != p.n:
            resp['capacidad'] = p.costos[resp['bodega']]['capacidad']

	#print 'Respuesta =', resp
    return resp
# end solve

def crearFuncionObjetivo(p):
    funobj = [p.costos[i]['costo'] / p.costos[i]['tiempo'] for i in range(p.n)] # Coeficiente de la variable binaria Xi
    funobj.append(0) # Sin bodega
    suministro_demanda = asignarSuministroDemanda(p.transdemanda)

    for i in range(p.n):
        funobj = [val for x in [funobj, suministro_demanda] for val in x] # Se agregaron los costos de punto de suministro a punto de demanda sin pasar por la bodega

    for i in suministro_demanda:
        funobj.append(i)

    for i in range(p.n):
        funobj = [val for x in [funobj, asignarSuministroBodegaDemanda(p.transbodega[i], p.tbodegademanda, i)] for val in x] # Se agregaron los costos de punto de suministro a punto de demanda pasando por la bodega

    for i in range(p.j * p.m): # Lleno de ceros las otras variables
        funobj.append(0)

    return funobj
# end crearFuncionObjetivo


def asignarSuministroDemanda(matriz):
    ret = []

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            ret.append(matriz[i][j])
    return ret
# end asignarSuministroDemanda

def asignarSuministroBodegaDemanda(suministro, demanda, i): # fila del suministro correspondiente a la bodega
    s = []
    for k in suministro:
        s.append(k)

    d = []
    for sublista in demanda:
        d.append(sublista[i])

    ret = []
    for a in s:
        for b in d:
            ret.append(a+b)
    return ret
# end asignarSuministroBodegaDemanda


def agregarRestriccionSuminitroDemanda(p,i): # Capacidad de la bodega
    global total_variables
    ret            = [0] * total_variables # Crea una lista de 0
    ret[i]         = -p.costos[i]['capacidad']
    indice_inicial = (p.n + 1 + p.j * p.m * (p.n + 1) + p.j * p.m * i)
    indice_final   = (p.n + 1 + p.j * p.m * (p.n + 1) + p.j * p.m * (i + 1))

    for k in range(indice_inicial, indice_final):
        ret[k] = 1

    return ret
# end agregarRestriccionSuministroDemanda

def agregarRestriccionSuministro(p,i,m): # Disponibilidad del suministro
    global total_variables
    ret            = [0] * total_variables # Crea una lista de 0
    ret[i]         = -p.suministros[m]

    indice_inicial = (p.n + 1 + p.j * m + p.j * p.m * i)
    indice_final   = indice_inicial + p.j

    for k in range(indice_inicial, indice_final):
        ret[k] = 1

    if i == p.n:
        return ret

    indice_inicial = (p.n+1+p.j*p.m*(p.n+1)+p.j*p.m*i+m*p.j)
    indice_final   = indice_inicial+p.j

    for k in range(indice_inicial, indice_final):
        ret[k] = 1

    return ret
# end agregarRestriccionSuministro

def agregarRestriccionDemanda(p,i,m): # Requerimiento de la demanda
    global total_variables
    ret            = [0] * total_variables # Crea una lista de 0
    ret[i]         = -p.demandas[m]

    indice_inicial = (p.n + 1 + p.j * p.m * i + m)
    indice_final   = (p.n + 1 + p.j * p.m * (i + 1) + m)

    for k in range(indice_inicial, indice_final, p.j):
        ret[k] = 1

    if i == p.n:
        return ret

    indice_inicial = (p.n + 1 + p.j * p.m * (p.n + 1) + i * p.j * p.m + m)
    indice_final   = (p.n + 1 + p.j * p.m * (p.n + 1) + (i + 1) * p.j * p.m)

    for k in range(indice_inicial, indice_final, p.j):
        ret[k] = 1

    return ret
# end agregarRestriccionDemanda
