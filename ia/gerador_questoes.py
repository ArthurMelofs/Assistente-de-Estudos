
import random


# Banco local de exercícios do StudyIA.
# Cada questão contém: enunciado, alternativas, gabarito e explicação.

BANCO_QUESTOES = {

    "Matemática": {

        "Adição": [
            ("Quanto é 34 + 28?", ["52", "62", "72", "58"], "B", "34 + 28 = 62."),
            ("Uma loja vendeu 125 produtos pela manhã e 87 à tarde. Quantos vendeu?", ["202", "212", "222", "200"], "B", "125 + 87 = 212."),
            ("Quanto é 246 + 153?", ["389", "399", "409", "3990"], "B", "246 + 153 = 399."),
            ("Uma biblioteca tinha 350 livros e recebeu mais 175. Quantos tem agora?", ["515", "525", "535", "500"], "B", "350 + 175 = 525."),
            ("Quanto é 1.245 + 356?", ["1.501", "1.591", "1.601", "1.611"], "C", "1.245 + 356 = 1.601."),
            ("Pedro tinha 48 figurinhas e ganhou 37. Com quantas ficou?", ["75", "85", "95", "81"], "B", "48 + 37 = 85.")
        ],

        "Subtração": [
            ("Quanto é 73 - 28?", ["45", "55", "35", "43"], "A", "73 - 28 = 45."),
            ("Uma loja tinha 150 unidades e vendeu 64. Quantas sobraram?", ["96", "86", "76", "84"], "B", "150 - 64 = 86."),
            ("Quanto é 500 - 275?", ["225", "235", "215", "325"], "A", "500 - 275 = 225."),
            ("Uma viagem tem 320 km. Se 145 km já foram percorridos, quantos faltam?", ["165", "175", "185", "195"], "B", "320 - 145 = 175."),
            ("Quanto é 1.000 - 468?", ["542", "532", "522", "632"], "B", "1.000 - 468 = 532."),
            ("Marina tinha R$ 90 e gastou R$ 37. Quanto restou?", ["R$ 53", "R$ 63", "R$ 57", "R$ 43"], "A", "90 - 37 = 53.")
        ],

        "Multiplicação": [
            ("Quanto é 9 x 6?", ["45", "54", "56", "64"], "B", "9 x 6 = 54."),
            ("Uma caixa tem 12 lápis. Quantos lápis há em 7 caixas?", ["72", "84", "96", "74"], "B", "12 x 7 = 84."),
            ("Quanto é 15 x 8?", ["100", "110", "120", "130"], "C", "15 x 8 = 120."),
            ("Uma sala tem 6 fileiras com 14 cadeiras cada. Quantas cadeiras há?", ["74", "80", "84", "90"], "C", "6 x 14 = 84."),
            ("Quanto é 23 x 4?", ["82", "92", "96", "102"], "B", "23 x 4 = 92."),
            ("Um pacote custa R$ 18. Quanto custam 5 pacotes?", ["R$ 80", "R$ 85", "R$ 90", "R$ 95"], "C", "18 x 5 = 90.")
        ],

        "Divisão": [
            ("Quanto é 96 / 8?", ["10", "11", "12", "13"], "C", "96 dividido por 8 é igual a 12."),
            ("24 balas serão divididas igualmente entre 6 crianças. Quantas cada uma recebe?", ["3", "4", "5", "6"], "B", "24 / 6 = 4."),
            ("Quanto é 144 / 12?", ["10", "11", "12", "14"], "C", "144 / 12 = 12."),
            ("Uma escola distribuiu 120 livros igualmente em 10 turmas. Quantos por turma?", ["10", "11", "12", "15"], "C", "120 / 10 = 12."),
            ("Quanto é 225 / 15?", ["12", "13", "14", "15"], "D", "225 / 15 = 15."),
            ("72 alunos foram divididos em grupos de 9. Quantos grupos foram formados?", ["6", "7", "8", "9"], "C", "72 / 9 = 8.")
        ]
    },

    "Português": {

        "Ortografia": [
            ("Qual palavra está escrita corretamente?", ["Enxergar", "Enchergar", "Enxerguar", "Encherga"], "A", "A forma correta é enxergar, com x."),
            ("Qual alternativa está escrita corretamente?", ["Beneficiente", "Beneficente", "Benefissente", "Beneficênte"], "B", "A grafia correta é beneficente."),
            ("Complete: 'Ele agiu com muita _____.'", ["discrição", "descrição", "discreção", "descreção"], "A", "Discrição significa reserva ou prudência."),
            ("Qual palavra está escrita corretamente?", ["Privilégio", "Previlegio", "Privilejio", "Previlégio"], "A", "A grafia correta é privilégio."),
            ("Qual alternativa apresenta a grafia correta?", ["Excessivo", "Excesivo", "Escessivo", "Ecessivo"], "A", "Excessivo é escrito com xc e ss."),
            ("Complete: 'A _____ de trânsito foi intensa.'", ["exceção", "excessão", "esceção", "ecessão"], "A", "Exceção é a grafia correta.")
        ],

        "Plural": [
            ("Qual é o plural de animal?", ["Animales", "Animais", "Animalis", "Animaleses"], "B", "Palavras terminadas em -al geralmente trocam -al por -ais."),
            ("Qual é o plural de pão?", ["Pãos", "Pães", "Pãoses", "Pãons"], "B", "O plural de pão é pães."),
            ("Qual é o plural de cidadão?", ["Cidadões", "Cidadãos", "Cidadães", "Cidadãoses"], "B", "O plural de cidadão é cidadãos."),
            ("Qual é o plural de papel?", ["Papeis", "Papels", "Papéis", "Papeles"], "C", "O plural de papel é papéis."),
            ("Qual é o plural de luz?", ["Luzes", "Luzis", "Luzes", "Luzs"], "A", "O plural de luz é luzes."),
            ("Qual é o plural de flor?", ["Flors", "Flores", "Floris", "Florezes"], "B", "O plural de flor é flores.")
        ],

        "Verbos": [
            ("Na frase 'Os alunos estudaram', qual é o verbo?", ["Alunos", "Os", "Estudaram", "Estudo"], "C", "Estudaram indica a ação realizada pelos alunos."),
            ("Qual alternativa apresenta um verbo no futuro?", ["Cantava", "Canto", "Cantarei", "Cantei"], "C", "Cantarei indica uma ação futura."),
            ("Na frase 'Ana corre todos os dias', qual é o verbo?", ["Ana", "Corre", "Todos", "Dias"], "B", "Corre é o verbo da frase."),
            ("Qual é o infinitivo do verbo 'escreveu'?", ["Escrevendo", "Escrever", "Escrevia", "Escrito"], "B", "Escrever é a forma infinitiva."),
            ("Qual alternativa apresenta um verbo no passado?", ["Brincará", "Brinca", "Brincou", "Brincar"], "C", "Brincou indica uma ação passada."),
            ("Na frase 'Nós viajaremos amanhã', em que tempo está o verbo?", ["Presente", "Passado", "Futuro", "Infinitivo"], "C", "Viajaremos indica uma ação futura.")
        ],

        "Antônimos": [
            ("Qual é o antônimo de abundante?", ["Farto", "Escasso", "Grande", "Numeroso"], "B", "Escasso indica algo em pouca quantidade."),
            ("Qual é o antônimo de corajoso?", ["Valente", "Destemido", "Medroso", "Ousado"], "C", "Medroso expressa o sentido oposto de corajoso."),
            ("Qual é o antônimo de expandir?", ["Ampliar", "Aumentar", "Reduzir", "Estender"], "C", "Reduzir significa diminuir."),
            ("Qual é o antônimo de antigo?", ["Velho", "Moderno", "Usado", "Histórico"], "B", "Moderno é o oposto de antigo."),
            ("Qual é o antônimo de aceitar?", ["Concordar", "Receber", "Recusar", "Permitir"], "C", "Recusar significa não aceitar."),
            ("Qual é o antônimo de otimista?", ["Esperançoso", "Confiante", "Pessimista", "Alegre"], "C", "Pessimista é o oposto de otimista.")
        ],

        "Interpretação": [
            ("Leia: 'Lucas levou um casaco porque a previsão indicava queda de temperatura.' Por que ele levou o casaco?", ["Porque faria calor", "Porque a temperatura diminuiria", "Porque iria chover", "Porque viajaria"], "B", "O texto informa que a temperatura iria cair."),
            ("Leia: 'Sofia economizou durante meses para comprar uma bicicleta.' O que Sofia fez antes da compra?", ["Gastou todo o dinheiro", "Pediu uma bicicleta", "Guardou dinheiro", "Vendeu a bicicleta"], "C", "Economizar significa guardar recursos."),
            ("Leia: 'A biblioteca estava fechada, então Pedro voltou para casa.' Por que Pedro voltou?", ["Estava cansado", "A biblioteca estava fechada", "Esqueceu o livro", "Estava chovendo"], "B", "A causa apresentada foi o fechamento da biblioteca."),
            ("Leia: 'Mesmo cansada, Júlia terminou o trabalho.' O que a expressão 'mesmo cansada' indica?", ["Uma condição que dificultava a tarefa", "Uma comemoração", "Uma ordem", "Uma dúvida"], "A", "A expressão indica uma dificuldade que não impediu Júlia de concluir o trabalho."),
            ("Leia: 'O trânsito estava intenso, por isso chegamos atrasados.' Qual foi a causa do atraso?", ["A chuva", "O trânsito intenso", "Uma reunião", "Uma caminhada"], "B", "O texto relaciona diretamente o trânsito intenso ao atraso."),
            ("Leia: 'Rafael apagou as luzes antes de sair para economizar energia.' Qual era o objetivo de Rafael?", ["Deixar a casa escura para sempre", "Economizar energia", "Encontrar um objeto", "Avisar os vizinhos"], "B", "O próprio texto apresenta a economia de energia como objetivo.")
        ],

        "Pontuação": [
            ("Qual frase apresenta pontuação adequada?", ["Você vem hoje.", "Você vem hoje?", "Você, vem hoje", "Você vem, hoje."], "B", "O ponto de interrogação indica uma pergunta."),
            ("Qual sinal geralmente encerra uma frase declarativa?", ["Vírgula", "Dois-pontos", "Ponto final", "Interrogação"], "C", "O ponto final encerra uma declaração."),
            ("Qual alternativa utiliza corretamente a vírgula em uma enumeração?", ["Comprei pão leite e queijo.", "Comprei pão, leite e queijo.", "Comprei, pão leite e queijo.", "Comprei pão leite, e queijo."], "B", "A vírgula separa os itens de uma enumeração."),
            ("Qual sinal é usado para indicar uma fala em diálogo?", ["Travessão", "Ponto final", "Vírgula", "Parênteses"], "A", "O travessão pode introduzir a fala de um personagem."),
            ("Qual frase expressa uma exclamação?", ["Que dia bonito!", "Que dia bonito?", "Que dia bonito.", "Que, dia bonito"], "A", "O ponto de exclamação expressa emoção ou intensidade."),
            ("Qual alternativa está pontuada corretamente?", ["Maria, venha aqui.", "Maria venha, aqui.", "Maria venha aqui,", "Maria; venha aqui,"], "A", "A vírgula separa o vocativo Maria do restante da frase.")
        ],

        "Concordância": [
            ("Qual frase apresenta concordância correta?", ["Os aluno chegaram.", "Os alunos chegaram.", "Os alunos chegou.", "O alunos chegaram."], "B", "O sujeito plural concorda com o verbo no plural."),
            ("Complete: 'As crianças _____ felizes.'", ["está", "estão", "estou", "esteve"], "B", "O sujeito plural exige o verbo estão."),
            ("Qual alternativa está correta?", ["A menina brincam.", "As menina brinca.", "As meninas brincam.", "A meninas brincam."], "C", "O artigo, o substantivo e o verbo concordam no plural."),
            ("Complete: 'Meu irmão e minha irmã _____ em casa.'", ["está", "estão", "estou", "estive"], "B", "O sujeito composto exige o verbo no plural."),
            ("Qual frase apresenta concordância nominal correta?", ["As casa bonitas.", "A casas bonita.", "As casas bonitas.", "As casas bonito."], "C", "O artigo, o substantivo e o adjetivo estão no feminino plural."),
            ("Complete: 'O professor e os alunos _____ presentes.'", ["estava", "estavam", "está", "estive"], "B", "O sujeito composto exige o verbo no plural.")
        ]
    }
}


def gerar_exercicios(materia, topico, nivel, quantidade=5):

    if materia not in BANCO_QUESTOES:
        raise ValueError("Matéria não encontrada no banco de questões.")

    if topico not in BANCO_QUESTOES[materia]:
        raise ValueError("Tópico não encontrado no banco de questões.")

    banco = BANCO_QUESTOES[materia][topico]

    if quantidade > len(banco):
        raise ValueError("Não há questões suficientes para essa quantidade.")

    questoes_selecionadas = random.sample(banco, quantidade)

    questoes = []

    for pergunta, alternativas, resposta_correta, explicacao in questoes_selecionadas:

        questoes.append({
            "pergunta": pergunta,
            "alternativas": {
                "A": alternativas[0],
                "B": alternativas[1],
                "C": alternativas[2],
                "D": alternativas[3]
            },
            "resposta_correta": resposta_correta,
            "explicacao": explicacao
        })

    return questoes
