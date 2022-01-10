import helper
import serial

#Portal serial

com = input('Informa a porta serial: ')

#Listando portas seriais

ser = serial.Serial(com, 9600, timeout=0)

while True:

	cmd = input('>')

	if(cmd == 'quit'):
		break

	message = helper.command(cmd)

	ser.write(message)

	response = bytes()

	while True:

		try:

			received = ser.read(2049)

			response += received

			search = response.find(b'\x17')

			if(search >= 0):

				print('{:3}'.format(response))

				print('<< {}'.format(response))

				break

		except:

			print('Algo deu errado!')
			break

ser.close()