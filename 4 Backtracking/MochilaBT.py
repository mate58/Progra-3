def MochilaRec(w,p,e,pa,s):
    if pa > p:
        return
    if e == len(w):
        print(s)
        return

    s[e] = 1
    MochilaRec(w, p, e+1, pa + w[e], s)

    s[e] = 0
    MochilaRec(w, p, e+1, pa, s)

def MochilaBT(w,p):
    s = [0] * len(w)
    MochilaRec(2,p,0,0,s)


