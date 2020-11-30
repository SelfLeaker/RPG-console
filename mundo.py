
from entidade import *


class Mundo(object):


	def __init__(self, nome):

		self.nome = nome
		self.areas = {}


	def get_nome(self):

		return self.nome


	def set_area(self, area):

		self.areas[area.get_nome()] = area


	def set_areas(self, areas):

		for area in areas:

			self.areas[area.get_nome()] = area


	def get_area(self, nome_area):

		area = self.areas.get(nome_area)

		if (area):
			return area

		return None


	def get_todas_areas(self):

		return [''.join(k[0]) for k in self.areas.items()]