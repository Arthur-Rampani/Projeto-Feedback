from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=["GET"])
def pagina_inicial():
    return render_template("pagina-inicial.html")

app.run(debug=True)