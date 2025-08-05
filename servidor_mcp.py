# ==============================================================================
# SERVIDOR MCP DA CALCULADORA - VERSÃO FINAL E CORRIGIDA
# ==============================================================================
# Este arquivo Python cria um servidor local que expõe as funcionalidades de
# uma calculadora simples como "ferramentas" que podem ser chamadas pelo Gemini.
#
# A estrutura deste código foi ajustada para ser compatível com a forma como
# a biblioteca MCP gerencia seus próprios processos assíncronos internamente.

# --- 1. IMPORTAÇÃO DAS BIBLIOTECAS ---
# Aqui, importamos todos os "kits de ferramentas" (bibliotecas) que nosso programa precisa.

import asyncio
# 'asyncio' é a biblioteca do Python para "programação assíncrona".
# Nossas ferramentas (ex: somar_numeros) são definidas como 'async', pois
# a biblioteca MCP espera que elas possam realizar tarefas demoradas sem
# travar o servidor. O próprio servidor MCP irá gerenciar a execução
# dessas funções assíncronas.

import logging
# 'logging' é um sistema para registrar mensagens e eventos que acontecem no programa.
# É mais poderoso que um simples 'print()', pois permite classificar mensagens por
# importância (INFO para informação, ERROR para erros, etc.).

from typing import Any, Dict
# 'typing' nos ajuda a usar "dicas de tipo" (type hints). Elas nos permitem anotar
# qual tipo de dado uma variável ou função espera (ex: float, str).
# Isso não muda como o código roda, mas o torna mais claro para quem lê e ajuda
# a encontrar erros durante o desenvolvimento.

import sys
# 'sys' fornece acesso a variáveis e funções do sistema. Vamos usá-lo para
# ler argumentos da linha de comando (por exemplo, para rodar um modo de "teste").

# --- 2. IMPORTAÇÃO DOS MÓDULOS DO NOSSO PROJETO ---
# Agora importamos as partes específicas do nosso projeto.

from mcp.server.fastmcp import FastMCP
# 'FastMCP' é a classe principal da biblioteca MCP que usaremos para criar nosso servidor.
# Uma "classe" é como uma planta ou um projeto para criar objetos.

from calculadora import CalculadoraSimples
# 'CalculadoraSimples' é a nossa própria classe, definida em outro arquivo
# (provavelmente 'calculadora.py'), que contém a lógica das operações matemáticas.

# --- 3. CONFIGURAÇÃO INICIAL ---
# Bloco de código para preparações iniciais antes de o servidor rodar.

# Configura o sistema de logging para exibir mensagens a partir do nível INFO.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) # Cria um objeto "logger" para este arquivo.

# Criamos as "instâncias" dos objetos que vamos usar. Uma instância é um objeto
# funcional criado a partir do "projeto" de uma classe.
mcp_server = FastMCP("calculadora-mcp") # Instância do servidor, com um nome único.
calculadora = CalculadoraSimples()      # Instância da nossa calculadora.

# --- 4. DEFINIÇÃO DAS FERRAMENTAS (TOOLS) MCP ---
# Esta é a parte principal. Cada função aqui se tornará um comando que o Gemini
# pode executar. As funções são 'async def' porque o servidor MCP as executa
# em seu próprio loop de eventos assíncrono.

# O '@mcp_server.tool()' é um "decorador". Ele "decora" ou "embrulha" nossa função,
# adicionando a ela a capacidade de ser reconhecida e exposta pelo servidor MCP.
@mcp_server.tool()
async def somar_numeros(numero1: float, numero2: float) -> float:
    """
    Esta é uma 'docstring'. Ela descreve o que a ferramenta faz, seus argumentos
    e o que ela retorna. O Gemini lê esta docstring para entender como usar a ferramenta.
    É fundamental que ela seja clara e precisa.

    Args:
        numero1 (float): O primeiro número para a soma.
        numero2 (float): O segundo número para a soma.

    Returns:
        float: O resultado da soma.
    """
    # Usamos o logger para registrar o que está acontecendo internamente.
    # Essas mensagens aparecerão no console onde o servidor está rodando.
    logger.info(f"Ferramenta 'somar_numeros' chamada com: {numero1}, {numero2}")

    # Chamamos o método real da nossa classe Calculadora para fazer o cálculo.
    resultado = calculadora.somar(numero1, numero2)

    # O valor que a função 'return'a é o que será enviado de volta para o Gemini como resposta.
    return resultado

@mcp_server.tool()
async def subtrair_numeros(numero1: float, numero2: float) -> float:
    """Subtrai o segundo número do primeiro."""
    logger.info(f"Ferramenta 'subtrair_numeros' chamada com: {numero1}, {numero2}")
    resultado = calculadora.subtrair(numero1, numero2)
    return resultado

@mcp_server.tool()
async def dividir_numeros(numero1: float, numero2: float) -> float:
    """
    Divide o primeiro número pelo segundo.

    Raises:
        ValueError: Se a divisão por zero for tentada.
    """
    logger.info(f"Ferramenta 'dividir_numeros' chamada com: {numero1}, {numero2}")
    try:
        # Usamos um bloco 'try...except' para tratar erros de forma segura.
        # Se o código dentro do 'try' falhar, o bloco 'except' é executado,
        # impedindo que o servidor inteiro trave.
        resultado = calculadora.dividir(numero1, numero2)
        return resultado
    except ValueError as e:
        # Se ocorrer uma divisão por zero, nossa calculadora gera um 'ValueError'.
        # Nós o capturamos, registramos o erro e o "re-levantamos" (raise).
        # Isso informa ao MCP e ao Gemini que a operação falhou por um motivo específico.
        logger.error(f"Erro na divisão: {e}")
        raise e

@mcp_server.tool()
async def info_calculadora() -> str:
    """Retorna uma string com informações sobre as operações disponíveis."""
    logger.info("Ferramenta 'info_calculadora' chamada")
    info = calculadora.info()
    return info

# --- 5. FUNÇÃO PRINCIPAL E DE TESTE ---

# Esta função 'main' agora é SINCRONA (usa 'def' e não 'async def').
# A razão é que 'mcp_server.run()' é uma função "bloqueante": ela mesma
# cria e gerencia o loop de eventos e só termina quando o servidor é fechado.
# A nossa tarefa é apenas prepará-la e chamá-la.
def main():
    """
    Função principal que configura e inicia o servidor MCP.
    """
    logger.info("Iniciando servidor MCP da calculadora...")

    # Imprimimos um cabeçalho bonito no console para o usuário saber que o servidor iniciou.
    print("=" * 60)
    print("SERVIDOR MCP DA CALCULADORA")
    print("=" * 60)
    print("Servidor iniciado e aguardando conexões do Gemini CLI...")
    print("Para parar o servidor, pressione Ctrl+C no terminal.")
    print("=" * 60)

    try:
        # Esta é a linha que efetivamente inicia o servidor.
        # A chamada é direta, SEM 'await'. A partir deste ponto, o controle do
        # programa é entregue à biblioteca MCP, que ficará escutando por
        # solicitações até que o processo seja interrompido (com Ctrl+C).
        mcp_server.run(transport="stdio")

    except KeyboardInterrupt:
        # Este bloco é executado se o usuário pressionar Ctrl+C no terminal.
        logger.info("🛑 Servidor MCP interrompido pelo usuário.")
        print("\n🛑 Servidor MCP parado com sucesso!")
    except Exception as e:
        logger.error(f"❌ Erro inesperado no servidor MCP: {e}")
        print(f"\n❌ Erro no servidor: {e}")
        raise e

def testar_servidor():
    """
    Uma função de diagnóstico simples para verificar se a configuração está correta
    sem precisar iniciar o servidor de fato.
    """
    print("🧪 Testando configuração do servidor MCP...")
    try:
        CalculadoraSimples()
        print("✅ Instância da Calculadora criada com sucesso.")
        FastMCP("teste")
        print("✅ Instância do Servidor MCP criada com sucesso.")
        print("\n🎉 Teste básico concluído com sucesso!")
        print("💡 Para iniciar o servidor de verdade, execute: python servidor_mcp.py")
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")

# --- 6. PONTO DE ENTRADA DO SCRIPT ---
# Este bloco de código só é executado quando o arquivo é chamado diretamente
# pelo terminal (ex: `python servidor_mcp.py`).

# A variável especial `__name__` só é igual a `"__main__"` neste cenário.
# Isso impede que o servidor inicie caso este arquivo seja importado por outro.
if __name__ == "__main__":
    # Verificamos se foi passado um argumento na linha de comando.
    # `sys.argv` é a lista de argumentos. `sys.argv[0]` é sempre o nome do script.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Se o usuário rodou `python servidor_mcp.py test`, chamamos a função de teste.
        testar_servidor()
    else:
        # Caso contrário (execução normal), chamamos a função principal diretamente.
        # Não usamos mais 'asyncio.run()' porque, como explicado acima,
        # a biblioteca MCP cuida de todo o gerenciamento assíncrono.
        main()