from input_shortanswer import q_name, q_text, q_answer, input_setting
from create_shortanswer import new_shortanswer, create_category



if __name__ == '__main__':

    create_category()
    start_setting = input_setting()
    print(start_setting)

    while True:
        new_shortanswer(q_name = q_name(), q_text=q_text(),
        q_feedback=start_setting[0], q_penalty=start_setting[1], q_answer=q_answer())
        start = str(input('would you like make other short question? [S/N]')).upper()
        if start[0] == 'N':
            break
        