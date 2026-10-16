# sdd-task-analyzer

Projeto desenvolvido para a disciplina **Bootcamp III**, seguindo uma abordagem de **Spec-Driven Development (SDD)** com apoio de assistentes de Inteligência Artificial.

## Objetivo

O `TaskAnalyzer` analisa dados de tarefas e gera métricas de produtividade, incluindo:

- total de tarefas;
- total de tarefas concluídas;
- total de tarefas pendentes;
- tempo médio de conclusão em horas;
- taxa de atraso;
- métricas de tempo médio agrupadas por prioridade.

A implementação segue o contrato definido em `specs/task_analyzer_spec.md` e as regras de governança descritas em `CONTEXT_RULES.md`.

## Requisitos

- Python 3.11 ou superior;
- pytest.

As dependências autorizadas estão registradas em `requirements.txt`.

## Estrutura do projeto

```text
sdd-task-analyzer/
├── README.md
├── CONTEXT_RULES.md
├── .gitignore
├── requirements.txt
├── specs/
│   └── task_analyzer_spec.md
├── tests/
│   └── test_harness.py
└── src/
    └── task_analyzer.py
```

## Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/eduardotrm/sdd-task-analyzer.git
cd sdd-task-analyzer
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução dos testes

Execute o Test Harness a partir da raiz do projeto:

```bash
python -m pytest -v tests/test_harness.py
```

## Status dos testes

Última validação realizada no Google Colab com Python 3.13.16:

```text
4 passed
```

Os testes cobrem:

- cenário de sucesso;
- validação de data inconsistente com `TaskValidationError`;
- entrada vazia;
- entrada contendo apenas tarefas pendentes.

## Arquivos principais

- `src/task_analyzer.py`: implementação de `TaskValidationError` e `analyze_tasks`;
- `tests/test_harness.py`: suíte automatizada de testes com pytest;
- `specs/task_analyzer_spec.md`: contrato SDD utilizado na implementação;
- `CONTEXT_RULES.md`: regras de contexto e governança para uso de IA.

## Versionamento

O desenvolvimento utiliza branches de funcionalidade, commits pequenos e descritivos e Pull Requests para revisão antes da integração à branch `main`.
