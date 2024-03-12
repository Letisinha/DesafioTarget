for i in range(1, 10, 2):
    print(i)
# em range, o primeiro algarismo é o ponto de início, o segundo é o fim
# e o terceiro é o espaçamento entre eles

print('-'*30)

x = 1
while x <= 129:
    print(x)
    x *= 2
# sendo x igual a 1, enquanto x for menor ou igual a 129, x será multiplicado por 2

print('-'*30)

for item in range(8):
    print(item**2)
# até a oitava repetição, os números de 1 até 8 serão elevados à potência 2

print('-'*30)

for cup in range(2, 11, 2):
    print(cup**2)
# os números de 2 à 11 terão espaçamento de 2 e os números resultantes serão elevados à 2

print('-'*30)


def fibonacci(n):
    sequencia = [0, 1]
    # começamos a sequencia com 0 e 1
    while len(sequencia) < n:
        # enquanto a sequencia for menor do que n
        next_number = sequencia[-1] + sequencia[-2]
        # o proximo número será igual ao último número da sequencia representado por -1
        # adicionado do penultimo numero da sequencia representado pelo -2
        sequencia.append(next_number)
        # com o append adicionamos o proximo numero à lista
    return sequencia


n = 8
# numero de repetições desejadas
result = fibonacci(n)
print(result)

print('-'*30)

list = ['dois', 'dez', 'doze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'duzentos']
primeira_letra = 'd'
com_d = [x for x in list if x.startswith(primeira_letra)]
print('2, 10, 12, 16, 17, 18, 19, 200')
