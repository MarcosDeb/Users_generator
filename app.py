

# *****Get the first three characters of your first and last name*****

def GetCharacters(string):
    new_string=""
    count=0
    for caracter in string:
        if count<=2:
            new_string=new_string+caracter
        count=count+1
    return new_string

# *****Get the first three characters of your social number*****

def GetNumbers(numbers):
    new_string=""
    count=0
    for caracter in numbers:
        if count<3:
            count=count+1
            new_string=new_string+caracter
    return new_string

name=input("Ingrese su nombre: ")
lastname=input("ingrese su apellido: ")
social_number=input("ingrese su dni: ")

key_1=GetCharacters(name)
key_2=GetCharacters(lastname)
key_3=GetNumbers(social_number)

definite_key=key_1.lower()+key_2.lower()+key_3

print(definite_key)