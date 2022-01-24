import re, sys

def main():
	parametros = sys.argv
	msg_err = f'Necessário o uso dos parâmetros. Tente: "python3 {parametros[0]} <path_leitura> <path_saída>"'

	try:
		if len(parametros) != 3: raise FileNotFoundError
		
		arquivo = open(parametros[1], 'r', encoding='utf8')
		dados = dados_brutos = arquivo.read()
		arquivo.close()

		dados = re.findall("[\w]+", dados)
		dados = [i.lower() for i in dados]
		dados = [(i, dados.count(i)) for i in set(dados)]
		dados.sort(key=lambda x: x[1], reverse=True)

		dados_brutos = dados_brutos.split()
		dados_brutos = [(i, dados_brutos.count(i)) for i in set(dados_brutos)]
		dados_brutos.sort(key=lambda x: x[1], reverse=True)

		arquivo_saida = open(parametros[2], 'a', encoding='utf8')
		arquivo_saida.write('Re'.ljust(30)+ '| Brutos\n'+'-'*100 + '\n')

		for i in range(len(max(dados, dados_brutos, key=len))):
			if i < len(dados) and i < len(dados_brutos):
				arquivo_saida.write(f'{dados[i][0]}: {dados[i][1]}'.ljust(30) + '| ' + f'{dados_brutos[i][0]}: {dados_brutos[i][1]}\n')
			elif i < len(dados) and i >= len(dados_brutos):
				arquivo_saida.write(f'{dados[i][0]}: {dados[i][1]}\n')
			elif i >= len(dados) and i < len(dados_brutos):
				arquivo_saida.write(' '*30 + '| ' + f'{dados_brutos[i][0]}: {dados_brutos[i][1]}\n')
				
		arquivo_saida.close()

	except FileNotFoundError:
		print(msg_err)

if __name__ == '__main__':
	main()