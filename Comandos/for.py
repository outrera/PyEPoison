from math import sqrt as root
suc=20
mer=0
i=0
while i<suc:
    i=i+1
    mer=1/(2+mer)

salida=1+mer
print("el resultado aproximado es "+salida)
print("El resultado exacto es "+str(root(2)))
