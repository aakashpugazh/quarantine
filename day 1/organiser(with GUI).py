from tkinter import *
import os
from tkinter import font as tkFont
from pathlib import Path as p
btn = Tk()
a = ""
b = []
but = []
butt ={}
helv36 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
for m in os.scandir():
    if m.is_dir():
        z = str(p(m))
        if not z.startswith("."):
            b.append(os.path.basename(m))
            butt.update({os.path.basename(m):os.path.abspath(m)})
dir = StringVar()

val = len(b)
l =[]


def foldering():
    import os
    import shutil
    from pathlib import Path
    cr = os.getcwd()



    dirs={"apps":[".apk",".deb"],"archives":[".zip",".7z",".xz",".gz"],"images":[".jpeg",".jpg",".png"],"docs":[".pdf",".txt",".html"],"videos":[".mp4",".avi",".mkv"],"music":[".mp3"]}
    ffms={f:d
          for d,ff in dirs.items()
           for f in ff}
    def arr():
        for i in os.scandir():
            if i.is_dir():
                continue
            fp = Path(i.name)
            f = fp.suffix.lower()
            if f in ffms:
                try :
                    s = os.path.abspath(i)
                    d = cr+"/"+ffms[f]+"/"+os.path.basename(i)
                    shutil.move(s,d)
                except:
                    cda = os.getcwd()
                    os.chdir(cr)
                    os.mkdir(ffms[f])
                    os.chdir(cda)
                    s = os.path.abspath(i)
                    d = cr+"/"+ffms[f]+"/"+os.path.basename(i)
                    shutil.move(s,d)
            else:
                cdb = os.getcwd()
                os.chdir(cr)
                os.mkdir("others")
                os.chdir(cdb)
                s = os.path.abspath(i)
                d = cr+"/"+"others"+"/"+os.path.basename(i)
                shutil.move(s,d)
    def org():
        for i in os.scandir():
                a=os.getcwd()
                if i.is_dir():
                    try:
                        os.chdir(os.path.abspath(i))
                        arr()
                        b=os.getcwd()
                        org()
                        os.chdir(a)
                        a=b
                    except:
                        pass
                else :
                    arr()
    org()
    dir.set("organised")












def com ():
    dir.set(os.getcwd())

dir.set(os.getcwd())
for i in range(0,9):
    for j in range(0,9):
        h = [i,j]
        l.append(h)
for k in range(val):
    v = Button(btn,text = str(b[k]) ,height = 1, width = 15,bg = "blue",justify = LEFT,fg = "white",bd = 4,font = helv36,command=lambda c=k:[os.chdir(butt[but[c].cget("text")]),com()])
    but.append(v)
    but[k].grid(row = l[k][0],column = l[k][1],padx = 5,pady = 5)

directory = Entry(btn,textvariable = dir,width = 30).grid(row = i)
Button (btn ,text = "organise",height = 3,width = 8,bg = "#f5425a",fg = "#030504",font = helv36,command = lambda :foldering()).grid(row = i,column = j)




mainloop()
