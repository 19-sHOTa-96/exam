### EXERCISE-3
from time import sleep
from random import randint

def bomber_man(n=0, r=0):
    arr = []
    ind = []

    for i in range(r):  
        r = randint(0, 5)
        a = '. '*n
        x = []
        b = a.split(' ')
        b[r] = '0'
        c = ' '.join(b).strip()
        arr.append(b)
        index = b.index('0')
        ind.append(index)

        print(c)

    sleep(2)    
    print("\n")    

    for i in arr:
        for j in range(len(i)):
            i[j] = '0'   

        print(" ".join(i))    

    sleep(2)     
    print("\n")    

    for i, j in zip(ind, arr):
        j[i] = '.'
        print(" ".join(j))


bomber_man(n=5, r=5)