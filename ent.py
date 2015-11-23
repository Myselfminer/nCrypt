import dictionary
def do(Path,Password):
    final=open(Path.strip(".crypt"),"w")
    original=open(Path,"r")
    originallist=original.readlines()
    for i in originallist:
        for u in i:
            d=str(dictionary.ent(str(u)))
            final.write(d)
        final.write("\n")
