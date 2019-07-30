def xor(a,b):
    current_ans = 0
    for i in range(a,b+1):
        current_ans = i^current_ans
    print(current_ans)
xor(5,8)
