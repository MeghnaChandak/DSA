def insert_at_sorting_position(L, N: int):
    key = L[N - 1]
    i = N - 2
    while i >= 0:
        if L[i] > key:
            L[i+1] = L[i]
        else:
            break
        i = i - 1
    L[i+1] = key

def insertion_sort(L):
    for i in range(2,len(L)):
        insert_at_sorting_position(L,i)

def display(L):
    for i in range(len(L)):
        print(i, L[i])

def main():
    L = [25]
    print("before : ", display(L))
    insertion_sort(L)
    print("after : ", display(L))

main()