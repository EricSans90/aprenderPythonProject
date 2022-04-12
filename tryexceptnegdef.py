#Funciona pa números reals
def intronum() :
    ival = 'false'
    while ival == 'false':
        num = input ('Introduce un número real:')
        try:
            ival = int(num)
        except:
            ival = 'false'

        if ival != 'false' :
            print('Perfecto, has introducido el número:', ival)
        else:
            print('No es un número escrito con sus cifras, inténtelo de nuevo')

intronum()
