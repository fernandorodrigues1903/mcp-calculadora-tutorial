# calculadora.py
# Este arquivo contém nossa calculadora simples que será exposta via MCP

# Importamos a biblioteca 'logging' para registrar informações sobre o que está acontecendo
# É como um "diário" do programa que nos ajuda a entender o que está funcionando
import logging

# Configuramos o sistema de logging para mostrar informações úteis
# Isso nos ajudará a debugar problemas se algo der errado
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CalculadoraSimples:
    """
    Esta é nossa classe Calculadora.
    Uma classe é como um "molde" ou "blueprint" que define como nossa calculadora funciona.
    
    Pense na classe como a "receita" de uma calculadora, e quando criamos uma instância
    da classe, é como se estivéssemos "assando" uma calculadora real usando essa receita.
    """
    
    def __init__(self):
        """
        Este é o método __init__ (inicializador).
        Ele é executado automaticamente quando criamos uma nova calculadora.
        É como "ligar" a calculadora pela primeira vez.
        """
        logger.info("Calculadora inicializada com sucesso!")
        print("Calculadora MCP iniciada - Pronta para calcular!")
    
    def somar(self, numero1: float, numero2: float) -> float:
        """
        Função para somar dois números.
        
        Parâmetros:
        - numero1 (float): O primeiro número a ser somado
        - numero2 (float): O segundo número a ser somado
        
        Retorna:
        - float: O resultado da soma
        
        Exemplo: somar(5, 3) retorna 8
        """
        # Registramos no log que a operação está sendo executada
        logger.info(f"Executando soma: {numero1} + {numero2}")
        
        # Realizamos a operação matemática
        resultado = numero1 + numero2
        
        # Registramos o resultado no log
        logger.info(f"Resultado da soma: {resultado}")
        
        # Retornamos o resultado
        return resultado
    
    def subtrair(self, numero1: float, numero2: float) -> float:
        """
        Função para subtrair dois números.
        
        Parâmetros:
        - numero1 (float): O número do qual vamos subtrair (minuendo)
        - numero2 (float): O número que vamos subtrair (subtraendo)
        
        Retorna:
        - float: O resultado da subtração
        
        Exemplo: subtrair(10, 3) retorna 7
        """
        # Registramos no log que a operação está sendo executada
        logger.info(f"Executando subtração: {numero1} - {numero2}")
        
        # Realizamos a operação matemática
        resultado = numero1 - numero2
        
        # Registramos o resultado no log
        logger.info(f"Resultado da subtração: {resultado}")
        
        # Retornamos o resultado
        return resultado
    
    def dividir(self, numero1: float, numero2: float) -> float:
        """
        Função para dividir dois números.
        
        Esta função inclui proteção contra divisão por zero, que é um erro matemático.
        Dividir por zero é impossível e causaria um erro no programa.
        
        Parâmetros:
        - numero1 (float): O número que será dividido (dividendo)
        - numero2 (float): O número pelo qual vamos dividir (divisor)
        
        Retorna:
        - float: O resultado da divisão
        
        Levanta:
        - ValueError: Se tentarmos dividir por zero
        
        Exemplo: dividir(10, 2) retorna 5
        """
        # Registramos no log que a operação está sendo executada
        logger.info(f"Executando divisão: {numero1} ÷ {numero2}")
        
        # Verificamos se o segundo número é zero
        # Se for, não podemos dividir e precisamos avisar sobre o erro
        if numero2 == 0:
            error_msg = "Erro: Não é possível dividir por zero!"
            logger.error(error_msg)
            # Levantamos uma exceção (erro) com uma mensagem explicativa
            raise ValueError(error_msg)
        
        # Se chegamos aqui, é seguro fazer a divisão
        resultado = numero1 / numero2
        
        # Registramos o resultado no log
        logger.info(f"Resultado da divisão: {resultado}")
        
        # Retornamos o resultado
        return resultado
    
    def info(self) -> str:
        """
        Função que retorna informações sobre a calculadora.
        
        Retorna:
        - str: Uma string com informações sobre as operações disponíveis
        """
        info_text = """
        🧮 Calculadora MCP - Informações:
        
        Operações disponíveis:
        1. Somar: Adiciona dois números
        2. Subtrair: Subtrai o segundo número do primeiro
        3. Dividir: Divide o primeiro número pelo segundo (protegido contra divisão por zero)
        
        Todas as operações aceitam números decimais (float).
        """
        return info_text

# Função de teste para verificar se nossa calculadora está funcionando
def testar_calculadora():
    """
    Esta função testa nossa calculadora para garantir que está funcionando corretamente.
    É como fazer um "teste de qualidade" antes de usar a calculadora de verdade.
    """
    print("🧪 Iniciando testes da calculadora...")
    
    # Criamos uma instância (uma "cópia") da nossa calculadora
    calc = CalculadoraSimples()
    
    # Testamos cada operação
    try:
        # Teste da soma
        resultado_soma = calc.somar(10, 5)
        print(f"✅ Teste soma: 10 + 5 = {resultado_soma}")
        
        # Teste da subtração
        resultado_subtracao = calc.subtrair(10, 3)
        print(f"✅ Teste subtração: 10 - 3 = {resultado_subtracao}")
        
        # Teste da divisão
        resultado_divisao = calc.dividir(15, 3)
        print(f"✅ Teste divisão: 15 ÷ 3 = {resultado_divisao}")
        
        # Teste da proteção contra divisão por zero
        print("🧪 Testando proteção contra divisão por zero...")
        try:
            calc.dividir(10, 0)
        except ValueError as e:
            print(f"✅ Proteção funcionando: {e}")
        
        print("🎉 Todos os testes passaram! A calculadora está funcionando corretamente.")
        
    except Exception as e:
        print(f"❌ Erro durante os testes: {e}")

# Esta parte só executa se rodarmos este arquivo diretamente
# (não quando ele for importado por outro arquivo)
if __name__ == "__main__":
    print("🚀 Executando calculadora.py diretamente")
    testar_calculadora()