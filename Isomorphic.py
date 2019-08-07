c,d = map(str,input().split())
x = {}; y = {}
def is_isomorphic(c, d):
    if len(c) != len(d):
        return False
    else:
        for i, v in enumerate(c):
            if v in x and x[v] != d[i]:
                return False
            else:
                x[v] = d[i]
            if d[i] in y and y[d[i]] != v:
                return False
            else:
                y[d[i]] = v
        return True
z=is_isomorphic(c,d)
if (True==z):
  print("yes")
else:
  print("no")
