from tkinter import Tk
import random
import pathlib
import dropbox
import re
import os

from os import system, name   # import only system from os
from time import sleep  # import sleep to show output for some time period 

from twilio.rest import Client

# Variáveis de Controle
c = 0
senha_salva = ''
dropboxToken = ""
link = ''

'''
def send_SMS(phone_number, link):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                       to=os.environ.get('CELL_PHONE_NUMBER'),
                        body= f'Link para o Arquivo gerado pelo Gerador de Senhas 1.0\n{link}')
'''

def clear():  # define our clear function
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def cloudSave(accessToken, file):
    # the source file
    folder = pathlib.Path(".")     # located in this folder
    filepath = folder / file       # path object, defining the file

    # target location in Dropbox
    target = "/Temp/"              # the target folder
    targetfile = target + file     # the target path and file name

    # Create a dropbox object using an API v2 key
    d = dropbox.Dropbox(accessToken)

    # open the file and upload it
    with filepath.open("rb") as f:
        # upload gives you metadata about the file
        # we want to overwite any previous version of the file
        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))

    # create a shared link
    link = d.sharing_create_shared_link(targetfile)

    # url which can be shared
    url = link.url

    # link which directly downloads by replacing ?dl=0 with ?dl=1
    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
    print (dl_url)
    return dl_url

def open_senha():
    arquivo = open('senhas.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close
    return conteudo

def save_senha(conteudo):
    arquivo = open('senhas.txt', 'r')  # Abre em modo leitura
    lines = arquivo.readlines()  # Armazena todo o arquivo na variável
    arquivo.close()  # Fecha o arquivo
    arquivo = open('senhas.txt', 'w')  # Abre o arquivo como gravação
    lines.append('\n' + conteudo)
    arquivo.writelines(lines)  # Escreve as linhas anteriores adicionando as novas
    arquivo.close  # Fecha o arquivo

def all_passwords():
    senha = open_senha()
    c = 0
    temp = ""
    lista_senhas = ""
    while c < len(senha):
        if c > 1:
            temp = "| " + senha[c]
            c = c+1
            lista_senhas = lista_senhas + temp
        else:
            temp = senha[c]
            c = c+1
            lista_senhas = lista_senhas + temp
    print(lista_senhas)

def copy2clip(txt):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txt)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def gera_senha(senha, qtd_char_capitalized, qtd_special_char, qtd_number_char):
    char_capt = []
    char_special = []
    char_number = []
    qtd_senha = len(senha) - 1

    if qtd_char_capitalized > 0 and qtd_char_capitalized < len(senha)-1:
        i = 0
        while qtd_char_capitalized > i:
            char_capt.append(random.randint(65, 90))
            i += 1
            pos = random.randint(0, len(senha)-1)
            if senha[pos] == "\n":
                senha[pos] = (chr(char_capt.pop(random.randint(0, len(char_capt)-1))))
            else:
                i -= 1
                continue

    if qtd_special_char > 0 and qtd_special_char < len(senha)-1:
        i = 0
        while qtd_special_char > i:
            char_special.append(random.randint(33, 47))
            i += 1
            pos = random.randint(0, len(senha)-1)
            if senha[pos] == '\n':
                senha[pos] = (chr(char_special.pop(random.randint(0, len(char_special)-1))))
            else:
                i -= 1
                continue

    if qtd_number_char > 0 and qtd_number_char < len(senha)-1:
        i = 0
        while qtd_number_char > i:
            char_number.append(random.randint(48, 57))
            i += 1
            pos = random.randint(0, len(senha)-1)
            if senha[pos] == '\n':
                senha[pos] = (chr(char_number.pop(random.randint(0, len(char_number)-1))))
            else:
                i -= 1
                continue

    i = 0
    control_random = [1, 3]
    while '\n' in senha:
        pos = random.randint(0, len(senha)-1)
        if senha[pos] == '\n': # and not char_number and not char_capt and not char_special:
            senha[pos] = (chr((random.randint(97, 122))))

        i += 1

    senha_final = ''.join(senha)
    copy2clip(senha_final)
    return senha_final
    

def menu():
    print("1 - Gerar nova senha\n2 - Senhas já geradas\n3 - Sair")
    try:
        option = input('Digite a opção:')
        check_option(option)
    except:
        quit()

def check_option(option):
    if option == "1":
        clear()
        senha = []
        name_senha = input("Digite um nome para a senha: ")
        print('Quais as condições?\n')
        qtd_char = int(input('Quantidade de caracteres: '))
        while qtd_char > len(senha):
            senha.extend('\n')
            
        qtd_char_capitalized = 0
        qtd_special_char = 0
        qtd_number_char = 0

        char_capitalized = input('Precisa de Letras Maiusculas? Y ou N: ')
        if char_capitalized == 'Y':
            qtd_char_capitalized = int(input('Quantidade de maiusculas necessária? '))

        special_char = input('Precisa de caracteres especiais? Y ou N: ')
        if special_char == 'Y':
            qtd_special_char = int(input('Quantidade de caracteres especiais necessária? '))

        number_char = input('Precisa de números? Y ou N: ')
        if number_char == 'Y':
            qtd_number_char = int(input('Quantidade de números necessária? '))

        senha = gera_senha(senha, qtd_char_capitalized, qtd_special_char, qtd_number_char)
        print(senha)
        save_senha(name_senha + " | " + senha)
        link = cloudSave(dropboxToken, 'senhas.txt')
        # send_SMS("+5521980721158", link)
        
    elif option == "2":
        clear()
        all_passwords()

    elif option == "3":
        clear()
        quit()

    else:
        clear()
        print("OPÇÃO INVÁLIDA!!!")

while True:
    if c == 0:
        clear()
        print('Bem-vindo ao gerador de senhas!!')
        menu()

    else:
        menu()

    c = 1