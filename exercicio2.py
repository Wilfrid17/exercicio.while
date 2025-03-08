vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 4]
    ]

vendas = []

while True:
    produto = input("Qual o produto? ")
    if not produto:
        break
    quantidade = input("Qual a quantidade? ")
    vendas.append([produto, quantidade])
print(vendas)