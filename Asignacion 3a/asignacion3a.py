
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
    if(p_year < 1582): # Confirmar que sea un año del calendario gregoriano válido
        return False

    if((p_year % 4) != 0): # Si el año es divisible entre 4 es bisiesto
        return False

    if((p_year % 100) == 0 and (p_year % 400) != 0): # Si el año es divisible entre 100 no es bisisesto a menos que también sea divisibles entre 400
        return False

    return True

# R2
def fecha_es_valida(p_date: tuple) -> bool:
    '''Función que valida una fecha dentro del calendario gregoriano.'''
    if(not fecha_es_tupla(p_date)): # Revisar si se ingreso el formato correcto para la fecha y si son enteros positivos
        return False

    if(p_date[0] < 1582): # Confirmar que sea un año válido del calendario gregoriano
        return False

    if((p_date[1] < 1 or p_date[1] > 12) or p_date[2] < 1): # Validar si es uno de los 12 meses permitidos, y si el día es mayor a cero
        return False

    ''' Validación de los días de un mes '''
    if(p_date[1] in [1, 3, 5, 7, 8, 10, 12]): # Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre meses con 31 días
        if(p_date[2] > 31):
            return False
            
    elif(p_date[1] in [4, 6, 9, 11] and p_date): # Abril, Junio, Septiembre y Noviembre meses con 30 días
        if(p_date[2] > 30):
            return False

    else: # Febrero con 28 o 29 días depende de si es bisiesto
        if(bisiesto(p_date[0])):
            if(p_date[2] > 29):
                return False
        elif (p_date[2] > 28):
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

# R2: fecha_es_valida
assert fecha_es_valida((1700, 10, 10, 12)) == False
assert fecha_es_valida((1500, 10, 10)) == False
assert fecha_es_valida((2500, 2, 29)) == False
assert fecha_es_valida((2300, 0, 12)) == False
assert fecha_es_valida((2300, 5, 0)) == False
assert fecha_es_valida((1900, 14, 12)) == False
assert fecha_es_valida((1900, 11, 31)) == False
assert fecha_es_valida((1900, 1, 32)) == False
assert fecha_es_valida((1924, 2, 29)) == True
assert fecha_es_valida((2020, 5, 28)) == True
assert fecha_es_valida((2500, 2, 28)) == True
assert fecha_es_valida((1998, 12, 13)) == True
assert fecha_es_valida((2012, 12, 12)) == True