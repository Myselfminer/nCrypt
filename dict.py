import random
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"\
   ,"t","u","v","w","x","y","z"]
def create():
    dictionary=open("dictionary.py","w")
    tablewenn=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"\
   ,"t","u","v","w","x","y","z"," "]
    tablewennupper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"\
   ,"T","U","V","W","X","Y","Z"]
    tabledann=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"\
   ,"t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"\
   ,"T","U","V","W","X","Y","Z"," "]
    dictionary.write("def ver(letter):\n")
    entkeys=[]
    for i in tablewenn:
        returning=random.choice(tabledann)
        tabledann.remove(returning)
        dictionary.write("   if letter == '"+i+"' :\n      return '"+returning+"'\n")
        entkeys.append([returning,i])
    for i in tablewennupper:
        returning=random.choice(tabledann)
        tabledann.remove(returning)
        dictionary.write("   if letter == '"+i+"' :\n      return '"+returning+"'\n")
        entkeys.append([returning,i])
    dictionary.write("   else:\n      return letter\n")
    dictionary.write("def ent(letter):\n")
    for i in entkeys:
        dictionary.write("   if letter == '"+i[0]+"':\n      return '"+i[1]+"'\n")
    dictionary.write("   else:\n      return letter")
def debug():
    pass
