from unittest import TestCase
#Import de la libreria datetime para conseguir la fecha del sistema
from datetime import date

tests_enabled = False # Variable para activar los test cases
dias31 = [1, 3, 5, 7, 8, 10, 12] # Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre meses con 31 días
dias30 =  [4, 6, 9, 11] # Abril, Junio, Septiembre y Noviembre meses con 30 días


# R0
def fecha_es_tupla(p_date: tuple) -> bool:
    '''Función que valida que una fecha sea un tupla de 3 números enteros positivos retorna un booleano.'''
    if(not isinstance(p_date, tuple)): # Se verifica si es una tupla
        return False
    
    if(len(p_date) != 3): # Se verifica si es una tupla de 3
        return False
    
    if((not isinstance(p_date[0], int)) or (not isinstance(p_date[1], int)) or (not isinstance(p_date[2], int))): # Se validan que sean 3 números enteros
        return False

    if(p_date[0] < 0 or p_date[1] < 0 or p_date[2] < 0): # Validar que el número no sea negativo
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
    if(p_date[1] in dias31): # Si es un mes con 31 días ver que los días no sea mayor a 31
        if(p_date[2] > 31):
            return False
            
    elif(p_date[1] in dias30): # Si es un mese con 30 días ver que los días no sea mayor a 30
        if(p_date[2] > 30):
            return False

    else: # Febrero con 28 o 29 días depende de si es bisiesto
        if(bisiesto(p_date[0])):
            if(p_date[2] > 29):
                return False
        elif (p_date[2] > 28):
            return False

    return True

# R3
def dia_siguiente(p_date: tuple) -> tuple:
    '''Función que dada una fecha válida determina el día siguiente.'''

    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(p_date)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(p_date)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')

    p_date_var = (p_date[0], p_date[1], p_date[2] + 1) # Se le agrega uno al día y se valida
    if(fecha_es_valida(p_date_var)):
        return p_date_var

    p_date_var = (p_date_var[0], p_date_var[1] + 1, 1) # Si sumandole uno al día es inválido entonces se pasa al siguiente mes
    if(fecha_es_valida(p_date_var)):
        return p_date_var

    return (p_date_var[0] + 1, 1, 1) # Si sumandole uno al mes es inválido entonces se pasa al siguiente año

# R4
def dias_desde_primero_enero(p_date: tuple) -> int:
    '''Función que determina la cantidad de días transcurridos desde el primero de enero del mismo año'''
    
    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(p_date)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(p_date)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')

    diasTranscurridos = 0
    hoy = (p_date[0],1,1)
    while(hoy != p_date):
        diasTranscurridos += 1

        hoy = dia_siguiente(hoy)
        
    return diasTranscurridos
    
    
#R5
def fecha_hoy() -> tuple:
    '''Función que retorna la fecha del día de hoy como una tupla de fecha válida'''
    m_date = date.today()
    return (m_date.year, m_date.month, m_date.day)

#R6
def edad_hoy(p_date: tuple) -> tuple:
    '''Función que determina la edad de una personas en años, meses y dias cumplidos.'''
    today = fecha_hoy()

    # Encontrar los años cumplidos
    years = today[0] - p_date[0]

    if(p_date[1] == today[1] and p_date[2] == today[2]):
        return (years, 0, 0)

    pastDay = True # Encontrar si la persona ya cumplió años en este año
    if(today[1] < p_date[1]):
        pastDay = False
    elif(today[1] == p_date[1]):
        if(today[2] < p_date[2]):
            pastDay = False

    months = 0
    days = 0 

    if(not pastDay):
        years -= 1
        months = (12 - p_date[1]) + today[1] # Encontrar los meses cumplidos
        
    else:
        months = (today[1] - p_date[1]) # Encontrar los meses cumplidos
        p_date = (today[0], p_date[1], p_date[2]) # Encuentro la cantidad de días cumplidos

    days = abs(today[2] - p_date[2])
    return (years, months, days)

''' Sección de pruebas para los requerimientos '''
if __name__ == "__main__" and tests_enabled:
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

    # R3
    assert dia_siguiente((2012, 12, 31)) == (2013, 1, 1)
    assert dia_siguiente((1992, 12, 1)) == (1992, 12, 2)
    assert dia_siguiente((1899, 11, 30)) == (1899, 12, 1)
    assert dia_siguiente((1792, 12, 31)) == (1793, 1, 1)
    assert dia_siguiente((1899, 1, 1)) == (1899, 1, 2)
    assert dia_siguiente((1899, 1, 31)) == (1899, 2, 1)
    testCase = TestCase()
    testCase.assertRaises(Exception, dia_siguiente, (1, 1, 1))
    testCase.assertRaises(Exception, dia_siguiente, (1440, 1, 1))
    testCase.assertRaises(Exception, dia_siguiente, (0, 0, 0, 0))
    testCase.assertRaises(Exception, dia_siguiente, 'hola')
    testCase.assertRaises(Exception, dia_siguiente, (1989, 14, 1))
    testCase.assertRaises(Exception, dia_siguiente, (1989, 12, 75))
    
    # R4
    assert dias_desde_primero_enero((2020,1,1)) == 0
    assert dias_desde_primero_enero((2020,1,13)) == 12
    assert dias_desde_primero_enero((2020,2,13)) == 43
    assert dias_desde_primero_enero((2019,2,13)) == 43
    assert dias_desde_primero_enero((2020,3,1)) == 60
    assert dias_desde_primero_enero((2020,4,1)) == 91
    assert dias_desde_primero_enero((2020,10,13)) == 286
    assert dias_desde_primero_enero((2020,11,13)) == 317
    assert dias_desde_primero_enero((2020,12,25)) == 359
    assert dias_desde_primero_enero((2019,12,31)) == 364
    assert dias_desde_primero_enero((2020,12,31)) == 365
    testCase.assertRaises(Exception, dias_desde_primero_enero, (1400, 12, 75))
    testCase.assertRaises(Exception, dias_desde_primero_enero, 'hola')

    # R5
    # Esta prueba requiere de cambiar de cambiar la fecha a mano 
    # Tener cuidado si se corren las pruebas pues probablemente tire errores
    assert fecha_hoy() == (2020, 5, 30)

    # R6
    # Esta prueba requiere de cambiar de cambiar la fecha a mano
    # Tener cuidado si se corren las pruebas pues probablemente tire errores
    assert edad_hoy((1998, 12, 13)) == (21, 5, 17)
    assert edad_hoy((1998, 9, 30)) == (21, 8, 0)
    assert edad_hoy((1995, 1, 3)) == (25, 4, 27)
    assert edad_hoy((1995, 5, 30)) == (25, 0, 0)