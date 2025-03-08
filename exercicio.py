produto = input("Regitre um produto. Para cancela o registro de novo produto, basta apertar enter com caixa vazia: ")
vendas = []

while produto != '':
    vendas.append(produto)
    produto = input("Regitre um produto. Para cancela o registro de novo produto, basta apertar enter com caixa vazia: ")

print(f"Registro Finalizado. As vdndas cadastradas foram: {vendas}")