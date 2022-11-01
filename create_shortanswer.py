from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
from input_shortanswer import q_name

def create_category(category_name = 'new_category'):
    #Acessar configurações de categoria
    file = ET.parse('questions.xml')
    #Acessar raiz da árvore
    root = file.getroot()
    #Acessar categoria
    '''print(root[0][0][0].text)'''
    #Modificar categoria
    root[0][0][0].text = category_name
    file.write('questions.xml')

def new_shortanswer(q_name='new question', q_text = 'question text', q_feedback = '',
                    q_penalty = '', q_answer = 'correct answer'):
    file = ET.parse('questions.xml')
    root = file.getroot()
    projeto = ET.fromstring(f'''<question type="shortanswer">
        <name>
        <text>{q_name}</text>
        </name>
        <questiontext format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{q_text}</p>]]></text>
        </questiontext>
        <generalfeedback format="html">
        <text>{q_feedback}</text>
        </generalfeedback>
        <defaultgrade>1</defaultgrade>
        <penalty>{q_penalty}</penalty>
        <hidden>0</hidden>
        <idnumber></idnumber>
        <usecase>0</usecase>
        <answer fraction="100" format="moodle_auto_format">
        <text>{q_answer}</text>
        <feedback format="html">
            <text></text>
        </feedback>
        </answer>
    </question>''')
    root.append(projeto)
    file.write("questions.xml")
  
