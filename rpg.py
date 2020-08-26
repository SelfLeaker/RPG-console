
class Entidade(object):

	def __init__(self, nome):

		self.nome = nome

	def get_nome(self):

		return self.nome

class NPC(Entidade):

	def __init__(self, nome):

		super().__init__(nome)


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

class Area(Entidade):

	def __init__(self, nome, lista_npcs):

		super().__init__(nome)
		self.lista_npcs = []

	def set_npcs(npcs):

		self.lista_npcs = npcs

	def __str__(self):

		return self.get_nome()

class Mundo(object):

	def __init__(self, nome):

		self.nome = nome
		self.areas = {}

	def get_nome(self):

		return self.nome

	def set_area(self, area):

		self.areas[area.get_nome()] = area

	def get_area(self, nome_area):

		return self.areas[nome_area]

	def get_todas_areas(self):

		return [''.join(k[0]) for k in self.areas.items()]


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
		return input()

	def logica(self):

		resposta = ""

		while (self.jogando):

			resposta = input("R: ")

			if (resposta == "mover"):

				area = self.menu_mover()
				
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