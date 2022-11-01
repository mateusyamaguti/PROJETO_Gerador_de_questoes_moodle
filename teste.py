from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

def create_xml():
  root = minidom.Document()
  xml = root.createElement('quiz')
  root.appendChild(xml)
  xml_str = root.toprettyxml(indent='\t', encoding='utf-8')
  save_path_file = "exemplo.xml"

  with open(save_path_file, mode = 'wb') as f:
      f.write(xml_str)

# raiz = arquivo.getroot()
# print(raiz.tag)
# for filhas in raiz:
#   print(filhas.tag, filhas.attrib)
##Acessar as tags filhas

##Encontrar filhas
## for filhas in raiz.findall('question'):
  # question = filhas.find('penalty').text
  # print(question)



# tree = ET.parse('exemplo.xml')
# root = tree.getroot()
# projeto = ET.fromstring('''
# <quiz>
# <!-- question: 421  -->
  # <question type="shortanswer">
  #   <name>
  #     <text>teste_resposta_curta</text>
  #   </name>
  #   <questiontext format="html">
  #     <text><![CDATA[<p dir="ltr" style="text-align: left;">teste_resposta_curta</p>]]></text>
  #   </questiontext>
  #   <generalfeedback format="html">
  #     <text></text>
  #   </generalfeedback>
  #   <defaultgrade>1</defaultgrade>
  #   <penalty>0.3333333</penalty>
  #   <hidden>0</hidden>
  #   <idnumber></idnumber>
  #   <usecase>0</usecase>
  #   <answer fraction="100" format="moodle_auto_format">
  #     <text>resposta_1</text>
  #     <feedback format="html">
  #       <text></text>
  #     </feedback>
  #   </answer>
  # </question>

# </quiz>
# ''')
# root.append(projeto)
# tree.write("exemplo.xml")


def create_shortanswer():
    pass

#Abrir o arquivo
file = ET.parse('shortanswer.xml')
#Identificar a árvore principal
root = file.getroot()
#Identificar a tag text, ou seja, texto da pergunta
print(root[0][0][0].text)
#alterar o texto
root[0][0][0].text = 'Texto da pergunta alterado'
#Reescrevendo o texto no XML
file.write('shortanswer.xml')


##nova instrução para adicionar elementos
root = minidom.Document()
#Criado elemento quiz
xml = root.createElement('quiz')
productChild = root.createElement('product') 
productChild.setAttribute('name', 'Geeks for Geeks') 
  
xml.appendChild(productChild) 
  
xml_str = root.toprettyxml(indent ="\t")  
  
save_path_file = "shortanswer.xml"
  
with open(save_path_file, "a") as f: 
    f.write(xml_str) 





