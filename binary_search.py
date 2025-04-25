def binSearch(si, ei, L, SE): 
    if si <= ei: 
        mi = (si+ei)//2 
        if L[mi] == SE: 
            return True 
        elif SE < L[mi]: 
            return binSearch(si, mi-1, L, SE)
        else: 
            return binSearch(mi+1, ei, L, SE)
    return False 

L = [10, 20, 30, 40, 50, 60, 70] 

for x in L: 
    ret_val = binSearch(0, len(L)-1, L, x)
    if ret_val == True: 
        print(x, "is present in", L)
    else: 
        print(x, "is not present in", L)

M = [15, 25, 35, 45, 55, 65, 75]
for x in M: 
    ret_val = binSearch(0, len(L)-1, L, x)
    if ret_val == True: 
        print(x, "is present in", L)
    else: 
        print(x, "is not present in", L)

while True: 
    ans = int(input("Do you want to search one more time?[1:YES, 0:No]:"))
    if ans != 1: 
        break 
    SE = int(input('Enter integer value to be searched:'))
    ret_val = binSearch(0, len(L)-1, L, SE)
    if ret_val == True: 
        print(SE, "is present in", L)
    else: 
        print(SE, "is not present in", L)

print("Terminating binSearch Program")