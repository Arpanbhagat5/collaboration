
mystr=raw_input("Get string: ")
cnt=[0]*26
odd=0
for c in mystr:
    cnt[ord(c)-ord('a')]+=1
l=[odd+1 for i in cnt if i%2!=0]
if (len(l) <=1 ):
    print("yes")