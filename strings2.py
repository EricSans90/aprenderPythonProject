def firstFunction():
    #Slicing Strings
    s='Monty Python'
    a= (s[:4])
    b= (s[4:7])
    c= (s[7:8])
    d= (s[8:])
    print (a+b+c+d)

def testsvarios():
    #Concatenació
    a='Hello'
    b='there'
    print (a+' '+b)

    #o a='Hello' b=a+' '+'there?' print (b)

    #using in as logical operator
    fruit='banana'
    x = 'm'
    if x in fruit:
        print('There is a '+ x +' in: ' + fruit)
    else:
        print("There isn't a "+ x + " in " + fruit)
    #Com conxasumare recupero la lletra que he posat al 'm' in fruit???
    # How the fuck poso la ' de isn't? --> \

#String comparison
def string_compare() :
    word = input ('Disme una paraula:')
    if word == 'banana':
        print('agárrame esta')
    elif word < 'banana':
        print('La teua paraula '+word+' està abans de banana.')
    elif word > 'banana':
        print('La teua paraula '+word+' està després de banana.')

def otrasFunciones():
    #String Library lower upper
    saluda='Qué passa Carabassa?'
    saluda_low=saluda.lower()
    #print(saluda_low)
    #print(saluda)
    saluda_up=saluda.upper()
    #print(saluda_up)
    #print(saluda)

    #Methodos (coses que li puc fer a strings)
    stuff = 'ola que ase hermano?'
    #print (type(stuff))
    #print(dir(stuff))

#Replace
def replace():
    #stuff = 'ola que ase hermano?'
    #print(stuff.replace('ase ', 'nasheeei '))
    stuff = 'ola que ase hermano? asease ase ase. ase,'

    #print(stuff.replace( r'ase+[ .,]', ' nasheeei ', 2))
    #print (re.sub(r'ase+[ .,]', ' nasheeei ', stuff))
#Problemes amb agafar els ase com a paraula y no dins de asease

#rfind
def rfind():
    raise Exception("Pues hoy no hacemos nada, estamos de huelga")
    stuff = 'ola que ase hermano?'
    buscador='ase'
    print(stuff.find(buscador))
    buscador2='monguer'
    if stuff.find(buscador2) == -1:
        raise  Exception("No hay ningún"+buscador2+"en la cadena")
    print(stuff.find(buscador2))

def rindex():
    stuff = 'ola que ase hermano?'
    buscador='ase'
    print(stuff.rindex(buscador))
    buscador2='monguer'
    try:
        print(str(stuff.rindex(buscador2)))
    except:
        print("Pues vaya")
    #se suposa que return ValueError --> com ho puc vore?


def rjust():
    stuff = 'ola que ase hermano?'
    print(stuff.rjust(50))
    print(stuff.rjust(50,'*'))


def strip():
    stuff = '       ola que ase hermano?         '
    print(stuff.rstrip())
    print(stuff.lstrip())
    print(stuff.strip())
    print(stuff.split())
    stuff2 = '++++++ola que ase hermano?+++++++++'
    print(stuff2.strip('+'))

def starts():
    line = 'Real life is p2W'
    if line.startswith('r'):
        print("Real and true")
    else:
        print("F")


#Parsing and extracting
def extract():
    # data = "From omgitsabe@omgitshim.es 13 04  2022"
    # atpos = data.find("@")
    # print (atpos)
    # sppos = data.find(" ",atpos)
    # print(sppos)
    # host=data [atpos+1:sppos]
    # print(host)
    # extract()
    data = "From omgitsabe@omgitshim.es 13 04 2022"
    dataWords = data.split(" ")
    for word in dataWords:
        print(word)
        if "@" in word:
            parts = word.split("@")
            for part in parts:
                print("Part: " + part)
                if "." in part:
                    print("result: "  + part.split(".")[0])
            break

    print("se acabó")

#si hi ha més d'un @...
