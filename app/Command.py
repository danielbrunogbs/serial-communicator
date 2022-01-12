class Command():

	def __init__(self, children):

		self.children = children

		return

	def displayCommand(self):

		print('\nVocê selecionou o comando {} siga a instruções abaixo.\n'.format(self.children.label))

		return