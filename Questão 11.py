#Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.

def main():
    
    nums = []
    
    for i in range(0,5):
        num = int (input("Digite um número: "))
        nums.append(num)
       
    print ("\nOs números pares são: ")
    
    for num in nums:
        if num %2 == 0:
            print(num)
        
if __name__ == "__main__":
    main()