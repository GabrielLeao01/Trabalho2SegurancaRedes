import hashlib
import os
from datetime import datetime
import time

def gera_sha256(senha):
    sha_signature = hashlib.sha256(senha.encode()).hexdigest()
    return sha_signature

def verifica_cadastro():
    if not os.path.exists("usuario_servidor.txt"):
        return False
    with open("usuario_servidor.txt", "r") as file:
        data = file.read()
        if data:
            return True
        else:
            return False

def cadastro_usuario():
    print("Crie seu usuário")
    login = input("login: ")    
    with open("usuario_servidor.txt", "w") as file:
        file.write(f"Login: {login}\n")
    print("Usuário cadastrado com sucesso")

def verifica_senha_semente():
    if not os.path.exists("senha_semente.txt"):
        return False
    with open("senha_semente.txt", "r") as file:
        data = file.read()
        if data:
            return True
        else:
            return False

def registra_senha_semente():
    print("Digite a senha semente")
    senha = input("senha:")
    senha = gera_sha256(senha)
    with open("senha_semente.txt", "a") as file:
        file.write(f"Senha semente: {senha}\n")
    print("Senha semente registrada com sucesso")   


def gerar_senhas_aleatorias():
    if os.path.exists("senhas_servidor.txt"):
        os.remove("senhas_servidor.txt")
    with open("senha_semente.txt", "r") as file:
        data = file.read()
        senha_semente = data.split(": ")[1].strip()
        for i in range(5):
            minuto = datetime.now().minute
            hash_salt = gera_sha256(str(minuto))
            if i == 0:
                senha = gera_sha256(senha_semente + hash_salt)[:6]
            else:
                senha = gera_sha256(senha + hash_salt)[:6]
            with open("senhas_servidor.txt", "a") as senha_file:
                senha_file.write(f"Senha {i+1}: {senha}\n")


def valida_senha():
    min_antes = datetime.now().minute
    senha_inserida = input("Digite a senha: ")
    if(min_antes == datetime.now().minute):
        with open("senhas_servidor.txt", "r") as file:
            senhas = file.readlines()
            for linha in senhas:
                senha_armazenada = linha.split(": ")[1].strip()
                if senha_inserida == senha_armazenada:
                    print("Senha válida!")
                    with open("senhas_servidor.txt", "w") as file:
                        for linha in senhas:
                            senha_armazenada = linha.split(": ")[1].strip()
                            if senha_inserida == senha_armazenada:
                                break
                            file.write(linha)
                    return
                
        print("Senha inválida!")
    if(min_antes != datetime.now().minute):
        print("Tempo esgotado, novas senhas foram geradas")
        gerar_senhas_aleatorias()

if(verifica_cadastro() == False):
    cadastro_usuario()
if(verifica_senha_semente() == False):
    registra_senha_semente()
gerar_senhas_aleatorias()
while True:
    valida_senha()
