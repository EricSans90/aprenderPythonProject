#Imprimir per consola tots els múltiples de 3 menors que 100
def multiples3menor100():
    Totalval=0
    while Totalval < 99:
        Totalval=Totalval+3
        print(Totalval)

#Imprimir per consola múltiples de 7 fins a sumar 100 (entre el que has imprimit)
def multiples7suma100():
    val=0
    totalval=0
    while totalval <= 100:
        val +=  7
        print(val)
        totalval += val

#Imprimir per consola els primers 15 números de la seqüència de Fibonazi

def fibonaziOP():
    a = 1
    b = 1
    c=1
    count=0
    while count <15:
        a=b
        b=c
        count=count+1
        c = a + b
        print(a)


#Imprimir per consola els primers 15 números de una seqüència de Fibonazi a la que podem passar per paràmetre dos
#valors inicials
def fibonaziParams(a,b):
    c = a + b
    count = 0
    while count < 15:
        a = b
        b = c
        count = count + 1
        c = a + b
        print(a)


