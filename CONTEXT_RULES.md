# CONTEXT_RULES

## 1. Diretrizes Arquiteturais Obrigatórias

- Utilizar Python 3.11 ou superior.
- Utilizar type hints em 100% das funções, métodos e parâmetros.
- Seguir a PEP 8 e as boas práticas da linguagem Python.
- Criar funções pequenas, coesas e com responsabilidade única.
- Utilizar Google Style Docstrings em módulos, classes e funções, documentando parâmetros, retornos e exceções quando aplicável.
- Utilizar tratamento de exceções específicas, com mensagens claras e compreensíveis.
- Prevenir operações inválidas, incluindo divisão por zero.
- Utilizar o módulo padrão `logging` quando houver necessidade de registrar eventos da aplicação.
- Utilizar nomes claros e descritivos para funções, variáveis, classes e demais elementos do código.
- Separar responsabilidades seguindo o princípio de responsabilidade única, evitando concentração excessiva de lógica em scripts ou funções extensas.
- Priorizar código legível, simples e de fácil manutenção.

## 2. Proibições Explícitas

- Não utilizar bibliotecas externas não autorizadas pelo projeto.
- Não alterar, remover ou adaptar os cenários de teste definidos na especificação sem autorização.
- Não modificar a estrutura de arquivos e diretórios definida para o repositório.
- Não implementar persistência em arquivos ou bancos de dados.
- Não alterar assinaturas de funções públicas sem autorização.
- Não criar funcionalidades novas sem testes correspondentes.
- Não duplicar código ou adicionar trechos desnecessários.
- Não assumir comportamentos que não estejam definidos no contrato de negócio.
- Não comentar o código em excesso; utilizar comentários apenas quando realmente necessários.
- Não retornar valores diferentes do contrato definido.

## 3. Regras de Interação com Assistentes de IA

- Fornecer ao assistente o contexto completo relevante antes de solicitar geração ou alteração de código.
- Confirmar que o assistente compreendeu o contrato de negócio e estas regras antes da geração da implementação.
- Solicitar explicações quando houver dúvida sobre uma decisão técnica ou comportamento gerado.
- Revisar criticamente todo código produzido por IA antes de aceitá-lo.
- Rejeitar ou corrigir qualquer resposta que viole estas regras, a especificação SDD ou os requisitos atuais da atividade.
- A decisão final de homologação do código permanece sob responsabilidade humana.
