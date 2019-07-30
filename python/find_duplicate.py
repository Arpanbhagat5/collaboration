def find_duplicate(b):
    b.sort()
    a=[b[i] for i in range(0,len(b)-1) if b[i] == b[i+1]]
    # for i in range(0,len(b)-1):
    #     if b[i] == b[i+1]:
    #         print(b[i])
    #     else:
    #         continue
    print(a)
find_duplicate([1,4,2,6,3,4,6,5])
