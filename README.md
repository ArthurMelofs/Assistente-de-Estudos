# StudyIA — MVP inicial

## Requisitos
- Python 3.10 ou superior
- Flask

## Executar no Windows / VS Code
1. Extraia o ZIP e abra a pasta no VS Code.
2. No terminal, crie um ambiente virtual (recomendado):
   `py -m venv .venv`
3. Ative:
   `.\.venv\Scriptsctivate`
4. Instale Flask:
   `py -m pip install flask`
5. Execute:
   `py app.py`
6. Abra `http://127.0.0.1:5000`

## O que está implementado
- Página inicial responsiva.
- Avaliação diagnóstica com 13 questões: 8 de Matemática e 5 de Português.
- Correção no backend.
- Resultado geral, por matéria e por tópico.
- Classificação inicial por faixa de aproveitamento.
- Recomendações baseadas nos erros.
- Exercícios adicionais por tópico.
- Chatbot demonstrativo com respostas programadas.

## Estrutura
- `app.py`: rotas, questões, correção, recomendações e chatbot.
- `templates/`: páginas HTML.
- `static/css/style.css`: estilos.
- `static/js/avaliacao.js`: fluxo da avaliação.
- `static/js/resultado.js`: resultado e exercícios.
- `static/js/main.js`: chatbot.

## Limitações
- O chatbot ainda não é IA generativa; usa regras e respostas programadas.
- Os resultados são guardados no `localStorage` do navegador, sem login e sem histórico centralizado.
- A classificação é uma regra de protótipo, não uma escala pedagógica validada.
- Não há Machine Learning nesta versão.

## Próximas etapas
1. Salvar alunos, tentativas e exercícios em SQLite.
2. Integrar API de LLM no backend (nunca expor a chave no JavaScript).
3. Guardar histórico e comparar evolução.
4. Ampliar e revisar o banco de questões.
