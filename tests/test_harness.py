"""Testes automatizados do TaskAnalyzer."""

from datetime import datetime

import pytest

from src.task_analyzer import TaskValidationError, analyze_tasks


def test_analyze_tasks_sucesso() -> None:
    """Valida as métricas gerais e por prioridade."""
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": datetime(2026, 10, 1, 8),
            "data_inicio": datetime(2026, 10, 1, 9),
            "data_conclusao": datetime(2026, 10, 1, 11),
            "prazo": datetime(2026, 10, 1, 12),
            "prioridade": "alta",
            "status": "concluida",
        },
        {
            "id_tarefa": 2,
            "data_criacao": datetime(2026, 10, 2, 8),
            "data_inicio": datetime(2026, 10, 2, 10),
            "data_conclusao": datetime(2026, 10, 2, 14),
            "prazo": datetime(2026, 10, 2, 13),
            "prioridade": "baixa",
            "status": "concluida",
        },
        {
            "id_tarefa": 3,
            "data_criacao": datetime(2026, 10, 3, 8),
            "data_inicio": None,
            "data_conclusao": None,
            "prazo": datetime(2026, 10, 4, 8),
            "prioridade": "media",
            "status": "pendente",
        },
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_tarefas"] == 3
    assert resultado["total_concluidas"] == 2
    assert resultado["total_pendentes"] == 1
    assert resultado["tempo_medio_conclusao_horas"] == 3.0
    assert resultado["taxa_atraso_percentual"] == 50.0

    assert resultado["por_prioridade"]["alta"][
        "tempo_medio_conclusao_horas"
    ] == 2.0

    assert resultado["por_prioridade"]["baixa"][
        "tempo_medio_conclusao_horas"
    ] == 4.0

    assert resultado["por_prioridade"]["media"][
        "tempo_medio_conclusao_horas"
    ] == 0.0


def test_analyze_tasks_data_inconsistente() -> None:
    """Valida a exceção para data de conclusão anterior à criação."""
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": datetime(2026, 10, 10, 10),
            "data_inicio": datetime(2026, 10, 10, 8),
            "data_conclusao": datetime(2026, 10, 10, 9),
            "prazo": datetime(2026, 10, 10, 12),
            "prioridade": "alta",
            "status": "concluida",
        }
    ]

    with pytest.raises(TaskValidationError):
        analyze_tasks(tarefas)


def test_analyze_tasks_lista_vazia() -> None:
    """Valida o comportamento para uma entrada vazia."""
    resultado = analyze_tasks([])

    assert resultado["total_tarefas"] == 0
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0


def test_analyze_tasks_apenas_pendentes() -> None:
    """Valida médias zeradas quando não existem tarefas concluídas."""
    tarefas = [
        {
            "id_tarefa": 1,
            "data_criacao": datetime(2026, 10, 1, 8),
            "data_inicio": None,
            "data_conclusao": None,
            "prazo": datetime(2026, 10, 2, 8),
            "prioridade": "media",
            "status": "pendente",
        }
    ]

    resultado = analyze_tasks(tarefas)

    assert resultado["total_tarefas"] == 1
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 1
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0
