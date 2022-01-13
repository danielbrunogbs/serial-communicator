from app.Command import Command

class DSP(Command):

	def __init__(self):

		self.label = 'DSP'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('DIGITE O TEXTO: ')

		return super().send(self.label, len(display), display)