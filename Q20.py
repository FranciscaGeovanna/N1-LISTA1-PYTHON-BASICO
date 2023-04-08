print("Programa para ordenar números em ordem decrescente \n")

quant = int (input("Quantos números deseja ordenar? "))
lista = []

print("")

for i in range(quant):
    num = int (input("Digite o {}° número: ".format(i+1)))
    lista.append(num)

lista.sort(reverse = True)
print("\nNúmeros ordenados em ordem decrescente: \n", lista)