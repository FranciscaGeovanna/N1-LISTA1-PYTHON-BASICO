print("Programa para exibir o produto de uma lista de números \n")

lista = []

for i in range(0, 5):
    num = int (input("Digite o {}° número: ".format(i+1)))
    lista.append(num)
    
prod = 1
    
for num in lista:
    prod *= num

print("\nO produto desta lista é: ", prod)