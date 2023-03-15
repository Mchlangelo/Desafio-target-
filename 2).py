"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

valor1 = 0
valor2 = 1
valor3 = 0
n = int(input('Digite um número: '))
while n > valor3:
  valor3 = valor1 + valor2
  valor1 = valor2
  valor2 = valor3
if n == 0 or n == 1:
    print ('O número pertence à sequência de Fibonacci.')
elif n == valor3:
    print ('O número pertence à sequência de Fibonacci.')
else:
    print ('O número não pertence à sequência de Fibonacci.')