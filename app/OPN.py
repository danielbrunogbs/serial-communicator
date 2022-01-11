from app.Command import Command

class OPN(Command):

	def __init__(self):

		self.id = 'A'
		self.label = 'OPN'

	def run(self):

		print('Entrou no processamento')