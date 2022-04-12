#Funció mirar dins d'una string
def look_string() :
    fruit = 'banana'
    letter = fruit[1]
    print(letter)

#Funció mida string
def len_string():
    fruit = 'banana'
    x=len(fruit)
    print(x)

#Loop spell string while
def loop_string():
    fruit = 'banana'
    index=0
    while index < len(fruit):
        letter = fruit[index]
        print(index, letter)
        index = index+1

#Loop spell string for
def loop_for_string():
    fruit='banana'
    for letter in fruit:
        print(letter)


#Loop counting string
def loop_count_string():
    word='banana'
    count=0
    for letter in word:
        if letter == 'a' :
            count = count+1
    print ('there are',count, '"a" in the word', word)
loop_count_string()
