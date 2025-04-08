from flask import Flask, render_template, request, redirect, session
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
from model.controle_usuario import Usuario

app = Flask(__name__)

app.secret_key = 'didico'

#Abre a página inicial do site
@app.route('/', methods=["GET"])
def pagina_inicial():
    mensagens = Mensagem.recuperar_mensagens()
    return render_template("pagina-cadastro.html", mensagens = mensagens)

#Adiciona o usuario e o comentário
@app.route("/cadastro", methods=["POST"])
def pagina_cadastro():
    #Peguei as informações vindo do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("comentario")

    #Cadastrando a mensagem usando a Classe mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    

    #Redireciona para o index
    return redirect("/pagina-inicial")

#Deleta a mensagem
@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/pagina-inicial")

#Adiciona a curtida
@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/pagina-inicial")

#Deleta a curtida
@app.route("/put/mensagem/excluir/curtida/<codigo>")
def excluir_curtida(codigo):
    Mensagem.deslike_mensagem(codigo)
    return redirect("/pagina-inicial")

#Rota para abrir a página de cadastro
@app.route('/pagina-cadastro', methods=["GET"])
def pagina_inicial_cadastro():
    usuarios = Usuario.recuperar_usuarios()
    return render_template("pagina-cadastro.html", usuarios = usuarios)

#Rota para cadastrar o usuário
@app.route("/cadastro-usuario", methods=["POST"])
def adicionar_usuarios():
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    Usuario.adicionar_usuario(login, nome, senha)

    return redirect("/pagina-cadastro")

@app.route("/pagina-login")
def pagina_login():
    return render_template("pagina-login.html")

@app.route("/pagina-inicial")
def pagina_mensagem():
    if "usuario" in session:
        mensagens = Mensagem.recuperar_mensagens()
        return render_template("pagina-inicial.html", mensagens = mensagens)
    else:
        return redirect("/pagina-login")

@app.route("/post/verificar-usuario", methods=["POST"])
def verificar_usuario():
    login = request.form.get("login")
    senha = request.form.get("senha")
    usuario = Usuario.verificar_usuario(login, senha)

    if usuario == True:
        return redirect("/pagina-inicial")
    else:
        return redirect("/pagina-login")
    
@app.route("/sair")
def sair():
    Usuario.logoff()
    return redirect("/pagina-login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)