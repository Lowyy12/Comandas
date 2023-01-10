def carta_cocina(ncomanda, mesa, platos):
    comanda = []
    comanda.append(f"El número de la comanda -> {ncomanda}")
    comanda.append(f"Numero de mesa -> {mesa}")
    while platos != "0":
        comanda.append(platos)
        platos = str(input("Que plato quiere? "))
    return comanda


comandas = int(input("Número de la comanda: "))
premesa = int(input("Numero de la mesa: "))
nomplatos = str(input("Que plato quiere? "))

total = (carta_cocina(comandas, premesa, nomplatos))
print("\n")
print(total[0])
print(" ")
print(total[1])
print(" ")
platos_total = total[2:]
print(f"Platos -> {','.join(platos_total)}\n")
