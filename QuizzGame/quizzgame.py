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
import json


#Verifica se a resposta esta correta ou incorreta.
def check_answer(response, correct):

    if response == correct:
        print("==========")
        print("Correto!")
        print("==========")
        return True
    else:
        print("========================================")
        print("Incorreto. A alternativa correta é a", correct)
        print("========================================")
        return False


#Mostra a pergunta a ser respondida.
def ask_question(question):
    print(question["question"])
    
    for option in question["options"]:
        print(option)
    response = validar()
    return response

#Se a alternativa não for entre A,B,C ou D mostra na tela novamente para que o usuario digite uma alternativa valida.
def validar():
    
    response = input("Qual é a opçaõ correta? (A, B, C ou D): ")
    response = response.upper()

    while (response not in ["A", "B", "C", "D"]):
        print("Resposta invalida. Tente entre A, B, C ou D.")
        response = input("Sua resposta (A, B, C, ou D): ")
        response = response.upper()
    
    return response

#Função para adicionar questão.
def add_question():
    print("Siga os proximos passos...")
    time.sleep(0.4)

    add = input("Enunciado da questão: ")
    
    option_a = input("Opção A: ")
    option_b = input("Opção B: ")
    option_c = input("Opção C: ")
    option_d = input("Opção D: ")
    
    correct = validar()

    question = {
        "active": True,
        "question": add,
        "options": [option_a, option_b, option_c, option_d],
        "correct": correct.upper()
    }

    
    questions["question_list"].append(question)
    questions["num_active"] += 1

    with open("QuizzGame/questions.json", "w") as json_file:
            json.dump(questions, json_file)
    
    print("Questão adicionada com sucesso!!")
    print("Voltando para o menu...")
    time.sleep(1.5)
    menu_question()

#Lista todas as questões ativas.
def list_questions(questions):
    for i, question in enumerate(questions["question_list"], 1):
        print(f"{i}. {question['question']}")

#Função para deletar questões.
def del_question():
    print("Siga os proximos passos...")
    time.sleep(0.4)
    list_questions(questions)

    delet = int(input("Qual o numero da questão que voce quer excluir: ")) - 1 
    if delet < len(questions["question_list"]):
        
        questao_deletada = questions["question_list"].pop(delet)
        if questao_deletada["active"]:
             questions["num_active"] -= 1
        
        with open("QuizzGame/questions.json", "w") as json_file:
            json.dump(questions, json_file)

        print("Questão excluída com sucesso!")
    else:
        print("Número de questão inválido.")

    time.sleep(0.8)
    menu_question()

#função para editar questão.
def edit_question():
    print("Siga os proximos passos...")
    time.sleep(0.4)
    list_questions(questions)

    edit = int(input("Qual o numero da questão que voce quer editar: ")) - 1

    if edit < len(questions["question_list"]):
        new_question = input("Novo enunciado da questão: ")
        new_option_a = input("Nova opção A: ")
        new_option_b = input("Nova opção B: ")
        new_option_c = input("Nova opção C: ")
        new_option_d = input("Nova opção D: ")
        
        new_correct = validar()
        
        questions["question_list"][edit] = {
            "active": True,
            "question": new_question,
            "options": [new_option_a, new_option_b, new_option_c, new_option_d],
            "correct": new_correct.upper()
        }

        with open("QuizzGame/questions.json", "w") as json_file:
            json.dump(questions, json_file)

        print("Questão atualizada com sucesso!")
    
    else:
        print("Número de questão inválido.")
    
    time.sleep(0.8)
    menu_question()

#Um menu dentro do menu, quando o usuario escolher a opção 2 do menu principal, esse é ativado.
def menu_question():
            print("---------------------")
            print("Aguarde um momento...")
            print("---------------------")
            time.sleep(1)
            print("=======================")
            print("Perguntas adicionais...")
            print("=======================")
            ad = input(" 1- Adicionar nova questão\n 2- Excluir questão\n 3- Editar questões\n 4- Voltar para o menu\n Sua escolha: ")
            
            
            if ad == '1': add_question()
            
            elif ad == '2': del_question()

            elif ad == '3': edit_question()

            elif ad == '4': menu()

            else:
                print("Opção inválida, tente novamente entre 1, 2, 3, 4.")
                menu_question()


def play_quiz(questions):
    score = 0
    count = 0
    print("Ok vamos jogar!!")
    time.sleep(0.4)
    print("Começando Quizz...")
    time.sleep(0.8)

    for question in questions["question_list"]:
        if question["active"]:
            count += 1
            response = ask_question(question)
            
            if response == question["correct"]:
                 score += 1
                 print("correto")
            else:
                 print("incorreto")     
            
    print("=========================")    
    print(f"Sua nota final é  {score}/{count}!")
    print("=========================")
    if score >= 5:
        print("Parabéns!! voce foi muito bem!!!")
    else:
        print("oopss, fique tranquilo voce pode tentar novamente!!")
    time.sleep(1.5)
    print("Voltando para o Menu...")
    time.sleep(1.8)
    menu()


def menu():
    
        print("==================")
        print("+-+-Menu Quizz-+-+")
        print("==================")
        time.sleep(0.3)
        print("--------------")
        n = input("1- Jogar\n2- Questões\n3- Sair\n--------------\nSua escolha: ")

        if n == '1': play_quiz(questions)

        elif n == '2': menu_question()

        elif n == '3':
            print("ok, Até logo!!")
            exit()
     
        else:
            print("Opção inválida! Tente entre 1, 2 ou 3.")
            menu()


if __name__ == "__main__":

    with open("QuizzGame/questions.json", "r") as json_file:
        questions = json.load(json_file)

    menu()

