#Funció contar
def count_string() :
    count = 0
    for numval in [9,41,12,3,74,15]:
        count = count + 1
        print(numval, 'is the number ', count)
    print('There are',count,'numbers')

count_string ()
