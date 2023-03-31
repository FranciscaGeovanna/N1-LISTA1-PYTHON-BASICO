def main():
    numeros = []
    
    print("Programa para mostrar a soma dos números digitados\n\n")
    
    for i in range(0, 5):
        numero = float (input("Digite um número: "))
        numeros = numeros + [numero]
        
    soma = sum(numeros)
    
    print("\nSoma dos números digitados: ", soma)
    
if __name__ == "__main__":
    main()