def leiaInt(msg):
    """
    Função que verifica se o número inputado pelo user é um inteiro ou não.
    :param msg: Número.
    :return: Mensagens de possíveis erros.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
        else:
            return n


def linha(tam = 42):
    """
    Função que cria uma linha do caracter menos.
    :param tam: Quantidade de vezes que o sinal de menos será multiplicado.
    :return: Uma linha com 42 ou a quantidade de sinais especificado pelo user.
    """
    return '-' * tam


def cabeçalho(txt):
    """
    Função que cria um cabeçalho de texto.
    :param txt: Texto
    :return: Um cabeçalho centralizado e destacado junto á função linha.
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    Função que solicita ao user uma opção dentre as disponíveis.
    :param lista: Lista de opções do sistema.
    :return: A opção desejada.
    """
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
