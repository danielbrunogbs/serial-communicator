import crcmod
import os
import json

def crc(string):

	string = string.encode('ascii')

	crc16 = crcmod.predefined.mkCrcFun('xmodem')
	message = crc16(string)
	message = str(hex(message))

	crc_l = message[2:][:-2].rjust(2, '0')
	crc_r = message[2:][2:].rjust(2, '0')

	CRC = crc_l + crc_r
	CRC = bytes.fromhex(CRC)

	return CRC

def message(string):

	SYN = '\x16' #START
	ETB = '\x17' #END

	CRC_MSG = string + ETB
	CRC = crc(CRC_MSG)

	#string = string.encode('ascii').hex()

	MSG = SYN + string + ETB
	MSG = bytes.fromhex(MSG.hex())

	return MSG + CRC

def config(value):

	try:

		if not os.path.isfile('config.json'):

			return False

		else:

			config = open('config.json', 'r')

			config = json.loads(config.read())

			return config[value]

	except KeyError:

		return False