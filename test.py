name = input('Who are you? ')
print('Welcome', name)
age = input ('How old are you? ')
type (age)
iage = int(age)
thisyear = input ('Did you already have your birthday this year? ')
print("Has dicho: " + thisyear)
iage += 1
isThisTheRealWorld = thisyear.upper() == 'YES'
if isThisTheRealWorld :
    print ('Next year you will have', iage ,'years old')
else :
    print ('When you reach your bithday this year you will have', iage ,
    'years old')
print(thisyear)
thisyear = thisyear.upper()
print(thisyear)
