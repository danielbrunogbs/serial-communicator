from app.Command import Command
from app.Helpers.app import message

class DSP(Command):

	def __init__(self):

		self.label = 'DSP'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('DIGITE O TEXTO: ')

		display = bytes(display, 'utf-8')

		print(display)

		text = '{}{:03d}{}'.format(self.label, len(display), display)

		return message(text)