app = Flask(__name__)

# Simulação de dados do aluno
aluno = {
    "nome": "Arthur",
    "desempenho": {
        "Matemática": 45,
        "Português": 80,
        "Programação": 60
    }
}

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/analise")
def analise():
    resultado = analisar_desempenho(aluno["desempenho"])
    return jsonify(resultado)

@app.route("/chat", methods=["POST"])
def chat():
    pergunta = request.json["mensagem"]

    resposta = gerar_recomendacao(
        pergunta,
        aluno["desempenho"]
    )

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)