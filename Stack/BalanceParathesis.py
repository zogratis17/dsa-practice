s = ')('

on , cn = 0 , 0 

for c in s:
    if c == '(':
        cn+=1
    elif c == ')':
        if cn > 0:
            cn -= 1
        else:
            on +=1

print(on+cn)