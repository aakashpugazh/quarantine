from tkinter import *
from tkinter import font as tkFont
fld = Tk()
x = StringVar()
y = StringVar()
rel = StringVar()
f = ['FRIEND','LOVE','AFFECTIONATE','MARRIAGE','ENEMY','SISTER']
z = f
helv36 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
def clear ():
    global f
    x.set("")
    y.set("")
    rel.set("")
    f = []
    for i in z :
        f.append(i)

def press():
    global f
    global r
    a = [i for i in  x.get().lower()]
    b = [i for i in  y.get().lower()]
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
    if a != b:
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
        rel.set(w)
    else:
        rel.set("PLEASE ENTER DIFFERENT NAMES")

aname =  Entry(fld,textvariable = x,width=35,font = helv36).grid(row = 0)
bname =  Entry(fld,textvariable = y,width=35,font = helv36).grid(row = 1)
result = Entry(fld,textvariable = rel,width=35,font = helv36).grid(row = 3)
Button(fld,text = 'ENTER',bg = 'blue',fg = 'white',width = 5,command = lambda:press(),font = helv36).grid(row = 2,column = 0)
Button(fld,text = 'reset names',bg = 'blue',fg = 'white',width = 8,command = lambda:clear(),font = helv36).grid(row = 4,column = 0)
fld.geometry("325x300")
mainloop()
