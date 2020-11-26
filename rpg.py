
from npc import *
from area import *
from jogador import *
from mundo import *


class Jogo(object):

	def __init__(self):

		self.verm = Mundo("Vermillion")
		self.azz = Mundo("Azzure")
		self.jogador = None
		self.jogando = True

	# popular entidades dos mundos
	def iniciar(self):

		# npcs

		verm_cdt_npcs = ( NPC("verm_cdt_01"), NPC("verm_cdt_02") )
		verm_alt_npcs = ( NPC("verm_alt_01"), NPC("verm_alt_02") )

		azz_cdt_npcs = ( NPC("azz_cdt_01"), NPC("azz_cdt_02") )
		azz_alt_npcs = ( NPC("azz_alt_01"), NPC("azz_alt_02") )
		
		# locais

		verm_cdt = Area("Campo de Treinamento", verm_cdt_npcs)
		verm_alt = Area("Altar", verm_alt_npcs)

		azz_cdt = Area("Campo de Treinamento", azz_cdt_npcs)
		azz_alt = Area("Altar", azz_alt_npcs)

		self.verm.set_area(verm_cdt)
		self.verm.set_area(verm_alt)

		self.azz.set_area(azz_cdt)
		self.azz.set_area(azz_alt)

		# jogador

		#nome_jogador = input("Digite o nome do jogador : ")
		nome_jogador = "Thiago"
		self.jogador = Jogador(nome_jogador, self.verm, self.verm.get_area("Campo de Treinamento"))

		print(self.get_localizacao_jogador())

		self.logica()

	def listar_areas(self):

		print(self.verm.get_todas_areas())

	def menu_mover(self):

		self.listar_areas()
		
		try:

			area_escolhida = input()
			return area_escolhida

		except:

			print("[ERRO] A Área escolhida é inválida!")
			return ""


	def logica(self):

		resposta = ""

		while (self.jogando):

			resposta = input("R: ")

			if (resposta == "mover"):

				area = self.menu_mover()
				
				if (area):
					self.jogador.set_area_atual_por_nome(area)

			elif (resposta == "listar_areas"):
				self.listar_areas()

			elif (resposta == "loc"):
				print(self.get_localizacao_jogador())

			elif (resposta == "sair"):
				self.jogando = False

	def get_localizacao_jogador(self):

		return "[Localização] : " + self.jogador.get_nome_mundo_atual() + \
			  " - " + self.jogador.get_nome_area_atual()

if __name__ == "__main__":

	rpg = Jogo()
	rpg.iniciar()