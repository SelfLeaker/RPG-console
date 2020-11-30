
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


class AssistenteDeEntrada(object):


	def __init__(self, todas_listas_de_opcoes = (), lista_de_opcoes_atual = ()):

		self.todas_listas_de_opcoes = todas_listas_de_opcoes

		self.SUGESTOR = WordCompleter(
			lista_de_opcoes_atual,
			ignore_case=True
		)


	def atualizar_lista_de_opcoes(self, nova_lista_de_opcoes):

		setattr(self.SUGESTOR, 'words', nova_lista_de_opcoes)


	def requisitar(self, texto = ": "):

		return prompt(
			texto, completer=self.SUGESTOR, complete_while_typing=False
		)


	def lista_de_opcoes_igual(self, lista_de_opcoes):

		return getattr(self.SUGESTOR, 'words') == lista_de_opcoes


	def get_entradas_validas(self):

		lista_de_opcoes_juntas = []

		for lista in self.todas_listas_de_opcoes:

			lista_de_opcoes_juntas += lista

		return tuple(lista_de_opcoes_juntas)


	def get_lista_da_entrada(self, entrada):

		for lista in self.todas_listas_de_opcoes:

			if entrada in lista:

				return lista

		return None


	def get_lista_correspondente(self, entrada):

		#print(f"[!] {entrada}")

		entradas_validas = self.get_entradas_validas()

		#print(f"[!] {entradas_validas}")

		if entrada in entradas_validas:

			lista_escolhida = self.get_lista_da_entrada(entrada)

			#print(f"[+] {lista_escolhida}")

			return lista_escolhida

		#print(f"[!] Nenhuma correspondência para com a entrada!")

		return None