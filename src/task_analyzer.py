"""Análise de tarefas e geração de métricas de produtividade."""

from datetime import datetime


PRIORIDADES_VALIDAS = {"baixa", "media", "alta"}
STATUS_VALIDOS = {"concluida", "pendente", "cancelada"}


class TaskValidationError(Exception):
    """Exceção utilizada para indicar dados de tarefa inválidos."""


def _validar_data(
    valor: object,
    nome_campo: str,
    opcional: bool = False,
) -> datetime | None:
    """Valida um campo de data.

    Args:
        valor: Valor recebido no campo.
        nome_campo: Nome do campo validado.
        opcional: Indica se o campo pode receber None.

    Returns:
        A data validada ou None quando permitido.

    Raises:
        TaskValidationError: Se o valor informado for inválido.
    """
    if valor is None and opcional:
        return None

    if not isinstance(valor, datetime):
        raise TaskValidationError(
            f"O campo '{nome_campo}' deve ser do tipo datetime."
        )

    return valor


def _validar_tarefa(tarefa: dict[str, object]) -> None:
    """Valida uma tarefa antes de sua análise.

    Args:
        tarefa: Dados da tarefa.

    Raises:
        TaskValidationError: Se algum dado obrigatório for inválido.
    """
    campos_obrigatorios = {
        "id_tarefa",
        "data_criacao",
        "prazo",
        "prioridade",
        "status",
    }

    campos_ausentes = campos_obrigatorios - tarefa.keys()

    if campos_ausentes:
        raise TaskValidationError(
            f"Campos obrigatórios ausentes: {sorted(campos_ausentes)}."
        )

    id_tarefa = tarefa["id_tarefa"]
    if not isinstance(id_tarefa, int) or id_tarefa <= 0:
        raise TaskValidationError(
            "O campo 'id_tarefa' deve ser um inteiro positivo."
        )

    prioridade = tarefa["prioridade"]
    if prioridade not in PRIORIDADES_VALIDAS:
        raise TaskValidationError("Prioridade inválida.")

    status = tarefa["status"]
    if status not in STATUS_VALIDOS:
        raise TaskValidationError("Status inválido.")

    data_criacao = _validar_data(
        tarefa["data_criacao"],
        "data_criacao",
    )
    _validar_data(tarefa["prazo"], "prazo")

    data_inicio = _validar_data(
        tarefa.get("data_inicio"),
        "data_inicio",
        opcional=True,
    )
    data_conclusao = _validar_data(
        tarefa.get("data_conclusao"),
        "data_conclusao",
        opcional=True,
    )

    if (
        data_conclusao is not None
        and data_criacao is not None
        and data_conclusao < data_criacao
    ):
        raise TaskValidationError(
            "A data de conclusão não pode ser anterior à data de criação."
        )

    if status == "concluida" and (
        data_inicio is None or data_conclusao is None
    ):
        raise TaskValidationError(
            "Tarefas concluídas devem possuir data de início e conclusão."
        )


def _media(valores: list[float]) -> float:
    """Calcula uma média sem risco de divisão por zero.

    Args:
        valores: Valores utilizados no cálculo.

    Returns:
        Média dos valores ou 0.0 quando a lista estiver vazia.
    """
    if not valores:
        return 0.0

    return round(sum(valores) / len(valores), 2)


def analyze_tasks(
    tasks: list[dict[str, object]],
) -> dict[str, object]:
    """Analisa tarefas e retorna métricas de produtividade.

    Args:
        tasks: Lista de tarefas a serem analisadas.

    Returns:
        Dicionário contendo as métricas definidas no contrato SDD.

    Raises:
        TaskValidationError: Se uma tarefa possuir dados inválidos.
    """
    for tarefa in tasks:
        _validar_tarefa(tarefa)

    concluidas = [
        tarefa
        for tarefa in tasks
        if tarefa["status"] == "concluida"
    ]

    total_pendentes = sum(
        tarefa["status"] == "pendente"
        for tarefa in tasks
    )

    tempos_conclusao: list[float] = []
    tarefas_atrasadas = 0

    tempos_por_prioridade: dict[str, list[float]] = {
        prioridade: []
        for prioridade in PRIORIDADES_VALIDAS
    }

    for tarefa in concluidas:
        data_inicio = tarefa["data_inicio"]
        data_conclusao = tarefa["data_conclusao"]
        prazo = tarefa["prazo"]
        prioridade = tarefa["prioridade"]

        if (
            isinstance(data_inicio, datetime)
            and isinstance(data_conclusao, datetime)
            and isinstance(prazo, datetime)
            and isinstance(prioridade, str)
        ):
            tempo_horas = (
                data_conclusao - data_inicio
            ).total_seconds() / 3600

            tempos_conclusao.append(tempo_horas)
            tempos_por_prioridade[prioridade].append(tempo_horas)

            if data_conclusao > prazo:
                tarefas_atrasadas += 1

    total_concluidas = len(concluidas)

    taxa_atraso = (
        round(
            tarefas_atrasadas / total_concluidas * 100,
            2,
        )
        if total_concluidas
        else 0.0
    )

    por_prioridade = {
        prioridade: {
            "tempo_medio_conclusao_horas": _media(tempos),
        }
        for prioridade, tempos in tempos_por_prioridade.items()
    }

    return {
        "total_tarefas": len(tasks),
        "total_concluidas": total_concluidas,
        "total_pendentes": total_pendentes,
        "tempo_medio_conclusao_horas": _media(tempos_conclusao),
        "taxa_atraso_percentual": taxa_atraso,
        "por_prioridade": por_prioridade,
    }
