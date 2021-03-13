r = int(input('razao:'))
a = int(input('primeiro termo:'))
n = int(input('n primeiros termos:'))

k = list(range(1,n+1))

l = list()

for i in k:
    while i < n:
        b = a+n*r-r
        print(b)
        l.append(b)
        i = i + 1
            
print(l)
