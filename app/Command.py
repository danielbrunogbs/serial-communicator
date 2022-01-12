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

		# print(string)

		# string = string.decode('utf-8')

		string = string[1:]
		# string = string[-1:]

		# print(string)

		crc16 = crcmod.predefined.mkCrcFun('xmodem')
		message = crc16(string)
		# message = str(hex(message))

		# print(message)

		# crc_l = message[2:][:-2].rjust(2, '0')
		# crc_r = message[2:][2:].rjust(2, '0')

		# CRC = crc_l + crc_r
		# CRC = bytes.fromhex(CRC)

		# print(CRC)

		return message

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

		hexa = hex(CRC)

		print(hexa[2:])

		# print(int(CRC / 256))
		# print(int(CRC % 256))

		# buffer.append()
		# buffer.append(int(CRC % 256))

		print(buffer)

		exit()

		return