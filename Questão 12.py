print("Programa para exibir números ímpares\n")

nums = [] #lista de números
    
for i in range(0, 5):
    num = int (input("Digite um número: ")) #recebe os números da lista
    nums.append(num)
    
print ("\nOs números ímpares são: ")
    
for num in nums:
    if num %2 != 0:
        print(num, end = "  ")