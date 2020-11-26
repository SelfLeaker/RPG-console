
from entidade import *

class Jogador(Entidade):

	def __init__(self, nome, mundo_atual, area_atual):

		super().__init__(nome)
		self.mundo_atual = mundo_atual
		self.area_atual = area_atual

	def get_nome_mundo_atual(self):

		return self.mundo_atual.get_nome()		

	def get_nome_area_atual(self):

		return self.area_atual.get_nome()

	def set_mundo_atual(self, mundo_atual):

		self.mundo_atual = mundo_atual

	def set_area_atual(self, area_atual):

		self.area_atual = area_atual

	def set_area_atual_por_nome(self, nome_area_atual):

		self.area_atual = self.mundo_atual.areas[nome_area_atual]