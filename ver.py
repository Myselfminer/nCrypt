import dictionary
def do(Path,Password):
    final=open(Path+".crypt","w")
    original=open(Path,"r")
    originallist=original.readlines()
    for i in originallist:
        for u in i:
            d=str(dictionary.ver(str(u)))
            final.write(d)
            print(u)
        final.write("\n")
        print(i)
    print("Fertig.")
