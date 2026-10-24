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

A implementação segue o contrato definido em `specs/task_analyzer_spec.md`, sua transposição estruturada em `specs/requirements.yaml` e as regras de governança descritas em `CONTEXT_RULES.md`.

## Requisitos

Para execução local:

- Python 3.11 ou superior;
- pytest.

Para execução conteinerizada:

- Docker com suporte a Docker Compose.

As dependências Python autorizadas estão registradas em `requirements.txt`.

## Estrutura do projeto

```text
sdd-task-analyzer/
├── .github/
│   └── workflows/
│       └── ci.yml
├── specs/
│   ├── task_analyzer_spec.md
│   ├── requirements.yaml
│   └── system_design_document.pdf
├── src/
│   └── task_analyzer.py
├── tests/
│   └── test_harness.py
├── CONTEXT_RULES.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação local

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

A suíte contém quatro cenários automatizados:

- cenário de sucesso;
- validação de data inconsistente com `TaskValidationError`;
- entrada vazia;
- entrada contendo apenas tarefas pendentes.

## Integração contínua

O workflow `.github/workflows/ci.yml` utiliza GitHub Actions para validar automaticamente o projeto em `push` e `pull_request` direcionados às branches `main` e `develop`.

A automação executa em `ubuntu-latest`, configura Python 3.11, instala as dependências de `requirements.txt` e roda:

```bash
python -m pytest -v tests/test_harness.py
```

O projeto implementa integração contínua para testes; não há etapa automatizada de implantação em produção.

## Docker

O `Dockerfile` utiliza `python:3.11-slim`, instala as dependências e executa o Test Harness como comando padrão.

Para construir a imagem:

```bash
docker build -t sdd-task-analyzer .
```

Para executar os testes no container:

```bash
docker run --rm sdd-task-analyzer
```

## Docker Compose

O `docker-compose.yml` define o serviço `tests` e reutiliza o Dockerfile do projeto.

Para construir e executar a suíte em ambiente isolado:

```bash
docker compose up --build --abort-on-container-exit
```

A validação realizada com Docker Compose concluiu os quatro testes com sucesso e código de saída 0.

## Documentação e governança

- `specs/task_analyzer_spec.md`: contrato SDD original e fonte normativa de negócio;
- `specs/requirements.yaml`: transposição estruturada do contrato;
- `specs/system_design_document.pdf`: documentação consolidada do desenho do sistema;
- `CONTEXT_RULES.md`: regras arquiteturais, proibições e diretrizes para uso de IA;
- `src/task_analyzer.py`: implementação de `TaskValidationError` e `analyze_tasks`;
- `tests/test_harness.py`: suíte automatizada de testes com pytest.

O código gerado ou alterado com apoio de IA permanece sujeito à revisão humana, ao contrato SDD e às `CONTEXT_RULES`.

## Versionamento

O desenvolvimento utiliza branches de funcionalidade e documentação, commits pequenos e descritivos e Pull Requests para revisão antes da integração à branch `main`.
