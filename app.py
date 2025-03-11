from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask(__name__)

@app.route('/', methods=["GET"])
def pagina_inicial():
    mensagens = Mensagem.recuperar_mensagens()
    return render_template("pagina-inicial.html", mensagens = Mensagem)

@app.route("/cadastro", methods=["POST"])
def pagina_cadastro():
    #Peguei as informações vindo do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("comentario")

    #Cadastrando a mensagem usando a Classe mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    

    #Redireciona para o index
    return redirect("/")
app.run(debug=True)