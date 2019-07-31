def nish(l):
    n="abcdefghijklmnopqrstuvwxyz"
    for g in n:
        if g not in l.lower():
            return False
    return True
lo=input()
if (nish(lo)==True):
    print("yes")
else:
    print("no")
