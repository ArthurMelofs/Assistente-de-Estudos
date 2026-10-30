
document.addEventListener("DOMContentLoaded", () => {

    const areaQuestao = document.getElementById("area-questao");
    const contador = document.getElementById("contador");
    const porcentagem = document.getElementById("porcentagem");
    const barraProgresso = document.getElementById("barra-progresso");

    const botaoAnterior = document.getElementById("botao-anterior");
    const botaoProximo = document.getElementById("botao-proximo");
    const botaoFinalizar = document.getElementById("botao-finalizar");

    const campoNome = document.getElementById("nome-estudante");

    let questoes = [];
    let respostas = {};
    let questaoAtual = 0;


    // Busca as questões no backend
    async function carregarQuestoes() {

        try {

            const resposta = await fetch("/api/questoes");

            if (!resposta.ok) {
                throw new Error("Erro ao carregar questões.");
            }

            const dados = await resposta.json();

            questoes = dados.questoes;

            mostrarQuestao();

        } catch (erro) {

            console.error(erro);

            areaQuestao.textContent =
                "Não foi possível carregar a avaliação.";

        }
    }


    // Exibe a questão atual
    function mostrarQuestao() {

        const questao = questoes[questaoAtual];

        areaQuestao.innerHTML = "";

        const titulo = document.createElement("h3");

        titulo.textContent =
            questao.materia + " - " + questao.topico;

        const pergunta = document.createElement("p");

        pergunta.classList.add("pergunta");

        pergunta.textContent = questao.pergunta;

        areaQuestao.appendChild(titulo);
        areaQuestao.appendChild(pergunta);


        // Cria as alternativas
        Object.entries(questao.alternativas).forEach(
            ([letra, texto]) => {

                const label = document.createElement("label");

                label.classList.add("alternativa");

                const radio = document.createElement("input");

                radio.type = "radio";
                radio.name = "resposta";
                radio.value = letra;

                radio.checked =
                    respostas[questao.id] === letra;

                radio.addEventListener("change", () => {

                    respostas[questao.id] = letra;

                });

                const span = document.createElement("span");

                span.textContent = letra + ") " + texto;

                label.appendChild(radio);
                label.appendChild(span);

                areaQuestao.appendChild(label);

            }
        );


        atualizarProgresso();

        botaoAnterior.disabled = questaoAtual === 0;

        botaoProximo.hidden =
            questaoAtual === questoes.length - 1;

        botaoFinalizar.hidden =
            questaoAtual !== questoes.length - 1;

    }


    // Atualiza a barra de progresso
    function atualizarProgresso() {

        const total = questoes.length;

        const atual = questaoAtual + 1;

        const progresso = Math.round(
            (atual / total) * 100
        );

        contador.textContent =
            "Questão " + atual + " de " + total;

        porcentagem.textContent = progresso + "%";

        barraProgresso.style.width = progresso + "%";

    }


    // Vai para a questão anterior
    botaoAnterior.addEventListener("click", () => {

        if (questaoAtual > 0) {

            questaoAtual--;

            mostrarQuestao();

        }

    });


    // Vai para a próxima questão
    botaoProximo.addEventListener("click", () => {

        if (questaoAtual < questoes.length - 1) {

            questaoAtual++;

            mostrarQuestao();

        }

    });


    // Finaliza a avaliação
    botaoFinalizar.addEventListener("click", async () => {

        const totalRespondidas = Object.keys(respostas).length;

        if (totalRespondidas !== questoes.length) {

            alert("Responda todas as questões antes de finalizar.");

            return;

        }

        botaoFinalizar.disabled = true;

        botaoFinalizar.textContent = "Corrigindo...";


        const dadosEnvio = {

            nome: campoNome.value.trim() || "Estudante",

            respostas: respostas

        };


        try {

            const resposta = await fetch("/api/corrigir", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(dadosEnvio)

            });


            if (!resposta.ok) {

                throw new Error("Erro ao corrigir avaliação.");

            }


            const resultado = await resposta.json();

            localStorage.setItem(
                "studyia_resultado",
                JSON.stringify(resultado)
            );

            window.location.href = "/resultado";


        } catch (erro) {

            console.error(erro);

            alert("Não foi possível corrigir a avaliação.");

            botaoFinalizar.disabled = false;

            botaoFinalizar.textContent = "Finalizar avaliação";

        }

    });


    carregarQuestoes();

});
