#Funciona pa números positius, pals reals tryexceptneg.py

ival = -1
while ival < 0:
    num = input ('Introduce un número positivo:')
    try:
        ival = int(num)
    except:
        ival = -1

    if ival > 0 :
        print('Perfecto, has introducido el número:', ival)
    else:
        print('No es un número escrito con sus cifras, inténtelo de nuevo')
