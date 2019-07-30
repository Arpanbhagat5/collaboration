a=[0,3,3,3,0]
lta=[0]*5
rta=[0]*5
suml=0
sumr=0
print(a)
for i in range(len(a)):
    if i == 0:
        lta[i] = 0
    else:
        suml += a[i-1]
        lta[i]=suml
print(lta)
for j in range(len(a)-1,-1,-1):
    if j == len(a)-1:
        rta[j]=0
    else:
        sumr += a[j+1]
        rta[j]=sumr
print(rta)
for c in range(len(a)):
    if rta[c]==lta[c]:
        print("voila = ", c)
