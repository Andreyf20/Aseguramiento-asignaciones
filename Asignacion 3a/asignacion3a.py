
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

''' Seccion de pruebas para los requerimientos '''
# R0: fecha_es_tupla
assert fecha_es_tupla(32) == False
assert fecha_es_tupla('hola') == False
assert fecha_es_tupla((-1, -1, -1)) == False
assert fecha_es_tupla((1, 2, 3, 4)) == False
assert fecha_es_tupla((1, 2, -3)) == False
assert fecha_es_tupla((1, 2, 3)) == True