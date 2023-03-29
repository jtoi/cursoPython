import sys

if __name__ == '__main__':
    argumentos = sys.argv
    nombre_progrma = sys.argv[0]
    if len(sys.argv) > 1:
        primer_argumento = sys.argv[1]
        sys.exit(0)
    else:
        sys.exit(-1)

