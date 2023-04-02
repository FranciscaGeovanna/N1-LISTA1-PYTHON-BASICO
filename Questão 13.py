#Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a"

def main():
    plvs = [] #lista de palavras
    
    for i in range(0,5):
        plv = input("Digite uma palavra: ") 
        plvs.append(plv)
    
    print('\nAs palavras que começam com "a" são: ')
    for plv in plvs:
        if plv[0] == "a":
            print(plv)
    
if __name__ == "__main__":
    main()