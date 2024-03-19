f = open("26-59.txt")
n = f.readline()
s = {}
p = {}
rmax = 0
for l in f:
    r, m = map(int, l.split())
    if r in s:
        s[r].append(m)
    else:
        s[r] = [m]
for rr in s:
    mm = s[rr]
    for n in range(min(mm)+1, max(mm)-2):
        if (n not in mm) and (n+1 not in mm) and (n-1 in mm) and (n+2 in mm):
            rmax = max(rmax, rr)
            if rr in p:
                p[rr].append(n)
            else:
                p[rr] = [n]
            #print(rr, mm, n, n+1)
    #print(rr, mm)
print(rmax, min(p[rmax]))
#print(sorted(s[20164]))
