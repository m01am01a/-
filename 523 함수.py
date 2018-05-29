def cal_apple(a, b, c):
    apple=0
    i=1
    while i<=b:
        if i%c==0:
           apple=apple+i
        i=i+1
    return apple

def cal_peer(d,e):
    peer=0
    i=d
    while i<=end:
        peer=peer+i
        i=i+1
    return peer
        

start=int(input("시작 값: "))
end=int(input("끝 값: "))
baesu=int(input("배수 값으로 지정할 정수: "))
applepie=cal_apple(start, end, baesu)
print(applepie)
print(cal_peer(start, end))

