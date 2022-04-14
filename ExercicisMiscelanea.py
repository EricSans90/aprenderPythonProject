#Agafar un DNI de un input i validar la lletra

#Utilitzant la possició a una cadena
def validateDNI(dni):
    if len(dni) == 9:
        #print(str(dni) + str(len(dni)))
        #print(dni[:8])
        #print(dni[8])
        try:
            dninum=int(dni[:8])
            #print(dninum)
            #print(type(dninum))
            dnilet = dni[8]
            dnilet = dnilet.upper()
            #print((dninum % 23))
            #print(restoalletra(dninum % 23))
            #print(dnilet)
            if restoalletra(dninum % 23) == dnilet:
                print("El DNI: " + str(dni) + " SÍ es válido")
            else:
                print("El DNI: " + str(dni) + " NO es válido")

        except:
            print("No has introducido un DNI válido, los 8 primeros caracteres deben ser números.")

    else:
        print("No has introducido un DNI válido, éste debe tener 9 caracteres: 8 números y una letra y tu has "
                "introducido: "+str(len(dni))+" caracteres.")

def restoalletra (resto):
    if resto == 0:
        letvalid="T"
    elif resto == 1:
        letvalid="R"
    elif resto == 2:
        letvalid="W"
    elif resto == 3:
        letvalid = "A"
    elif resto == 4:
        letvalid = "G"
    elif resto == 5:
        letvalid = "M"
    elif resto == 6:
        letvalid = "Y"
    elif resto == 7:
        letvalid = "F"
    elif resto == 8:
        letvalid = "P"
    elif resto == 9:
        letvalid = "D"
    elif resto == 10:
        letvalid = "X"
    elif resto == 11:
        letvalid = "B"
    elif resto == 12:
        letvalid = "N"
    elif resto == 13:
        letvalid = "J"
    elif resto == 14:
        letvalid = "Z"
    elif resto == 15:
        letvalid = "S"
    elif resto == 16:
        letvalid = "Q"
    elif resto == 17:
        letvalid = "V"
    elif resto == 18:
        letvalid = "H"
    elif resto == 19:
        letvalid = "L"
    elif resto == 20:
        letvalid = "C"
    elif resto == 21:
        letvalid = "K"
    elif resto == 22:
        letvalid = "E"
    return letvalid
    #print(str(letvalid))
