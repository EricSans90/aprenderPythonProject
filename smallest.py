#Funció trobar el més petit
def find_smallest() :
    smallest = None
    for value in [9,41,12,3,74,15]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print ('this value was', value, 'and the smallest so far is',smallest)

    print('The smallest number of them all is', smallest)


find_smallest ()

#Preguntar:
    #Com recuperar les posicions dels 3 en la cadena
        #Si soles 1 volta var count, si hi ha més d'una?
