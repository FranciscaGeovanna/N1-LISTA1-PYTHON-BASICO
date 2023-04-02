def main():
    nums = []
    
    for i in range(0,5):
        num = float (input("Digite o {}° número: ".format(i+1)))
        nums.append(num)
    
    print("\nDos números digitados os maiores que 5 são: ")
    for num in nums:
        if num < 5:
            print(num)
            
if __name__ == "__main__":
    main()