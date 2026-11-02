# ==============================================================================
# CALCULADORA SIMPLES EM PYTHON
# Operações: Adição, Subtração, Multiplicação, Divisão e Porcentagem
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DEFINIÇÃO DAS FUNÇÕES MATEMÁTICAS
# Cada função recebe dois valores (a, b) e retorna o resultado da operação.
# ------------------------------------------------------------------------------

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração do segundo número em relação ao primeiro."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto da multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """
    Retorna a divisão do primeiro número pelo segundo.
    Inclui validação defensiva para evitar o erro de divisão por zero.
    """
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def porcentagem(a, b):
    """
    Retorna o valor da porcentagem de um número em relação ao outro (a% de b).
    Exemplo: 20% de 200 = (20 * 200) / 100 = 40.0
    """
    return (a * b) / 100

# ------------------------------------------------------------------------------
# 2. FUNÇÃO PRINCIPAL DA CALCULADORA
# Gerencia o menu, entrada de dados e lógica de decisão.
# ------------------------------------------------------------------------------

def calculadora():
    print("=" * 40)
    print("      BEM-VINDO À CALCULADORA PYTHON    ")
    print("=" * 40)
    print("Selecione a operação desejada:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Porcentagem (%)")
    print("=" * 40)

    # 3. RECEBENDO A OPÇÃO DO USUÁRIO
    # O input() sempre retorna texto (string 'str')
    opcao = input("Digite o número da operação (1/2/3/4/5): ").strip()

    # 4. VALIDAÇÃO DA OPÇÃO
    # Verificamos se a opção escolhida existe antes de pedir os números
    if opcao in ['1', '2', '3', '4', '5']:
        # 5. RECEBENDO E CONVERTENDO OS NÚMEROS
        # Usamos float() para aceitar números inteiros e decimais
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("\nErro: Por favor, digite apenas números válidos!")
            return

        # 6. ESTRUTURA CONDICIONAL (IF / ELIF / ELSE)
        # Identifica a operação escolhida e executa a função correspondente
        if opcao == '1':
            resultado = somar(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}")

        elif opcao == '2':
            resultado = subtrair(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}")

        elif opcao == '3':
            resultado = multiplicar(num1, num2)
            print(f"\nResultado: {num1} * {num2} = {resultado}")

        elif opcao == '4':
            resultado = dividir(num1, num2)
            print(f"\nResultado: {num1} / {num2} = {resultado}")

        elif opcao == '5':
            resultado = porcentagem(num1, num2)
            print(f"\nResultado: {num1}% de {num2} = {resultado}")

    else:
        # Caso o usuário digite uma opção fora de 1 a 5
        print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")

# ------------------------------------------------------------------------------
# 7. PONTO DE ENTRADA DO PROGRAMA
# Inicia a execução chamando a função principal
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    calculadora()
