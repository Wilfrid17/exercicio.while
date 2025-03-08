vendas = [941, 852, 783,714,
          697, 686, 670, 630, 
          453, 386,371, 290, 
          269, 259, 218, 208, 
          163, 125, 102, 87, 
          47, 7]
vendedor = ["Maria","José",
            "Antonio","Joâo",
            "Francisco","Ana",
            "Luiz","Paulo",
            "Carlos","Manoel",
            "Pedro","Francesca",
            "Bruno","Brenda",
            "Masouco","Loui",
            "Denes","Jhanson",
            "Cris","Benes",
            "Mona","Napoleon"]
meta = 50

i = 0 
while vendas[i] > meta:
    print(f"{vendedor[i]} Bateu a meta. vendas: {vendas[i]}")
    i += 1
else:
    print("Nenhum Vendedor bateu a meta. ")