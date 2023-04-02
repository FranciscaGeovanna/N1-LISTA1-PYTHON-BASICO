def main():
    
    print("Programa para somar números pares\n")
   
    nums = [] #lista de números
    
    for i in range(0,5):
        num = int (input("Digite o {}° número: ".format(i+1)))
        nums.append(num)
    
    nump = [] #lista de números pares
    
    print("\nNúmeros pares: ")
    for num in nums:
        if num %2 == 0:
            print(num)
            nump.append(num)

    print("\nSoma dos números pares: ")
    soma = sum(nump) #soma dos números pares
    print(soma)
    
if __name__ == "__main__":
    main()