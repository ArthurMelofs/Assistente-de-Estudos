
document.addEventListener("DOMContentLoaded", () => {

    const resumo = document.getElementById("resumo-resultado");
    const desempenho = document.getElementById("desempenho");
    const listaReforcos = document.getElementById("lista-reforcos");

    const secaoExercicios = document.getElementById("secao-exercicios");
    const informacaoReforco = document.getElementById("informacao-reforco");
    const areaReforco = document.getElementById("area-reforco");


    // Recupera o resultado da avaliação
    const raw = localStorage.getItem("studyia_resultado");

    if (!raw) {

        resumo.textContent = "Nenhum resultado encontrado.";

        return;

    }

    const resultado = JSON.parse(raw);


    // Exibe o resumo geral
    function mostrarResumo() {

        resumo.innerHTML = "";

        const nome = document.createElement("h3");

        nome.textContent = resultado.nome;

        const pontuacao = document.createElement("p");

        pontuacao.textContent =
            "Acertos: " + resultado.acertos +
            " de " + resultado.total;

        const percentual = document.createElement("p");

        percentual.textContent =
            "Desempenho geral: " +
            resultado.percentual_geral + "%";

        const nivel = document.createElement("p");

        nivel.textContent =
            "Nível: " + resultado.nivel_geral;

        resumo.appendChild(nome);
        resumo.appendChild(pontuacao);
        resumo.appendChild(percentual);
        resumo.appendChild(nivel);

    }


    // Exibe o desempenho de cada conteúdo
    function mostrarDesempenho() {

        desempenho.innerHTML = "";

        resultado.desempenho.forEach((item) => {

            const card = document.createElement("article");

            card.classList.add("card");

            const titulo = document.createElement("h3");

            titulo.textContent =
                item.materia + " - " + item.topico;

            const acertos = document.createElement("p");

            acertos.textContent =
                item.acertos + " de " + item.total + " acertos";

            const percentual = document.createElement("p");

            percentual.textContent =
                item.percentual + "% de aproveitamento";

            const nivel = document.createElement("p");

            nivel.textContent =
                "Nível: " + item.nivel;

            card.appendChild(titulo);
            card.appendChild(acertos);
            card.appendChild(percentual);
            card.appendChild(nivel);

            desempenho.appendChild(card);

        });

    }


    // Exibe os conteúdos recomendados para reforço
    function mostrarReforcos() {

        listaReforcos.innerHTML = "";

        if (resultado.reforcos.length === 0) {

            listaReforcos.textContent =
                "Parabéns! Nenhum conteúdo precisa de reforço neste momento.";

            return;

        }


        resultado.reforcos.forEach((item) => {

            const card = document.createElement("article");

            card.classList.add("card");

            const titulo = document.createElement("h3");

            titulo.textContent =
                item.materia + " - " + item.topico;

            const nivel = document.createElement("p");

            nivel.textContent =
                "Seu nível atual: " + item.nivel;

            const botao = document.createElement("button");

            botao.type = "button";
            botao.classList.add("botao");

            botao.textContent = "Gerar exercícios";

            botao.addEventListener("click", () => {

                gerarExercicios(item);

            });

            card.appendChild(titulo);
            card.appendChild(nivel);
            card.appendChild(botao);

            listaReforcos.appendChild(card);

        });

    }


    // Solicita novos exercícios à IA
    async function gerarExercicios(item) {

        secaoExercicios.hidden = false;

        informacaoReforco.textContent =
            "Gerando exercícios de " +
            item.topico + "...";

        areaReforco.textContent =
            "Aguarde enquanto a inteligência artificial prepara as questões.";

        secaoExercicios.scrollIntoView({
            behavior: "smooth"
        });


        try {

            const resposta = await fetch("/api/reforco", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    materia: item.materia,

                    topico: item.topico,

                    nivel: item.nivel

                })

            });


            const dados = await resposta.json();

            if (!resposta.ok) {

                throw new Error(
                    dados.erro || "Erro ao gerar exercícios."
                );

            }


            informacaoReforco.textContent =
                item.materia + " - " + item.topico;

            iniciarExercicios(dados.questoes);


        } catch (erro) {

            console.error(erro);

            areaReforco.textContent = erro.message;

        }

    }


    // Controla a resolução dos exercícios
    function iniciarExercicios(questoes) {

        let questaoAtual = 0;
        let acertos = 0;

        mostrarExercicio();


        function mostrarExercicio() {

            areaReforco.innerHTML = "";

            const questao = questoes[questaoAtual];


            const contador = document.createElement("p");

            contador.textContent =
                "Questão " + (questaoAtual + 1) +
                " de " + questoes.length;


            const pergunta = document.createElement("h3");

            pergunta.textContent = questao.pergunta;


            areaReforco.appendChild(contador);
            areaReforco.appendChild(pergunta);


            const alternativas = document.createElement("div");

            alternativas.classList.add("alternativas");


            Object.entries(questao.alternativas).forEach(
                ([letra, texto]) => {

                    const botao = document.createElement("button");

                    botao.type = "button";
                    botao.classList.add("alternativa");

                    botao.textContent = letra + ") " + texto;

                    botao.addEventListener("click", () => {

                        corrigirExercicio(
                            letra,
                            alternativas
                        );

                    });

                    alternativas.appendChild(botao);

                }
            );


            areaReforco.appendChild(alternativas);

        }


        // Corrige a resposta selecionada
        function corrigirExercicio(resposta, alternativas) {

            const questao = questoes[questaoAtual];

            const botoes = alternativas.querySelectorAll("button");

            botoes.forEach((botao) => {

                botao.disabled = true;

            });


            const acertou =
                resposta === questao.resposta_correta;

            if (acertou) {

                acertos++;

            }


            const feedback = document.createElement("p");

            feedback.classList.add("feedback");

            feedback.textContent = acertou
                ? "Resposta correta!"
                : "Resposta incorreta. A resposta correta é " +
                  questao.resposta_correta + ".";


            const explicacao = document.createElement("p");

            explicacao.textContent =
                questao.explicacao;


            const botaoProximo = document.createElement("button");

            botaoProximo.type = "button";
            botaoProximo.classList.add("botao");

            botaoProximo.textContent =
                questaoAtual === questoes.length - 1
                    ? "Finalizar exercícios"
                    : "Próxima questão";


            areaReforco.appendChild(feedback);
            areaReforco.appendChild(explicacao);
            areaReforco.appendChild(botaoProximo);


            botaoProximo.addEventListener("click", () => {

                questaoAtual++;

                if (questaoAtual < questoes.length) {

                    mostrarExercicio();

                } else {

                    mostrarConclusao();

                }

            });

        }


        // Apresenta o resultado final do reforço
        function mostrarConclusao() {

            areaReforco.innerHTML = "";

            const titulo = document.createElement("h3");

            titulo.textContent = "Reforço concluído!";

            const resultadoFinal = document.createElement("p");

            resultadoFinal.textContent =
                "Você acertou " + acertos +
                " de " + questoes.length + " questões.";

            const percentual = Math.round(
                (acertos / questoes.length) * 100
            );

            const aproveitamento = document.createElement("p");

            aproveitamento.textContent =
                "Aproveitamento: " + percentual + "%";


            const botaoReiniciar = document.createElement("button");

            botaoReiniciar.type = "button";
            botaoReiniciar.classList.add("botao");

            botaoReiniciar.textContent =
                "Gerar novos exercícios";


            botaoReiniciar.addEventListener("click", () => {

                const item = resultado.reforcos.find(
                    (reforco) => reforco.topico === informacaoReforco.textContent.split(" - ")[1]
                );

                if (item) {

                    gerarExercicios(item);

                }

            });


            areaReforco.appendChild(titulo);
            areaReforco.appendChild(resultadoFinal);
            areaReforco.appendChild(aproveitamento);
            areaReforco.appendChild(botaoReiniciar);

        }

    }


    // Inicializa a página
    mostrarResumo();

    mostrarDesempenho();

    mostrarReforcos();

});
