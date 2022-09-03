#!/usr/bin/env python3

from random import choice
from string import ascii_letters, digits, punctuation

def create_pw(lenght, type):
    pw = ''
    # type is the type of character accepted
    if type == 0:
        valid = list(ascii_letters)
        for i in range(lenght):
            pw += choice(valid)
    
    elif type == 1:
        valid = list(digits)
        for i in range(lenght):
            pw += choice(valid)
    
    elif type == 2:
        valid = list(punctuation)
        for i in range(lenght):
            pw += choice(valid)
    
    elif type == 3:
        valid = list(ascii_letters + digits)
        for i in range(lenght):
            pw += choice(valid)
    
    elif type == 4:
        valid = list(ascii_letters + punctuation)
        for i in range(lenght):
            pw += choice(valid)
    
    elif type == 5:
        valid = list(digits + punctuation)
        for i in range(lenght):
            pw += choice(valid)

    elif type == 6:
        valid = list(ascii_letters + digits + punctuation)
        for i in range(lenght):
            pw += choice(valid)

    return pw


def br():
    print('\nQual será o comprimento da senha?')
    leng = int(input('>>> '))
    
    print('\nEscolha o que pode compor a senha.')
    print('\n[0] - Só letras\n[1] - Só números\n[2] - Só símbolos\n[3] - Letras e números')
    print('[4] - Letras e símbolos\n[5] - Números e símbolos\n[6] - Tudo')
    type = int(input('>>> '))
    
    print(f'Senha gerada: {create_pw(leng, type)}')

def en():
    print('\nWhat will be the password lenght?')
    leng = int(input('>>> '))
    
    print('\nChoose what can be in the password.')
    print('\n[0] - Only letters\n[1] - Only numbers\n[2] - Only symbols\n[3] - Letters and numbers')
    print('[4] - Letters and symbols\n[5] - Numbers and symbols\n[6] - Everything')
    type = int(input('>>> '))
    
    print(f'Generated password: {create_pw(leng, type)}')

def main():
    print('[0] - Português (Brasileiro)\n[1] - English\n')
    lang = int(input('>>> '))
    if lang == 0: br()
    elif lang == 1: en()
    else: 
        print('Escolha inválida. Tente novamente.\nInvalid choice. Try again.')
        exit()

if __name__ == '__main__':
    main()