print ("Programa para exibir o menor número de uma lista\n")

lista = []

for i in range(0,5):
    num = int (input("Digite um número: "))
    lista.append(num)
    
maior = lista[0]

for j in range(len(lista)):
    if lista[j] < maior:
        maior = lista[j]

print("\nO menor número desta lista é: ", maior)