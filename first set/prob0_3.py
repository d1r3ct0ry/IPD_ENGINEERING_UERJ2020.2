x = 1

z = [] #entrada
p = [] #pares
j = [] #impares

while x != 0:
    x = int(input('número: ',))
    z.append(x)

for i in z:
    if i % 2 == 0:
        p.append(i)
    else:
        j.append(i)

print(len(p),'pares')
print(len(j),'impares')

print(sum(p)/len(p))
