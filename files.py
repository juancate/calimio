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

    p.suministros    = cargarlista(f, p.m)
    p.demandas       = cargarlista(f, p.j)
    p.costos         = cargarcapacidadcosto(f, p.n)
    p.transbodega    = cargarvaloresmultiples(f, p.n)
    p.transdemanda   = cargarvaloresmultiples(f, p.j)
    p.tbodegademanda = cargarvaloresmultiples(f, p.j)

    return p
# end leerarchivo


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
        if(junk[0] == 'IL'):
            import sys
            n = sys.maxint # Debe sorporta números como IL (capacidad ilimitada)
        else:
            n = int(junk[0])
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

