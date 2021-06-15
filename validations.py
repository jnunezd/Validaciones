from enum import Flag
import re
import os
from itertools import cycle


# * Si el email es valido retorna un array con [True, email], si no retorna False
def validar_mail(email):
    regex_mail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(regex_mail, email)):
        print("Email valido")
        email_extraido = re.search(regex_mail, email).group()
        return [True, email_extraido]
    else:
        print("Email invalido")
        return False


# * Si el rol es valido retorna un array con [True, rol], si no retorna False
def validar_rol(rol):

    regex_rol = re.compile("[a-zA-Z]-\d+-\d{4}") 

    # * [a-zA-Z] hace match a un solo caracter entre a y z o A y Z seguido de un guion
    # * \d hace match a un numero y con el mas a 1 o mas numeros seguidos de un guion
    # * \d{4} hace match a exactamente 4 numeros
    if(re.search(regex_rol, rol)):
        rol_extraido = regex_rol.search(rol).group()
        print("Rol valido")
        rol_extraido = re.search(regex_rol, rol).group()
        return [True, rol_extraido]
    else:
        print("Rol no valido")
        return False
    

# * Calcula el digito verificador y lo compara con el dado retorna True o False segun corresponda
def validar_rut(rut):
    rut = rut.replace(".","")
    rut_split = rut.split('-')
    reversed_digits = map(int, reversed(str(rut_split[0])))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = (-s) % 11

    if str(dv) == rut_split[1]:
        print("El rut es valido")
        return True
    else:
        print("El rut es invalido")
        return False