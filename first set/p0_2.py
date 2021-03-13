r = int(input('razão:'))
n = int(input('quantidade:'))
a = int(input('primeiro termo:'))

z = range(1,n+1)

valores = []

for i in z:
    t = a+(i-1)*r
    valores.append(t)
    i = i + 1

print(valores)
