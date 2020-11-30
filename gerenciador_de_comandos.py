
from estados import *


class GerenciadorDeComandos(object):


	def __init__(self, gerenciador_de_erros):

		self.dict_comando_e_despacho = {}
		self.dict_comando_e_argumentos = {}
		self.dict_comando_e_funcao_dependente = {}
		self.gerenciador_de_erros = gerenciador_de_erros


	def __existe_comando(self, comando):

		return self.dict_comando_e_despacho.get(comando) is not None


	def associar_comando_a_funcao(self, comando, funcao_de_despacho, depende_de = ()):

		self.dict_comando_e_funcao_dependente[comando] = depende_de

		self.dict_comando_e_despacho[comando] = funcao_de_despacho

		return SUCESSO


	def __logica_variaveis_funcoes(self, comando):

		funcoes_dependentes = self.dict_comando_e_funcao_dependente.get(comando)

		if (funcoes_dependentes is not None):

			for funcao_dependente in funcoes_dependentes:

				retorno = funcao_dependente()

				if (retorno['erro']):

					return retorno

				for e in ['erro', 'mensagem_de_erro']:

					retorno.pop(e)

				self.associar_comando_a_argumentos(comando, **retorno)

		return SUCESSO


	def invocar_funcao_de_despacho(self, comando):

		if not self.__existe_comando(comando):

			return self.gerenciador_de_erros.notificar_erro(f"[-] Comando {comando} inválido ou não implementado!")

		retorno = self.__logica_variaveis_funcoes(comando)

		if (retorno['erro']):

			return retorno

		argumentos_de_despacho = self.recuperar_argumentos(comando)

		if (argumentos_de_despacho is None):

			self.dict_comando_e_despacho[comando]()

		else:

			self.dict_comando_e_despacho[comando](**argumentos_de_despacho)

		return SUCESSO


	def associar_comando_a_argumentos(self, comando, **argumentos):

		self.dict_comando_e_argumentos[comando] = argumentos


	def recuperar_argumentos(self, comando):

		return self.dict_comando_e_argumentos.get(comando)


	def get_lista_de_comandos(self):

		return list(self.dict_comando_e_despacho.keys())