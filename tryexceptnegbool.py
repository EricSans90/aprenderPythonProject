#Funciona pa números positius, falta pensar negatius també

ival = False
while not ival:
    num = input ('Introduce un número real:')
    try:
        val = int(num)
        ival = True
    except:
        print('No es un número escrito con sus cifras, inténtelo de nuevo')
        continue
    print('Perfecto, has introducido el número:', val)

val *= 1000
print("He calculado que te puedes comer " + str(val)  + " mierdas")
