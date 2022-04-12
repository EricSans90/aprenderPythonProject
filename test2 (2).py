listaNum = [1,2,3, 4,5,7,8, 0]
existsNegative = False
allPositive = True
numNegative = 0
numPositive = 0
for num in listaNum:
    if num<0:
        existsNegative = True
        allPositive = False
    if num == 0:
        continue
    if num<0:
        numNegative += 1
    else:
        numPositive += 1
print("Número negativos:", numNegative)
print("Número positivos:", numPositive)
print("Son todos positivos? " + str(allPositive))

if existsNegative:
    print("Hay algun negativo")
else:
    print("No hay ningún negativo")
