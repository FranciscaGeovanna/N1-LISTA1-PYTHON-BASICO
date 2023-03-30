#Crie um programa que leia uma palavra do usuário e exiba a primeira letra dessa palavra.

def main():
    palavra = str (input ("Digite uma palavra: "))
    
    letra = palavra[0]
    
    print("\nA primeira letra da sua palavra é: ", letra)
    
if __name__ == "__main__":
    main()