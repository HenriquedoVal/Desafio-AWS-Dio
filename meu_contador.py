import re, sys

def main(entrada, saida):
	try:
		arquivo = open(entrada, 'r', encoding='utf8')
		arquivo = re.findall("[\w']+", arquivo.read())
		arquivo = [i.lower() for i in arquivo]
		arquivo = [(i, arquivo.count(i)) for i in set(arquivo)]
		arquivo.sort(key=lambda i: i[1], reverse=True)

		arquivo_saida = open(saida, 'a')
		for i in arquivo:
			arquivo_saida.write(str(i)+'\n')
		arquivo_saida.close()

	except FileNotFoundError:
		print(f'Arquivo a ser lido não encontrado. Tente: "py {parametros[0]} <path_leitura> <path_saída>"')

if __name__ == '__main__':
	parametros = sys.argv
	main(parametros[1], parametros[2])
	
