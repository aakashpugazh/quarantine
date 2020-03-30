
f = ['f','l','a','m','e','s']
a = [i for i in str(input("name1:"))]
b = [i for i in str(input("name2:"))]
name1 = list(a)
name2 = list(b)
for i in name1:
        if i in name2:
            name2.remove(i)
for i in b:
    if i in name1:
        name1.remove(i)
com = name1 + name2
t  = len(com)
n = t-1
def dup(l,a):
    global f
    for i in range(n):
        l.remove(a)
    m = []
    [m.append(x) for x in l if x not in m]
    r = f[f.index(a)+1::]
    l =f[:f.index(a):]
    f = r+l
    return f
def dup(l,a):
    global f
    for i in range(n+1):
        l.remove(a)
    m = []
    [m.append(x) for x in l if x not in m]
    r = f[f.index(a)+1::]
    l =f[:f.index(a):]
    f = r+l
    return f
def res(d,n):
    q = []
    for i in range(n+1):
        q += d
    return q
if a != b :
    while len(f)>1:
        if n != 0:
            while n<len(f)-1:
                    f.pop(n)
                    r = f[n::]
                    l = f[:n]
                    f = r+l
            else:
                    v = res(f,n)
                    s = v[n]
                    f = dup(v,s)
        else :
            f.pop(n)
    w = "Relationship status :", f[0]
    print(w)


else:
    print("plaes enter diff names")
