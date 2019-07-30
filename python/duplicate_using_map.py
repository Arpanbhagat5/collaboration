def duplicate(a):
    d = {}
    for i in a:
        if i in d.keys():
            d[i] += 1
        else:
            d.update({i:1})
    for k in d:
        if d[k] > 1:
            print(k) 
    print(d.keys())
    print(d.values())
duplicate([1,2,2,3,4,5,5,6,3,7,8])
        
