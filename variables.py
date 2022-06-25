from unicodedata import name


print("Type your age: "),
# myAge = input()
myAge = 37
print('I am {} years old.'.format(myAge))

############

Num1 = 2
Num2 = 3
print('O resultado de ', Num1, '+', Num2, 'é ', Num1 + Num2)

############

name = 'Alcenir'
print(type(name))

middlename = 'Nascimento de'

lastname = 'Alcantara'
print(type(lastname))

print(name + ' ' + lastname)

print(name + ' ' + middlename + ' ' + lastname)

############

name5 = name * 5
print(name5)

############

print(len(name))
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[-1])
print(name[-2])
print(name[0:3])
print(name[-7:-4])
print(name[-4:-6])
print(name[-5:])
