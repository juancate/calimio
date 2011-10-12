# -*- coding: utf-8 -*-

"""
Clase para representar el problema
"""

class Problema:
	def __init__(self, n, m, j):
		self.n, self.m, self.j = n, m, j
	
	def set_suministros(self, suministros):
		self.suministros = suministros
	
	def set_demandas(self, demandas):
		self.demandas = demandas
	
	def set_costos(self, costos):
		self.costos = costos
	
	def set_trans_a_bodega(self, transbodega):
		self.transbodega = transbodega
	
	def set_trans_a_demanda(self, transdemanda):
		self.transdemanda = transdemanda
	
	def set_trans_bodega_a_demanda(self, tbodegademanda):
		self.tbodegademanda = tbodegademanda

	def __repr__(self):
		return __str__()

	def __str__(self):
		return "n = %d, m = %d, j = %d\nsumistros = %s \ndemandas = %s \ncostos = %s\ntransbodega = %s \ntransdemanda = %s \ntbodegademanda = %s" % \
					 (self.n, self.m, self.j, self.suministros, self.demandas, self.costos, self.transbodega, self.transdemanda, self.tbodegademanda)

