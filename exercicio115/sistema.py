from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep


arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR UMA NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('ERRO: Digite uma pessoa válida!')
    sleep(2)

input()
