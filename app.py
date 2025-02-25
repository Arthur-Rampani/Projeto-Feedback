from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=["GET"])
def pagina_inicial():
    return render_template("pagina-inicial.html")

@app.route("/cadastro", methods=["POST"])
def pagina_cadastro():
    #Peguei as informações vindo do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("comentario")
    data_hora = datetime.datetime.today()

    #Cadastrando  as informações no banco de dados
    #criando a conexão
    conexao = mysql.connector.connect(host = "localhost", 
                                      port = 3306, 
                                      user = "root", 
                                      password = "root", 
                                      database = "dbfeedback")
    
    #O cursor será responsável por manipular o banco de dados
    cursor = conexao.cursor()

    #Criando o SQL que será executado
    sql = """INSERT INTO tbcomentario
            (nome, comentario, data_comentario)
            VALUES
            (%s,%s,%s)"""
    valores = (usuario, mensagem, data_hora)

    #Executando o comando SQL
    cursor.execute(sql,valores)

    #Confirmo a alteração
    conexao.commit()

    #Fecho a conexão com o banco
    cursor.close()
    conexao.close()

    #Redireciona para o index
    return redirect("/")
app.run(debug=True)