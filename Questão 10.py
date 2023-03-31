def main():
    print("Programa para exibir a média \n")
    
    nums = []
    
    for i in range(0,5):
        num = float (input("Digite um número: "))
        nums.append(num)
        
    soma = sum(nums)
    quant = len(nums)
    
    media = soma / quant

    print ("\nA média é: ", media)
    
if __name__ == "__main__":
    main()