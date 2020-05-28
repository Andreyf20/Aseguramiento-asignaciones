
# R0
def fecha_es_tupla(p_date: tuple) -> bool:
    '''Función que valida que una fecha sea un tupla de 3 números enteros positivos retorna un booleano.'''
    if(not isinstance(p_date, tuple)): # Se verifica si es una tupla
        return False
    
    if(len(p_date) != 3): # Se verifica si es una tupla de 3
        return False
    
    if((not isinstance(p_date[0], int)) or (not isinstance(p_date[1], int)) or (not isinstance(p_date[2], int))): # Se validan que sean 3 números enteros
        return False

    if(p_date[0] < 0 or p_date[1] < 0 or p_date[2] < 0):
        return False

    return True

# R1
def bisiesto(p_year: int) -> bool:
    '''Función que valida si un año es bisiesto dentro del calendario gregoriano.'''
    if(p_year < 1582): # Validar que sea un año del calendario gregoriano
        return False

    if((p_year % 4) != 0): # Si el año es divisible entre 4 es bisiesto
        return False

    if((p_year % 100) == 0 and (p_year % 400) != 0): # Si el año es divisible entre 100 no es bisisesto a menos que también sea divisibles entre 400
        return False

    return True

''' Sección de pruebas para los requerimientos '''
# R0: fecha_es_tupla
assert fecha_es_tupla(32) == False
assert fecha_es_tupla('hola') == False
assert fecha_es_tupla((-1, -1, -1)) == False
assert fecha_es_tupla((1, 2, 3, 4)) == False
assert fecha_es_tupla((1, 2, -3)) == False
assert fecha_es_tupla((1, 2, 3)) == True

# R1: bisiesto
assert bisiesto(1800) == False
assert bisiesto(1900) == False
assert bisiesto(2100) == False
assert bisiesto(2300) == False
assert bisiesto(2500) == False
assert bisiesto(2020) == True
assert bisiesto(2000) == True
assert bisiesto(2400) == True
assert bisiesto(2308) == True
assert bisiesto(1924) == True