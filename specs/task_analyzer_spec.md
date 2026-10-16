# TaskAnalyzer SDD Specification

## 1. Objetivo

O `TaskAnalyzer` é um módulo destinado à análise de tarefas para geração de métricas de produtividade. A implementação desta fase deve seguir estritamente este contrato e as regras definidas em `CONTEXT_RULES.md`.

## 2. Interface Pública

### 2.1 Exceção customizada

A implementação deve disponibilizar a exceção pública:

```python
class TaskValidationError(Exception):
    ...
```

Ela deve ser utilizada para sinalizar dados de tarefa inválidos previstos neste contrato.

### 2.2 Função principal

A implementação deve disponibilizar a função pública:

```python
def analyze_tasks(tasks: list[dict[str, object]]) -> dict[str, object]:
    ...
```

A função recebe uma lista de tarefas e retorna um dicionário com as métricas definidas neste documento.

## 3. Dados de Entrada

Cada tarefa deve ser representada por um dicionário contendo os seguintes campos:

- `id_tarefa`: identificador inteiro e positivo da tarefa.
- `data_criacao`: data e hora de criação da tarefa.
- `data_inicio`: data e hora de início da tarefa, quando disponível.
- `data_conclusao`: data e hora de conclusão da tarefa, quando disponível.
- `prazo`: data e hora limite da tarefa.
- `prioridade`: uma entre `"baixa"`, `"media"` ou `"alta"`.
- `status`: uma entre `"concluida"`, `"pendente"` ou `"cancelada"`.

As datas devem ser tratadas de forma consistente e comparável.

## 4. Saída Esperada

O retorno de `analyze_tasks` deve conter, no mínimo:

- `total_tarefas`: quantidade total de tarefas recebidas.
- `total_concluidas`: quantidade de tarefas com status `"concluida"`.
- `total_pendentes`: quantidade de tarefas com status `"pendente"`.
- `tempo_medio_conclusao_horas`: média geral do tempo de conclusão das tarefas concluídas, em horas.
- `taxa_atraso_percentual`: percentual de tarefas concluídas após o prazo.
- `por_prioridade`: métricas agrupadas por prioridade.

Em `por_prioridade`, cada prioridade presente deve permitir validar ao menos a média de tempo de conclusão correspondente.

## 5. Regras de Negócio

1. O total de tarefas corresponde ao número de itens recebidos pela função.
2. `total_concluidas` considera apenas tarefas com status `"concluida"`.
3. `total_pendentes` considera apenas tarefas com status `"pendente"`.
4. O tempo de conclusão deve ser calculado apenas para tarefas concluídas com os dados necessários para o cálculo.
5. O tempo médio de conclusão deve ser expresso em horas.
6. A taxa de atraso deve considerar uma tarefa atrasada quando sua `data_conclusao` for posterior ao `prazo`.
7. A função deve produzir também métricas por prioridade, incluindo o tempo médio de conclusão por prioridade.
8. Se não houver tarefas concluídas, as médias relacionadas à conclusão devem retornar `0.0`.
9. Entradas vazias devem ser tratadas sem exceções não previstas e devem retornar métricas numéricas zeradas quando aplicável.
10. Uma tarefa com `data_conclusao` anterior à `data_criacao` é inválida e deve disparar `TaskValidationError`.
11. A implementação deve prevenir divisão por zero.
12. Valores médios e percentuais devem ser retornados como números de ponto flutuante.

## 6. Cenários de Aceite da Fase 2

### Cenário 1 — Sucesso

**Dado** um conjunto válido de tarefas contendo tarefas concluídas e pendentes, com diferentes prioridades e prazos,  
**Quando** `analyze_tasks` for executada,  
**Então** o resultado deve apresentar corretamente `total_tarefas`, `total_concluidas`, `total_pendentes`, `tempo_medio_conclusao_horas`, `taxa_atraso_percentual` e as métricas por prioridade.

### Cenário 2 — Exceção/Erro

**Dado** uma tarefa em que `data_conclusao < data_criacao`,  
**Quando** `analyze_tasks` for executada,  
**Então** deve ser lançada a exceção `TaskValidationError`.

### Casos de borda

- Lista de tarefas vazia.
- Lista contendo apenas tarefas pendentes.
- Ausência de tarefas concluídas para cálculo de médias.

Nesses casos, a implementação deve evitar divisão por zero e retornar `0.0` para médias sem lançar exceções não tratadas.

## 7. Restrições

- A implementação deve utilizar Python 3.11 ou superior.
- Todas as funções e parâmetros devem possuir type hints.
- O código deve respeitar integralmente o arquivo `CONTEXT_RULES.md`.
- Não deve haver persistência em arquivos ou banco de dados.
- Não devem ser adicionados comportamentos não previstos neste contrato.
