
a=[]
b=[]

g = 'red123ford'
d = {}
z =''
l=[]
for x in g:
    if x.isdigit():

        a.append(x)
        b.append(g.index(x))

        # print(x , g.index(x))
        # d[g.index(x)] = x
    else:
        l.append(x)



# for x in g:
#     if not x.isdigit():
#         l.append(x)
# print(d)
print(a)
print(b)
print(l)
l.reverse()

for c in range(0,len(a)):
    l.insert(b[c],a[c])



# for x in d:
#     print(x,d[x] )
#     # print(type(x),type(y))
#     l.insert(x,d[x])

print(l)

v = ''.join(l)
print(v)