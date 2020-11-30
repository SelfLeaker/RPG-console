
from entidade import *


class Area(Entidade):


	def __init__(self, nome, lista_npcs):

		super().__init__(nome)
		self.lista_npcs = []


	def set_npcs(npcs):

		self.lista_npcs = npcs


	def __str__(self):

		return self.get_nome()