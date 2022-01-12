from app.Command import Command
from app.Helpers.app import message

class OPN(Command):

	def __init__(self):

		self.label = 'OPN'
		self.abecs = False

		super().__init__(self)

	def run(self):

		return message('OPN')