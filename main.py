from input_shortanswer import q_name, q_text, q_feedback, q_penalty, q_answer
from create_shortanswer import new_shortanswer



if __name__ == '__main__':
    while True:
        new_shortanswer(q_name = q_name(), q_text=q_text(),
        q_feedback=q_feedback(), q_penalty=q_penalty(), q_answer=q_answer())
        start = str(input('would you like make other short question? [S/N]')).upper()
        if start[0] == 'N':
            break
        