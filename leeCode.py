import sys

sH = False

def uso():
	print "USO\n\tleeHex.py [ARCHIVO] [OPCION]\n\nOPCION\n\tsH\n\t\tMostrar solo el codigo hexadecimal (para poder copiarlo)"

def hexArchivo(archivo):

	global sH

	contador = 0
	x = open(archivo, 'rb')

	if not sH:
		y = "0x{0:04x}".format(contador) + "\t"

	for i in x.read():
		y += "{0:02x}".format(ord(i))
		contador+=1

		if contador%16 == 0:
			print y 
			if not sH:
				y = "0x{0:04x}".format(contador) + "\t"
		else:
			y+=' '

	print y

def soloHex():
	global sH
	sH = True

def main(argv=None):
	if argv is None:
		argv = sys.argv

	if(len(argv) == 2):
		print sys.argv
		hexArchivo(argv[1])
	else:
		if(len(argv) == 3):
			opcion = {'sH': soloHex(),}

			try:
				opcion[argv[2]]
				hexArchivo(argv[1])
			except:
				print "Opcion '{0}' no valida\n".format(argv[2])
				print sys.exc_info()[0]
				uso()

		else:
			uso()

	return 0

if __name__ == '__main__':
	sys.exit(main())
