import re
import string

def clean_text_round1(text):
    '''Eliminar signos de puntuacion, corchetes y palabras que aporten poco'''
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub('[%s]' %re.escape(string.punctuation
                                    ),'',text)
    text = re.sub('\w*\d\w*','',text)
    return text

def clean_text_round2(text):
    '''segunda ronda de limpieza'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text