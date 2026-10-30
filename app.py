
from flask import Flask, render_template, jsonify, request
from ia.gerador_questoes import gerar_exercicios


app = Flask(__name__)


# Questões da avaliação inicial
QUESTOES = [

    # MATEMÁTICA - ADIÇÃO

    {
        "id": 1,
        "materia": "Matemática",
        "topico": "Adição",
        "pergunta": "Quanto é 25 + 17?",
        "alternativas": {
            "A": "32",
            "B": "42",
            "C": "52",
            "D": "40"
        },
        "resposta_correta": "B"
    },

    {
        "id": 2,
        "materia": "Matemática",
        "topico": "Adição",
        "pergunta": "Quanto é 136 + 48?",
        "alternativas": {
            "A": "174",
            "B": "184",
            "C": "194",
            "D": "164"
        },
        "resposta_correta": "B"
    },

    # MATEMÁTICA - SUBTRAÇÃO

    {
        "id": 3,
        "materia": "Matemática",
        "topico": "Subtração",
        "pergunta": "Quanto é 50 - 23?",
        "alternativas": {
            "A": "27",
            "B": "37",
            "C": "23",
            "D": "17"
        },
        "resposta_correta": "A"
    },

    {
        "id": 4,
        "materia": "Matemática",
        "topico": "Subtração",
        "pergunta": "Quanto é 145 - 67?",
        "alternativas": {
            "A": "88",
            "B": "78",
            "C": "82",
            "D": "72"
        },
        "resposta_correta": "B"
    },

    # MATEMÁTICA - MULTIPLICAÇÃO

    {
        "id": 5,
        "materia": "Matemática",
        "topico": "Multiplicação",
        "pergunta": "Quanto é 8 x 7?",
        "alternativas": {
            "A": "54",
            "B": "48",
            "C": "56",
            "D": "64"
        },
        "resposta_correta": "C"
    },

    {
        "id": 6,
        "materia": "Matemática",
        "topico": "Multiplicação",
        "pergunta": "Quanto é 12 x 9?",
        "alternativas": {
            "A": "108",
            "B": "98",
            "C": "118",
            "D": "96"
        },
        "resposta_correta": "A"
    },

    # MATEMÁTICA - DIVISÃO

    {
        "id": 7,
        "materia": "Matemática",
        "topico": "Divisão",
        "pergunta": "Quanto é 81 / 9?",
        "alternativas": {
            "A": "8",
            "B": "7",
            "C": "9",
            "D": "6"
        },
        "resposta_correta": "C"
    },

    {
        "id": 8,
        "materia": "Matemática",
        "topico": "Divisão",
        "pergunta": "Quanto é 144 / 12?",
        "alternativas": {
            "A": "10",
            "B": "12",
            "C": "14",
            "D": "11"
        },
        "resposta_correta": "B"
    },

    # PORTUGUÊS - ORTOGRAFIA

    {
        "id": 9,
        "materia": "Português",
        "topico": "Ortografia",
        "pergunta": "Qual palavra está escrita corretamente?",
        "alternativas": {
            "A": "Excessão",
            "B": "Exceção",
            "C": "Esceção",
            "D": "Ecessão"
        },
        "resposta_correta": "B"
    },

    {
        "id": 10,
        "materia": "Português",
        "topico": "Ortografia",
        "pergunta": "Qual alternativa apresenta a grafia correta?",
        "alternativas": {
            "A": "Privilégio",
            "B": "Previlegio",
            "C": "Privilejio",
            "D": "Previlégio"
        },
        "resposta_correta": "A"
    },

    # PORTUGUÊS - PLURAL

    {
        "id": 11,
        "materia": "Português",
        "topico": "Plural",
        "pergunta": "Qual é o plural de cidadão?",
        "alternativas": {
            "A": "Cidadões",
            "B": "Cidadãos",
            "C": "Cidadães",
            "D": "Cidadãoses"
        },
        "resposta_correta": "B"
    },

    {
        "id": 12,
        "materia": "Português",
        "topico": "Plural",
        "pergunta": "Qual é o plural de papel?",
        "alternativas": {
            "A": "Papeis",
            "B": "Papels",
            "C": "Papéis",
            "D": "Papeles"
        },
        "resposta_correta": "C"
    },

    # PORTUGUÊS - VERBOS

    {
        "id": 13,
        "materia": "Português",
        "topico": "Verbos",
        "pergunta": "Qual alternativa apresenta um verbo no passado?",
        "alternativas": {
            "A": "Caminharei",
            "B": "Caminho",
            "C": "Caminhei",
            "D": "Caminharei amanhã"
        },
        "resposta_correta": "C"
    },

    {
        "id": 14,
        "materia": "Português",
        "topico": "Verbos",
        "pergunta": "Na frase 'Maria estuda todos os dias', qual é o verbo?",
        "alternativas": {
            "A": "Maria",
            "B": "Estuda",
            "C": "Todos",
            "D": "Dias"
        },
        "resposta_correta": "B"
    },

    # PORTUGUÊS - ANTÔNIMOS

    {
        "id": 15,
        "materia": "Português",
        "topico": "Antônimos",
        "pergunta": "Qual é o antônimo de generoso?",
        "alternativas": {
            "A": "Bondoso",
            "B": "Egoísta",
            "C": "Solidário",
            "D": "Gentil"
        },
        "resposta_correta": "B"
    },

    {
        "id": 16,
        "materia": "Português",
        "topico": "Antônimos",
        "pergunta": "Qual é o antônimo de tranquilo?",
        "alternativas": {
            "A": "Calmo",
            "B": "Sereno",
            "C": "Agitado",
            "D": "Silencioso"
        },
        "resposta_correta": "C"
    },

    # PORTUGUÊS - INTERPRETAÇÃO

    {
        "id": 17,
        "materia": "Português",
        "topico": "Interpretação",
        "pergunta": "Leia: 'João saiu de casa com um guarda-chuva porque estava chovendo.' Por que João levou o guarda-chuva?",
        "alternativas": {
            "A": "Porque estava ensolarado",
            "B": "Porque estava chovendo",
            "C": "Porque estava frio",
            "D": "Porque iria viajar"
        },
        "resposta_correta": "B"
    },

    {
        "id": 18,
        "materia": "Português",
        "topico": "Interpretação",
        "pergunta": "Leia: 'Ana estudou bastante e conseguiu uma boa nota.' O que contribuiu para o resultado de Ana?",
        "alternativas": {
            "A": "O descanso",
            "B": "A sorte exclusivamente",
            "C": "O estudo",
            "D": "A ausência de provas"
        },
        "resposta_correta": "C"
    },

    # PORTUGUÊS - PONTUAÇÃO

    {
        "id": 19,
        "materia": "Português",
        "topico": "Pontuação",
        "pergunta": "Qual alternativa apresenta a pontuação correta?",
        "alternativas": {
            "A": "Olá como vai.",
            "B": "Olá, como vai?",
            "C": "Olá como, vai?",
            "D": "Olá; como vai,"
        },
        "resposta_correta": "B"
    },

    {
        "id": 20,
        "materia": "Português",
        "topico": "Pontuação",
        "pergunta": "Qual sinal deve ser utilizado para indicar uma pergunta?",
        "alternativas": {
            "A": "Ponto final",
            "B": "Vírgula",
            "C": "Ponto de interrogação",
            "D": "Ponto e vírgula"
        },
        "resposta_correta": "C"
    },

    # PORTUGUÊS - CONCORDÂNCIA

    {
        "id": 21,
        "materia": "Português",
        "topico": "Concordância",
        "pergunta": "Qual frase apresenta concordância correta?",
        "alternativas": {
            "A": "Os menino brinca.",
            "B": "As meninas brincam.",
            "C": "A meninas brincam.",
            "D": "Os meninos brinca."
        },
        "resposta_correta": "B"
    },

    {
        "id": 22,
        "materia": "Português",
        "topico": "Concordância",
        "pergunta": "Complete: 'Os alunos _____ preparados para a prova.'",
        "alternativas": {
            "A": "está",
            "B": "estamos",
            "C": "estão",
            "D": "estive"
        },
        "resposta_correta": "C"
    }

]


# Classifica o nível de desempenho
def classificar_nivel(percentual):

    if percentual < 40:
        return "Inicial"

    elif percentual < 70:
        return "Em desenvolvimento"

    elif percentual < 90:
        return "Bom"

    return "Avançado"


# Página inicial
@app.route("/")
def inicio():

    return render_template("index.html")


# Página da avaliação
@app.route("/avaliacao")
def avaliacao():

    return render_template("avaliacao.html")


# Página de resultados
@app.route("/resultado")
def resultado():

    return render_template("resultado.html")


# Disponibiliza as questões sem o gabarito
@app.route("/api/questoes", methods=["GET"])
def obter_questoes():

    questoes_publicas = []

    for questao in QUESTOES:

        questao_publica = {
            "id": questao["id"],
            "materia": questao["materia"],
            "topico": questao["topico"],
            "pergunta": questao["pergunta"],
            "alternativas": questao["alternativas"]
        }

        questoes_publicas.append(questao_publica)

    return jsonify({
        "questoes": questoes_publicas
    })


# Corrige a avaliação inicial
@app.route("/api/corrigir", methods=["POST"])
def corrigir():

    dados = request.get_json(silent=True) or {}

    respostas = dados.get("respostas", {})
    nome = dados.get("nome", "Estudante")

    if not isinstance(respostas, dict):

        return jsonify({
            "erro": "Formato de respostas inválido."
        }), 400

    total_questoes = len(QUESTOES)
    acertos = 0

    desempenho = {}

    for questao in QUESTOES:

        topico = questao["topico"]
        materia = questao["materia"]

        resposta_usuario = respostas.get(
            str(questao["id"])
        )

        if topico not in desempenho:

            desempenho[topico] = {
                "materia": materia,
                "topico": topico,
                "total": 0,
                "acertos": 0
            }

        desempenho[topico]["total"] += 1

        if resposta_usuario == questao["resposta_correta"]:

            acertos += 1
            desempenho[topico]["acertos"] += 1

    percentual_geral = round(
        (acertos / total_questoes) * 100
    )

    resultado_topicos = []
    reforcos = []

    for topico, dados_topico in desempenho.items():

        percentual = round(
            (dados_topico["acertos"] / dados_topico["total"]) * 100
        )

        nivel = classificar_nivel(percentual)

        resultado_topicos.append({

            "materia": dados_topico["materia"],
            "topico": topico,
            "total": dados_topico["total"],
            "acertos": dados_topico["acertos"],
            "percentual": percentual,
            "nivel": nivel

        })

        # Recomenda reforço quando o desempenho é inferior a 70%
        if percentual < 70:

            reforcos.append({

                "materia": dados_topico["materia"],
                "topico": topico,
                "nivel": nivel

            })

    return jsonify({

        "nome": nome,
        "acertos": acertos,
        "total": total_questoes,
        "percentual_geral": percentual_geral,
        "nivel_geral": classificar_nivel(percentual_geral),
        "desempenho": resultado_topicos,
        "reforcos": reforcos

    })


# Gera exercícios personalizados utilizando o banco local
@app.route("/api/reforco", methods=["POST"])
def reforco():

    dados = request.get_json(silent=True) or {}

    materia = dados.get("materia")
    topico = dados.get("topico")
    nivel = dados.get("nivel", "Em desenvolvimento")

    materias_validas = ["Matemática", "Português"]

    topicos_validos = {

        "Matemática": [
            "Adição",
            "Subtração",
            "Multiplicação",
            "Divisão"
        ],

        "Português": [
            "Ortografia",
            "Plural",
            "Verbos",
            "Antônimos",
            "Interpretação",
            "Pontuação",
            "Concordância"
        ]

    }

    niveis_validos = [
        "Inicial",
        "Em desenvolvimento",
        "Bom",
        "Avançado"
    ]

    if materia not in materias_validas:

        return jsonify({
            "erro": "Matéria inválida."
        }), 400

    if topico not in topicos_validos[materia]:

        return jsonify({
            "erro": "Tópico inválido."
        }), 400

    if nivel not in niveis_validos:

        nivel = "Em desenvolvimento"

    try:

        questoes = gerar_exercicios(
            materia=materia,
            topico=topico,
            nivel=nivel,
            quantidade=5
        )

        return jsonify({

            "materia": materia,
            "topico": topico,
            "questoes": questoes

        })

    except Exception as erro:

        print("Erro ao gerar exercícios:", erro)

        return jsonify({
            "erro": "Não foi possível gerar os exercícios. Tente novamente."
        }), 500


if __name__ == "__main__":

    app.run(debug=True)
