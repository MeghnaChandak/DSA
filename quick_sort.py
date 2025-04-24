def partition(p,r,L):
    i = p - 1
    j = p
    pivot = L[r]
    while j <= r:
        if L[j] <= pivot:
            i = i + 1
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
        j = j + 1
    return i

def quickSort(p,r,L):
    if p < r:
        q = partition(p,r,L)
        quickSort(p,q-1,L)
        quickSort(q+1,r,L)

def main():
    L = [5,90,2,390,1,39,9,399,91,23,12,50]
    print("Before Sort : ",L)
    quickSort(0,len(L)-1,L)
    print("After Sort : ",L)

    L = [90,5,2,390,1,39,9,399,91,23,12,50]
    print("Before Sort : ",L)
    quickSort(0,len(L)-1,L)
    print("After Sort : ",L)
    print("------END---------")

main()
        