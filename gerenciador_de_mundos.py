
class GerenciadorDeMundos(object):


	def __init__(self, lista_de_mundos = ()):

		self.lista_de_mundos = lista_de_mundos


	def set_lista_de_mundos(self, lista_de_mundos):

		self.lista_de_mundos = lista_de_mundos


	def get_lista_de_mundos(self):

		return self.lista_de_mundos