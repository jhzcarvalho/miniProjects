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

def get_question():

    return {
        "question": "Qual a capital da frança?",
        "options": ["A) Berlin", "B) Paris", "C) Londres", "D) Roma"],
        "correct": "B"
    }

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    response = input("Sua resposta (A, B, C, ou D): ")
    response = response.upper()
    if response not in ["A", "B", "C", "D"]:
        print("====================")
        print("Resposta invalida.")
        print("====================")
        return ask_question(question)
    return response

def check_answer(response, correct):
    if response == correct:
        print("==========")
        print("Correto!")
        print("==========")
        return 1
    else:
        print("========================================")
        print("Incorreto. a alternativa correta é a", correct)
        print("========================================")
        return 0

def play_quiz(questions):
    score = 0
    for question in questions:
        response = ask_question(question)
        score += check_answer(response, question["correct"])
    print("=========================")    
    print("Sua nota final é ", score, "/", len(questions))
    print("=========================")  

if __name__ == "__main__":
    questions = [get_question() for _ in range(1)]  # criar questoes
    questions.append({
         "question": "Qual o maior planeta do sistema solar?",
        "options": ["A) Terra", "B) Marte", "C) Jupiter", "D) Venus"],
        "correct": "C"
    })
    questions.append({
        "question": "Qual o menor planeta do sistema solar?",
        "options": ["A) Mercurio", "B) Venus", "C) Terra", "D) Marte"],
        "correct": "A"
    })
    questions.append({
        "question": "Quantos estados tem o Brasil?",
        "options": ["A) 26", "B) 27", "C) 24", "D) 25"],
        "correct": "A"
    })
    questions.append({
         "question": "Quem é considerado o pai da computação?",
        "options": ["A) Freddie mercury", "B) Alan turing", "C) Steve Jobs", "D) Linus Torvalds"],
        "correct": "B"
    })
    questions.append({
         "question": "Quantos continentes a terra possui?",
        "options": ["A) 8", "B) 5", "C) 6", "D) 7"],
        "correct": "C"
    })
    play_quiz(questions)
    