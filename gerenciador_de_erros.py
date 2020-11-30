
class GerenciadorDeErros(object):

	def __init__(self):

		self.mensagens_de_erro = []
		self.debugging = False


	def adicionar_mensagem_de_erro(self, mensagem_de_erro, apenas_debug):

		self.mensagens_de_erro.append({"texto": mensagem_de_erro, "apenas_debug": apenas_debug})


	def existe_mensagens_de_erro(self):

		return bool(self.mensagens_de_erro)


	def mostrar_mensagens_de_erro(self):

		for mensagem_de_erro in self.mensagens_de_erro:

			mostrar_mensagem = True

			if (mensagem_de_erro['apenas_debug'] and not self.debugging):

				mostrar_mensagem = False

			if (mostrar_mensagem):

				print(mensagem_de_erro['texto'])


	def limpar_mensagens_de_erro(self):

		self.mensagens_de_erro.clear()


	def notificar_erro(self, mensagem_de_erro, apenas_debug = False):

		self.adicionar_mensagem_de_erro(mensagem_de_erro = mensagem_de_erro, apenas_debug = apenas_debug)

		return dict(erro = True,
					mensagem_de_erro = mensagem_de_erro)


	def logica(self):

		if self.existe_mensagens_de_erro():

			self.mostrar_mensagens_de_erro()

			self.limpar_mensagens_de_erro()
			