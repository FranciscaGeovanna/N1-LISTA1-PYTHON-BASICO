#Crie um programa que leia um número do usuário e determine se esse
#número é par ou ímpar 

num = int (input("Digite um número para saber se ele é par ou ímpar: "))

if num %2 == 0: 
    print ("\nO número", num, "é par")
else:
    print ("\nO número", num, "é ímpar")