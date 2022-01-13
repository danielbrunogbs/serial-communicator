from app.Command import Command

class OPN(Command):

	def __init__(self):

		self.label = 'OPN'
		self.abecs = False

		super().__init__(self)

	def run(self):

		return super().send(self.label, 0, '')