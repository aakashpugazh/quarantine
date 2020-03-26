

def foldering():
    import os
    import shutil
    from pathlib import Path
    b = str(input("enter the directory path  : "))
    os.chdir(b)
    cr = os.getcwd()
    print(cr)



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


foldering()
