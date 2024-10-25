import hashlib
import os
from datetime import datetime

def gera_sha256(senha):
    sha_signature = hashlib.sha256(senha.encode()).hexdigest()
    return sha_signature

def verifica_cadastro():
    if not os.path.exists("senha.txt"):
        return False
    with open("senha.txt", "r") as file:
        data = file.read()
        if data:
            return True
        else:
            return False

def cadastro_usuario():
    print("Cadastre login e senha")
    login = input("login: ")    
    senha = input("senha:")
    senha = gera_sha256(senha)
    with open("senha.txt", "w") as file:
        file.write(f"Login: {login}\nSenha: {senha}\n")
    print("Usuário cadastrado com sucesso")

def login_usuario():
    print("Digite seu login e senha")
    login = input("login: ")    
    senha = input("senha:")
    senha = gera_sha256(senha)
    with open("senha.txt", "r") as file:
        data = file.read()
        if f"Login: {login}\nSenha: {senha}\n" in data:
            print("login efetuado com sucesso")
        else:
            print("login ou senha incorretos") 
            login_usuario()

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
            print(f"Senha {i+1}: {senha}")
        print(minuto)

if(verifica_cadastro() == False):
    cadastro_usuario()
login_usuario()
if(verifica_senha_semente() == False):
    registra_senha_semente()
gerar_senhas_aleatorias()


