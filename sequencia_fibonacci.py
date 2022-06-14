
# Função que recebe como parâmetro a quantidade de resultados que o usuário deseja.
# E aplica a sequência de Fibonacci.
def fibonacci(num):

    contador = 0
    a, b =  1, 1
    array_fibonacci = []
    while contador < num:
        array_fibonacci.append(a)
        c = a + b
        a = b
        b = c
        contador += 1
    return array_fibonacci

if __name__ == "__main__":
    num = int(input("Digite o numero para calcular a sequência de Fibonacci: "))
    resultado_fibonacci = fibonacci(num)
    # Imprime o resultado para o usuário.
    print(f'O resultado da sequência foi: {", ".join(str(num) for num in resultado_fibonacci)}')
    # Verifica se o número informado está dentro da sequência de Fibonacci.
    if num in resultado_fibonacci:
        print(f'O numero {num} está na sequência de Fibonacci.')
    else:
        print(f'O numero {num} não está na sequência de Fibonacci.')