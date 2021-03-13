i = int(input('idade:')) #age
s = input('sexo:') #sex
d = int(input('salario:')) #income

h = 0
m = 0

salario30 = []

sh = []
sm = []

while i > 0:
    if i < 30:
        salario30.append(d)
    if s == "M":
        sh.append(d)
        h = h + 1
    else:
        sm.append(d)
        m = m + 1
    i = int(input('idade')) #idade
    s = input('sexo') #sexo 
    d = int(input('salario')) #salário
        
    print(sh)
    print(sm)

v = sum(sh)/h
print('Salário médio dos homens:', v) #average man income

x = sum(sm)/m
print('Salário médio das mulheres:', x) #average woman income

print(max(salario30)) #highest salary under 30




