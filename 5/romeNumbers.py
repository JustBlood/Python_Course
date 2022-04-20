while True:
    alph = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
    decades = 'IXCM'
    excepted = ['IIII','VVVV','XXXX','LLLL','CCCC','DDDD','MMMM']
    def romeToArab(number=str):
        num = 0
        i = 0
        while i < len(number):
            if i+1<len(number):
                if (alph[number[i+1]] > alph[number[i]]) & (number[i] in decades) & ((alph[number[i+1]] == alph[number[i]]*5) | (alph[number[i+1]] == alph[number[i]]*10)):
                    num += alph[number[i+1]] - alph[number[i]]
                    i+=2
                    continue
            num += alph[number[i]]
            i+=1
        return num

    inputString = str(input())
    for i in excepted:
        if i in inputString:
            print('Неверный ввод числа.')
            exit()
    print(romeToArab(inputString))