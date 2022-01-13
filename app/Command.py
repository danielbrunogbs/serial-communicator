import crcmod

class Command():

	def __init__(self, children):

		self._SYN = 22
		self._ETB = 23

		self.children = children

		return

	def displayCommand(self):

		print('\nVocê selecionou o comando {} siga a instruções abaixo.\n'.format(self.children.label))

		return

	def __crc(self, string):

		string = string[1:]

		crc16 = crcmod.predefined.mkCrcFun('xmodem')
		message = crc16(string)

		hexa = hex(message)

		byte1 = int(hexa[2:-2], 16)
		byte2 = int(hexa[4:], 16)

		return byte1, byte2

	def send(self, command, length, message):

		buffer = bytearray()

		buffer.append(self._SYN)

		for char in command:

			buffer.append(ord(char))

		length = '{:03d}'.format(length)

		for char in length:

			buffer.append(ord(char))

		for char in message:

			buffer.append(ord(char))

		buffer.append(self._ETB)

		CRC = self.__crc(buffer)

		for byte in CRC:

			buffer.append(byte)

		return buffer