from exercicio115.lib.interface import *


def arquivoExiste(nome):
    """
    Função que verifica se o arquivo onde é guardado os dados existe.
    :param nome: Nome do arquivo.
    :return: True or False.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Função que cria o arquivo de texto onde é guardado os dados.
    :param nome: Nome do arquivo.
    :return: Se o arquivo foi criado ou não, antes da execução do sistema.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do aquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """
    Função que mostra as pessoas cadastradas no sistema.
    :param nome: Nome do arqquivo.
    :return: Dados lidos ou erro de leitura.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO: Ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    """
    Função que cadastra uma nova pessoa no sistema.
    :param arq: Seleciona o arquivo de texto que guarda os dados.
    :param nome: Guarda o nome lido.
    :param idade: Guarda a idade lida.
    :return: Sucesso ou erro na implementação da nova pessoa ao sistema.
    """
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
