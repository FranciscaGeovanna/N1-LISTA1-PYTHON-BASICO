def main():
    palavras = []
    
    print("Programa para mostrar qual palavra digitada é mais longa\n\n")
    
    for i in range(0, 5):
        palavra = (input("Digite uma palavra: "))
        palavras += [palavra]
        
    palavraLonga = ""
    for palavra in palavras:
        if len(palavra) > len(palavraLonga):
            palavraLonga = palavra
    
    print ("\nA palavra mais longa entre as digitadas é: ", palavraLonga)
    
if __name__ == "__main__":
    main()