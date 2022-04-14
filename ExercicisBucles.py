from Models import FibonacciModel as fm
#Imprimir per consola tots els múltiples de 3 menors que 100
def multiples3menor100():
    # Totalval=0
    # while Totalval < 99:
    #     Totalval=Totalval+3
    #     print(Totalval)
    print(20474501 % 23)
    i = 0
    while i < 100:
        i+=1
        print("Número: " + str(i) + " Modulo = " + str(i%3))
        if i % 3 ==0 :
            print(i)

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
#valors inicials utilitzant el model FibonacciModel
def fibonaziParams(a,b):
    # fibo1 = fm.FibonacciModel(1,1)
    # fibo2 = fm.FibonacciModel(2, 3)
    # fibo3 = fm.FibonacciModel(10, 20)
    #
    # print("fibo1" + fibo1.printNextValue())
    # print("fibo2" + fibo2.printNextValue())
    # print("fibo3" + fibo3.printNextValue())
    # print("")
    # fibo2.calculateNextValue()
    # print("fibo1" + fibo1.printNextValue())
    # print("fibo2" + fibo2.printNextValue())
    # print("fibo3" + fibo3.printNextValue())
    # print("")
    # fibo3.calculateNextValue()
    # fibo3.calculateNextValue()
    # fibo1.calculateNextValue()
    # print("fibo1" + fibo1.printNextValue())
    # print("fibo2" + fibo2.printNextValue())
    # print("fibo3" + fibo3.printNextValue())
    fibo = fm.FibonacciModel(a, b)
    count = 0
    print("lol")
    while count < 15:
        print(fibo.printNextValue())
        fibo.calculateNextValue()
        count = count + 1


