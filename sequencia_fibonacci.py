# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
#  anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.




# Função que recebe como parâmetro a quantidade de resultados que o digitou. E retorna a sequência de Fibonacci.
def fibonacci(num):
    contador = 0
    t1, t2 =  1, 1
    array_fibonacci = []
    while contador < num:
        array_fibonacci.append(t1)
        t3 = t1 + t2
        t1 = t2
        t2 = t3
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