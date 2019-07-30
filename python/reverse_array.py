def reverse_array(a):
    l=len(a)
    count = l/2 if l%2 == 0 else (l-1)/2
    print("hello")
    print((int)(count))
    for i in range((int)(count)):
        tmp = a[l-i-1]
        a[l-i-1] = a[i]
        a[i] = tmp
    print(a)

reverse_array([1,2,3,4,5,6,7,8,9])