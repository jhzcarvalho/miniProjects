###
# Crie um joguinho de pergutas e respostas que mostre uma pergunta qualquer 
# para o usuário e forneça 4 alternativas ('A', 'B', 'C' e 'D') de resposta,
# o programa deve receber a resposta do usuário e fazer as verificações 
# necessárias, quando todas as porgundtas forem respondidas, o programa deve
# mostrar a nota final do usuário.
#
# O programa deverá aceitar apenas as entradas que atendem as seguintes regras:
# - A resposta deverá conter apenas uma unica letra;
# - Essa letra deve ser correspondente à uma das alternativas ('A', 'B','C' e 'D');
# - Não é necessário diferenciar entre maiúsculas e minúsculas, então as 
#   entradas 'a', 'b', 'c' e 'd' são válidas
#
# Algumas etapas serão necessárias para realizar esse projeto, incluindo uma 
# maneira de armazenar as perguntas do quizz, contendo um enunciado, lista de 
# respostas e qual é a resposta correta, essas e outras decisões sobre como 
# pedaços especícicos do programa devem funcionar ficam ao seu critério.
# 
# OBS: Utilize funções para ajudar a organizar o código, isso facilitará
# o seu trabalho.
#
# Boa sorte!!

import time

def jogar():
    for i in range(5):
        print("jogando...")
        time.sleep(0.5)

    print("Voltando ao menu!")


def adiciona_questao():
    print("Adicionando questão..")
    time.sleep(3)


def edita_questao():
    print("Editando questão..")
    time.sleep(3)


def ativa_questao():
    print("Ativando/Desativando questão..")
    time.sleep(3)


def remove_questao():
    print("Removendo questão..")
    time.sleep(3)


def menu_questao():
    
    
    opt = ""

    while opt != "5":
        print(
            """
            > Menu Questão <
            """)
        

        print(
            """
            1. Adicionar questão 
            2. Editar questão 
            3. Ativar|Desativar qustão 
            4. Remover questão 
            5. Voltar ao menu principal
            """
        )
    
        opt = input('Selecione uma opção')

        if opt == "1": adiciona_questao()

        elif opt == "2": edita_questao()
            
        elif opt == "3": ativa_questao()

        elif opt == "4": remove_questao()

        elif opt == "5": print("Voltando ao Menu Principal..")

        else: print("Selecione uma opção válida..")


def main():
    """
    Exemplo  de Menu
    """

    opt = ""

    while opt != "3":
        print("""
            > Menu Principal <
            """)
        print(
            """
            1. Jogar
            2. Editar Questões
            3. Sair do Jogo
            """)

        opt = input('Selecione uma opção: ')

        if opt == "1": jogar()

        elif opt == "2": menu_questao()

        elif opt == "3": print("Saindo do jogo..")

        else: print("Selecione uma opção válida..")


if __name__ == "__main__":
    main()
