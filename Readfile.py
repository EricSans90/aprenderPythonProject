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
            #print(linia[4])
            if linia[4]==(str(" ")):
                 print(linia[0:4])
                 count += 1
            elif linia[4] == (str("\n")):
                print(linia[0:4])
                count += 1
            # primera=linia.split(" ")[0]
            # if len(primera)==5:
            #     print(str(primera))
            #     count += 1
    print("Filas que empiezan por nano encontradas: "+str(count)+", la coooncha...")

def llevarbackslashn ():
    for linia in fhand:
        linia=linia.rstrip()
#perquè quan llevo la linia de dalt no funciona?
        if linia.startswith("nano"):
            if len(linia)==4:
                print(linia)

def rstripcontinue ():
    for linia in fhand:
        linia=linia.rstrip()
        if not linia.startswith("nano"):
            continue
        elif len(linia)==4:
            print(linia)

def obrirarxiuinput():
    final = False
    while final == False:
        fname = input("Dis-me el nom de l'arxiu (amb la seva extensió): ")
        try:
            fhand = open(fname)
            final = True
        except:
            print("No es pot obrir l'arxiu: ", fname)
            tornar = input ("Vols tornar a introduir el nom de l'arxiu? Si o no?: ")
            tornar=tornar.upper()
            if not tornar == ("SI"):
                quit()
            else:
                final == True

    for linia in fhand:
        linia=linia.rstrip()
        print (linia)