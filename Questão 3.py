#Crie um programa que leia um número do usuário e exiba a sua raiz quadrada

from math import sqrt

def main():
    num = int (input ("Digite um número para calcular sua raiz quadrada: "))
    
    raiz = sqrt(num)
    
    print("\nA raiz quadrada de", num, "é: ", raiz)
    
if __name__ == "__main__":
    main()