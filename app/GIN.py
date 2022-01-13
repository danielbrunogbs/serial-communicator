from app.Command import Command

class GIN(Command):

	def __init__(self):

		self.label = 'GIN'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('ESCOLHA AS OPÇÕES ABAIXO:\n\n00 - Informações do PINPAD\n01 - Informações da Bibliotec Abecs\n\n>')

		return super().send(self.label, len(display), display)