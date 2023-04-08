print("Programa para ordenar números em ordem crescente \n")

quant = int (input("Quantos números deseja ordenar? "))
lista = []

print("")

for i in range(quant):
    num = int (input("Digite o {}° número: ".format(i+1)))
    lista.append(num)

lista.sort()
print("\nNúmeros ordenados em ordem crescente: \n", lista)