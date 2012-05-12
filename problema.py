# -*- coding: utf-8 -*-

class Problema:
    """Clase para representar el problema
    """

    # Constructor
    def __init__(self, n, m, j):
        self.n, self.m, self.j = n, m, j

    # Cargar suministros
    def _set_suministros(self, value):
        self._suministros = value

    def _get_suministros(self):
        return self._suministros

    # Cargar demandas
    def _set_demandas(self, value):
        self._demandas = value

    def _get_demandas(self):
        return self._demandas

    # Cargar costos
    def _set_costos(self, value):
        self._costos = value

    def _get_costos(self):
        return self._costos

    # Cargar transporte a bodegas desde los suministros
    def _set_transbodega(self, value):
        self._transbodega = value

    def _get_transbodega(self):
        return self._transbodega

    # Cargar transporte a puntos de demanda desde los suministros
    def _set_transdemanda(self, value):
        self._transdemanda = value

    def _get_transdemanda(self):
        return self._transdemanda

    # Cargar transporte desde bodega a puntos de demanda
    def _set_tbodegademanda(self, value):
        self._tbodegademanda = value

    def _get_tbodegademanda(self):
        return self._tbodegademanda


    def __repr__(self):
        return __str__()

    def __str__(self):
        return "n = %d, m = %d, j = %d\nsumistros = %s \ndemandas = %s \ncostos = %s\ntransbodega = %s \ntransdemanda = %s \ntbodegademanda = %s" % \
            (self.n, self.m, self.j, self.suministros, self.demandas, self.costos, self.transbodega, self.transdemanda, self.tbodegademanda)

    """
    Propiedades :
    """
    suministros    = property(_get_suministros, _set_suministros)
    demandas       = property(_get_demandas, _set_demandas)
    costos         = property(_get_costos, _set_costos)
    transbodega    = property(_get_transbodega, _set_transbodega)
    transdemanda   = property(_get_transdemanda, _set_transdemanda)
    tbodegademanda = property(_get_tbodegademanda, _set_tbodegademanda)

#end class Problema
