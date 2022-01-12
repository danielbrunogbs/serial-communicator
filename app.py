import helper
import serial

#Objeto dos Comandos

from app.OPN import OPN

#Comandos

commands = [
	OPN()
]

# Menu

print('==========================================================================')
print('=   ██████╗███╗   ███╗    ██████╗ ██╗███╗   ██╗██████╗  █████╗ ██████╗   =')
print('=  ██╔════╝████╗ ████║    ██╔══██╗██║████╗  ██║██╔══██╗██╔══██╗██╔══██╗  =')
print('=  ██║     ██╔████╔██║    ██████╔╝██║██╔██╗ ██║██████╔╝███████║██║  ██║  =')
print('=  ██║     ██║╚██╔╝██║    ██╔═══╝ ██║██║╚██╗██║██╔═══╝ ██╔══██║██║  ██║  =')
print('=  ╚██████╗██║ ╚═╝ ██║    ██║     ██║██║ ╚████║██║     ██║  ██║██████╔╝  =')
print('=   ╚═════╝╚═╝     ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═════╝   =')
print('==========================================================================')

print('\n')

for index, command in enumerate(commands, start = 1):

	print('{}) {}'.format(index, command.label))

print('\n')

command = int(input('>')) - 1

try:

	command = commands[command]

	com = input('Informa a porta serial: ')

	ser = serial.Serial(com, 9600, timeout=0)

	while True:

		cmd = input('>')

		if(cmd == 'quit'):
			break

		message = helper.command(cmd)

		ser.write(message)

		response = bytes()

		while True:

			received = ser.read(2049)

			response += received

			search = response.find(b'\x17')

			if(search >= 0):

				print('{:3}'.format(response))

				print('<< {}'.format(response))

				break

except IndexError:

	print('Comando não encontrado!')

except:

	print('Algo deu errado!')