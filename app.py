import bluetooth
import helper

#Pega todos os dispositivos
devices = bluetooth.discover_devices(lookup_names=True)
key = 0

#Lista todos os dispositivos encontrados
for address, name in devices:

	print('{}: ({}) {}'.format(key, address, name))

	key = key + 1

#Verifica se encontrou algum dispositivo
if(len(devices) > 0):

	deviceId = int(input('Insira o valor do dispositivo: '))
	device = devices[deviceId]

	host = device[0]
	port = 3

	dev = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	dev.connect((host, port))

	while True:

		cmd = input('>')

		if(cmd == 'quit'):
			break

		message = helper.command(cmd)

		print('>> {}'.format(message))

		dev.send(message)
		dev.settimeout(10)

		response = bytes()

		while True:

			try:

				received = dev.recv(2049)

				response += received

				search = response.find(b'\x17')

				if(search >= 0):
					break

			except:

				print('Time out!')
				break

		print(response)

else:

	print('Nenhum dispositivo encontrado!')