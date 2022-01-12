from app.Command import Command
from app.Helpers.app import message

class GIN(Command):

	def __init__(self):

		self.label = 'GIN'
		self.abecs = False

		super().__init__(self)

	def run(self):

		super().displayCommand()

		display = input('ESCOLHA 01 OU 02: ')

		text = '{}{:03d}{}'.format(self.label, len(display), display)

		return message(text)