import re, sys

def main():
	parametros = sys.argv
	msg_err = f'Necessário o uso dos parâmetros. Tente: "python3 {parametros[0]} <path_leitura> <path_saída>"'

	try:
		if len(parametros) != 3: raise IndexError
		
		arquivo = open(parametros[1], 'r', encoding='utf8')
		dados = re.findall("[\w]+", arquivo.read())
		arquivo.close()

		dados = [i.lower() for i in dados]
		dados = [(i, dados.count(i)) for i in set(dados)]
		dados.sort(key=lambda i: i[1], reverse=True)

		arquivo_saida = open(parametros[2], 'a', encoding='utf8')
		for i in dados:
			arquivo_saida.write(f'{i[0]}: {i[1]}\n')
		arquivo_saida.close()

	except FileNotFoundError:
		print(msg_err)
	except  IndexError:
		print(msg_err)

if __name__ == '__main__':
	main()