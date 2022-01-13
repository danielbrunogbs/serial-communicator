import serial
from app.Helpers.app import config

#Objeto dos Comandos

from app.OPN import OPN
from app.DSP import DSP
from app.DEX import DEX
from app.GIN import GIN
from app.MLI import MLI

#Comandos

commands = [
	OPN(),
	DSP(),
	DEX(),
	GIN(),
	MLI()
]

#Conexão com a porta serial

port = config('PORT')

if not port:

	port = input('Informe a porta: ')

connect = serial.Serial(port, 9600, timeout=0)

try:

	while True:

		# Menu

		print('==========================================================================')
		print('=   ██████╗███╗   ███╗    ██████╗ ██╗███╗   ██╗██████╗  █████╗ ██████╗   =')
		print('=  ██╔════╝████╗ ████║    ██╔══██╗██║████╗  ██║██╔══██╗██╔══██╗██╔══██╗  =')
		print('=  ██║     ██╔████╔██║    ██████╔╝██║██╔██╗ ██║██████╔╝███████║██║  ██║  =')
		print('=  ██║     ██║╚██╔╝██║    ██╔═══╝ ██║██║╚██╗██║██╔═══╝ ██╔══██║██║  ██║  =')
		print('=  ╚██████╗██║ ╚═╝ ██║    ██║     ██║██║ ╚████║██║     ██║  ██║██████╔╝  =')
		print('=   ╚═════╝╚═╝     ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═════╝   =')
		print('==========================================================================')

		print('\nSelecione o comando que deseja executar.\n')

		for index, command in enumerate(commands, start = 1):

			print('{}) {}'.format(index, command.label))

		print('\n')

		command = int(input('>')) - 1

		command = commands[command]

		message = command.run()

		connect.write(message)

		response = bytes()

		while True:

			received = connect.read(2049)

			response += received

			search = response.find(b'\x17')

			if(search >= 0):

				print('<< {}'.format(response))

				print('\n')

				break

except IndexError:

	print('Comando não encontrado!')

except:

	print('Algo de errado não está certo!')