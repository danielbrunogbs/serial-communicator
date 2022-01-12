from app.Command import Command
from app.Helpers.app import message

class DEX(Command):

	def __init__(self):

		self.label = 'DEX'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('DIGITE O TEXTO: ')

		display = display.replace('\\n', '\x0d')

		text = '{}{:03d}{:03d}{}'.format(self.label, len(display) + 3, len(display), display)

		return message(text)