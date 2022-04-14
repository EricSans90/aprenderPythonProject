fhand = open("whatever.txt")
#
# stuff="ola que\nase?"
# print(stuff)
# stuff2="A\nB"
# print(stuff2)
# print(len(stuff2))

def imprimirtext():
    for paraula in fhand:
    #paraula aquí es una línea sencera
        print(paraula)

def contalinies():
    fhand = open("C:/Users/User/PycharmProjects/aprenderPythonProject/whatever.txt")
    count = 0
    for paraula in fhand:
        count += 1
    print("Hi ha: " + str(count) + " línies en aquest text")

def lligirtot ():
    lligir=open("whatever.txt")
    toteltext=lligir.read()
    print (len(toteltext))
    print (toteltext [:20])
    #print(toteltext.split())

def buscarstartswith():
    count=0
    lligir=open("whatever.txt")
    for linia in lligir:
        if linia.startswith("nano"):
            print(linia[4])
            if linia[4]==(str(" ")):
                 print(linia[0:4])
                 count += 1
            # primera=linia.split(" ")[0]
            # if len(primera)==5:
            #     print(str(primera))
            #     count += 1
#NO me surt en el codi de dalt i no sé per què

    print("Filas que empiezan por nano encontradas: "+str(count)+", la coooncha...")