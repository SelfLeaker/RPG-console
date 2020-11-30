
from entidade import *
from estados import *


class Jogador(Entidade):


	def __init__(self, nome, mundo_atual, area_atual, gerenciador_de_erros):

		super().__init__(nome)

		self.mundo_atual = mundo_atual
		self.area_atual = area_atual
		self.gerenciador_de_erros = gerenciador_de_erros


	def get_nome_mundo_atual(self):

		return self.mundo_atual.get_nome()		


	def get_nome_area_atual(self):

		return self.area_atual.get_nome()


	def set_mundo_atual(self, novo_mundo):

		self.mundo_atual = novo_mundo


	def get_mundo_atual(self):

		return self.mundo_atual


	def set_area_atual(self, nova_area):

		self.area_atual = nova_area


	def get_area_atual(self):

		return self.area_atual


	def set_area_atual_por_nome(self, nome_area):

		area = self.mundo_atual.areas.get(nome_area)

		if (area is None): return ERRO
		
		self.set_area_atual(area)
			
		return SUCESSO


	def mover(self, area_escolhida):

		if (not area_escolhida):
			
			return self.gerenciador_de_erros.notificar_erro("[!] Escolha uma área válida!")
		
		self.set_area_atual_por_nome(area_escolhida)

		return SUCESSO


	def get_localizacao_jogador_formatado(self):

		return dict(texto = f"[Localização] : {self.get_nome_mundo_atual()} - {self.get_nome_area_atual()}",
					erro = False,
					mensagem_de_erro = VAZIO
			   )