while True:

    from random import choice

    print("=-" * 5, "GERADOR DE SENHA", "=-" * 5)

    caracteres = "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*1234567890"

    tamanho_senha = int(input("Digite o comprimento desejado da senha: "))

    #As ''  é usada como o separador entre os caracteres, resultando em uma única string contendo a senha aleatória.
    #O join é usado pra concatenar os caracteres
    #O choice é função da biblioteca random que serve para pegar os caracteres da variável caractere
    #O _ para indicar que a variável não será usada no loop 
    senha = ''.join(choice(caracteres) for _ in range(tamanho_senha))

    print("Senha gerada:", senha)

    print()

    while True:
            cont = input("Você deseja gerar outra senha? [s/n]: ").lower()
            print()
            if cont in ["s", "n"]:
                break
            print("Por favor, digite 's' para sim ou 'n' para não.")

    if cont == "n":
        print("Fim do programa!")
        break