def merge(L,p,q,r):
    L1 = []
    L2 = []
    N1 = q-p+1
    N2 = r-q

    i = 0
    while i < N1:
        L1.append(L[p+i])
        i = i + 1
    
    i = 0
    while i < N2:
        L2.append(L[q+1+i])
        i = i + 1
    
    print(L)
    print(L1)
    print(L2)

    i = 0
    j = 0
    k = 0
    while True:
        if L1[i] <= L2[j]:
            L[p+k] = L1[i]
            i = i + 1
            k = k + 1
            if i == N1:
                while j < N2:
                    L[p+k] = L2[j]
                    j = j + 1
                    k = k + 1
                break
        else:
            L[p+k] = L2[j]
            j = j + 1
            k = k + 1
            if j == N2:
                while i < N1:
                    L[p+k] = L1[i]
                    i = i + 1
                    k = k + 1
                break
print("-------START---------")
L = [-2,4,3,10,20,30,40,15,17,25,35,45,50,55,60,-200,-100,345]
p = 3
q = 6
r = 14
merge(L,p,q,r)

print(L)
print("--------END---------")    
