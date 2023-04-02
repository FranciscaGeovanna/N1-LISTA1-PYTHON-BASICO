def main():
    nums = [] 
    
    print("Programa para somar números ímpares\n")
    
    for i in range(0,5):
        num = int (input("Digite o {}° número: ".format(i+1)))
        nums.append(num)
    
    numi = [] 
    
    print("\nNúmeros ímpares: ")
    for num in nums:
        if num %2 != 0:
            print(num)
            numi.append(num)

    print("\nSoma dos números ímpares: ")
    soma = sum(numi)
    print(soma)
    
if __name__ == "__main__":
    main()
