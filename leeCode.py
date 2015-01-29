import sys

def uso():
	print "USO\n\tleeHex.py [ARCHIVO]"

def hexArchivo(archivo):

	contador = 0
	x = open(archivo, 'rb')

	y = "0x{0:04x}".format(contador) + "\t"

	for i in x.read():
		y += "{0:02x}".format(ord(i))
		contador+=1

		if contador%16 == 0:
			print y 
			y = "0x{0:04x}".format(contador) + "\t"
		else:
			y+=' '

	print y

def main(argv=None):
	if argv is None:
		argv = sys.argv

	if(len(argv) == 2):
		print sys.argv
		hexArchivo(argv[1])
	else:
		uso()
		
	return 0

if __name__ == '__main__':
	sys.exit(main())
