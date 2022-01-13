from app.Command import Command

class DEX(Command):

	def __init__(self):

		self.label = 'DEX'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('DIGITE O TEXTO: ')

		display = display.replace('\\n', '\x0d')

		display = '{:03d}{}'.format(len(display), display)

		return super().send(self.label, len(display), display)