def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        next_number = sequencia[-1] + sequencia[-2]
        sequencia.append(next_number)
    return sequencia


n = 20
result = fibonacci(n)
valor = 144

if valor in result:
    print(valor, "pertence à fibonacci")
if valor not in result:
    print(valor, "não pertence à fibonacci")
