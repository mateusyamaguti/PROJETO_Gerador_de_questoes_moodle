def q_name():
    question_name = str(input('Digite o nome da questão: '))
    return question_name

def q_text():
    question_text = str(input('Digite o texto da questão: '))
    return question_text

def q_feedback():
    question_feedback = str(input('Digite o feedback da questão: '))
    return question_feedback

def q_penalty():
    question_penalty = str(input('Penalidade de 0 a 1, números decimais com ponto (.):'))
    return question_penalty

def q_answer():
    question_answer = str(input('Resposta da questão: '))
    return question_answer

def input_setting():
    sublist = []
    q_feedback = str(input('Digite o feedback da questão: '))
    q_penalty = str(input('Digite o penalti da questão: '))
    sublist.append(q_feedback)
    sublist.append(q_penalty )
    return tuple(sublist)
