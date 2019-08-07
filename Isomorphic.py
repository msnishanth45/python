a,b = map(str,input().split())
c = {}; d = {}
def is_isomorphic(a, b):
    if len(a) != len(b):
        return False
    else:
        for i, v in enumerate(a):
            if v in c and c[v] != b[i]:
                return False
            else:
                c[v] = b[i]
            if b[i] in d and d[b[i]] != v:
                return False
            else:
                d[b[i]] = v
        return True
z=is_isomorphic(a,b)
if (True==z):
  print("yes")
else:
  print("no")
