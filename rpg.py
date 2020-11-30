
from npc import *
from area import *
from jogador import *
from mundo import *

from estados import *
from constantes import *
from gerenciador_de_comandos import *
from gerenciador_de_erros import *
from gerenciador_de_mundos import *
from assistente_de_entrada import *


class Jogo(object):

	def __init__(self):

		self.jogador = None
		self.jogando = True
		self.gerenciador_de_erros = GerenciadorDeErros()
		self.gerenciador_de_comandos = GerenciadorDeComandos(self.gerenciador_de_erros)
		self.gerenciador_de_mundos = GerenciadorDeMundos()
		self.todas_areas_do_mundo_atual = ()
		self.comandos = ()
		self.mundos = ()

	def mostrar_texto(self, texto):

		print(texto)

		return SUCESSO


	def mostrar_texto_dict(self, dicionario):

		texto = dicionario.get('texto')

		if (texto is None):

			return self.gerenciador_de_erros.notificar_erro("[-] Texto do dicionário não existe!", apenas_debug = True)

		self.mostrar_texto(texto)

		return SUCESSO


	def sair(self):

		self.jogando = False


	def ajuda(self):

		self.mostrar_texto("[+] Pressione TAB para listar as opções disponíveis!")


	def iniciar(self):

		"""

		Areas

		"""

		vermecia = Mundo("Vermécia")
		ellia = Mundo("Ellia")

		vermecia.set_areas(

			(
				Area("Campo de Treinamento",
					(
						NPC("Lothus"),
						NPC("Sieghart")
					)
				),
				Area("Altar",
					(
						NPC("Priest"),
						NPC("Viajante")
					)
				)
			)

		)

		ellia.set_areas(

			(
				Area("Campo de Treinamento",
					(
						NPC("Amon"),
						NPC("Darkatt")
					)
				),
				Area("Altar",
					(
						NPC("Darkpriest"),
						NPC("Guarda Amon")
					)
				)
			)

		)

		self.gerenciador_de_mundos.set_lista_de_mundos((vermecia, ellia))


		"""

		Jogador

		"""


		self.jogador = Jogador("Thiago", vermecia, vermecia.get_area("Campo de Treinamento"), self.gerenciador_de_erros)

		self.mostrar_texto_dict(self.jogador.get_localizacao_jogador_formatado())


		"""

		Comandos & Despachos


		"""


		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "mover",
			funcao_de_despacho = self.jogador.mover,
			depende_de = (self.menu_mover,)
		)

		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "ajuda",
			funcao_de_despacho = self.ajuda
		)

		"""
		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "listar_mundos",
			funcao_de_despacho = self.listar_mundos
		)
		"""

		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "listar_areas_do_mundo_atual",
			funcao_de_despacho = self.listar_areas_do_mundo_atual
		)

		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "localizacao",
			funcao_de_despacho = self.mostrar_texto,
			depende_de = (self.jogador.get_localizacao_jogador_formatado,)
		)

		self.gerenciador_de_comandos.associar_comando_a_funcao(
			comando = "sair",
			funcao_de_despacho = self.sair
		)

		self.comandos = self.gerenciador_de_comandos.get_lista_de_comandos()

		self.mundos = self.gerenciador_de_mundos.get_lista_de_mundos()

		self.todas_areas_do_mundo_atual = self.jogador.get_mundo_atual().get_todas_areas()

		self.assistente_de_entrada = AssistenteDeEntrada(
			todas_listas_de_opcoes = (
				self.comandos,
				self.mundos,
				self.todas_areas_do_mundo_atual
			),
			lista_de_opcoes_atual = self.comandos
		)

		self.logica()


	def listar_areas_do_mundo_atual(self):

		self.todas_areas_do_mundo_atual = self.jogador.get_mundo_atual().get_todas_areas()

		self.mostrar_texto(', '.join(self.todas_areas_do_mundo_atual))


	def listar_mundos(self):

		self.mostrar_texto(', '.join(self.mundos))


	def menu_mover(self):

		self.listar_areas_do_mundo_atual()

		try:

			self.assistente_de_entrada.atualizar_lista_de_opcoes(self.todas_areas_do_mundo_atual)

			area_escolhida = self.assistente_de_entrada.requisitar("R: ")

			if not (area_escolhida in self.todas_areas_do_mundo_atual) or area_escolhida is None:

				return self.gerenciador_de_erros.notificar_erro("[!] Escolha uma área válida!")
				"""
				return dict(area_escolhida = area_escolhida,
						erro = True,
						mensagem_de_erro = "[!] Escolha uma área válida!")
				"""

			return dict(area_escolhida = area_escolhida,
						erro = False,
						mensagem_de_erro = VAZIO)

		except:

			return self.gerenciador_de_erros.notificar_erro("[!] Escolha uma área válida!")


	def logica(self):

		while (self.jogando):

			lista_escolhida = self.comandos

			entrada = self.assistente_de_entrada.requisitar("R: ")

			lista_correspondente = self.assistente_de_entrada.get_lista_correspondente(entrada)
			
			if (lista_correspondente is None):
				continue

			lista_escolhida = lista_correspondente

			self.gerenciador_de_comandos.invocar_funcao_de_despacho(entrada)

			self.assistente_de_entrada.atualizar_lista_de_opcoes(lista_escolhida)

			self.gerenciador_de_erros.logica()


if __name__ == "__main__":

	rpg = Jogo()
	rpg.iniciar()