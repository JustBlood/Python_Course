while True:
    # Define alph, decades and excepted combinations
    alph = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
    decades = 'IXCM'
    excepted = ['IIII','VVVV','XXXX','LLLL','CCCC','DDDD','MMMM']
    # Main func
    def romeToArab(number=str):
        # num - returning number in Arab
        num = 0
        i = 0
        while i < len(number):
            if i+1<len(number):
                # Processing case with rule of substraction
                if (alph[number[i+1]] > alph[number[i]]) & (number[i] in decades) & ((alph[number[i+1]] == alph[number[i]]*5) | (alph[number[i+1]] == alph[number[i]]*10)):
                    num += alph[number[i+1]] - alph[number[i]]
                    # Shifting i
                    i+=2
                    continue
            # If case is default, not substraction, just folding
            num += alph[number[i]]
            i+=1
        return num

    inputString = str(input())
    # Checking to correct input...
    for i in excepted:
        if i in inputString:
            print('Неверный ввод числа.')
            exit()
    print(romeToArab(inputString))