#Funció trobar el més gran
def find_biggest() :
    biggest = None
    for value in [9,41,12,3,74,15]:
        if biggest is None:
            biggest = value
        elif value > biggest:
            biggest = value
        print ('this value was', value, 'and the biggest so far is', biggest)

    print('The biggest number of them all is', biggest)


find_biggest ()

#Preguntar:
    #Com recuperar les posicions dels 3 en la cadena
        #Si soles 1 volta var count, si hi ha més d'una?
