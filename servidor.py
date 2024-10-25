import hashlib
import os
from datetime import datetime

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
        if data:
            for i in range(5):
                minuto = datetime.now().minute
                senha = gera_sha256(str(i))
                print(f"Senha {i}: {senha}")
        else:
            print("Senha semente não registrada")
            registra_senha_semente()
            gerar_senhas_aleatorias()

def verifica_senha_semente():
    if not os.path.exists("senha_semente.txt"):
        return False
    with open("senha_semente.txt", "r") as file:
        data = file.read()
        if data:
            return True
        else:
            return False

if(verifica_cadastro() == False):
    cadastro_usuario()
if(verifica_senha_semente() == False):
    registra_senha_semente()

registra_senha_semente()
gerar_senhas_aleatorias()

