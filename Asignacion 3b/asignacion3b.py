from unittest import TestCase
#Import de la libreria datetime para conseguir la fecha del sistema
from datetime import date

tests_enabled = True # Variable para activar los test cases
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

#R7
def dia_semana(p_date: tuple) -> int:
    '''Función que determina el día de la semana que le corresponde: 0 domingo, 1 lunes, 2 martes, 3 miércoles, 4 jueves, 5 viernes, 6 sábado.'''
    # Se utiliza la regla de Zeller: F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C

    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(p_date)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(p_date)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')
    
    v_year = p_date[0]
    k = p_date[2] # El día del mes

    # El número del mes
    m = p_date[1] - 2 if p_date[1] > 2 else (11 if p_date[1] == 1 else (12 if p_date[1] == 2 else -1))
    if(m == -1):
        raise Exception('ERROR FATAL: No se logró obtener la llave del mes')
    
    if(p_date[1] == 1 or p_date[1] == 2):
        v_year -= 1

    D = v_year % 100 # Los últimos dos dígitos del mes
    C = v_year // 100 # Los primeros dos dígitos del mes
    
    F = k + ((13 * m - 1) // 5) + D + ( D // 4 ) + ( C // 4 ) - 2 * C

    return F % 7


#R8
#Función que imprime calendario gregoriano en formato 3 columnas x 4 filas
calendar = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre'] #lista con los meses del año

week = ['D','L', 'K', 'M', 'J', 'V', 'S'] #lista con las iniciales de la semana

def imprimir_3x4(year):
    if year < 1583:
        raise Exception('El año ingresado no es válido: El año no es parte del calendario gregoriano')
    else:
        
        start_pos = dia_semana((year,1,1))#encontrar día en que se inicia año solicitado, se usa función de R7
        leap = False
        if bisiesto(year):
            leap = True
        cont=0
        nextMonth = 0
        while(cont<12):
            #Nombre del mes
            print('| ',end = ' ')
            print(calendar[cont].center(20, ' '),end = '')        
            if cont==3 or cont==7 or cont==11: #comenzar una fila de meses cada 4 columnas
                print()
                i=0
                while(i<4):
                    print('| ',end = '')
                    print(''.join(['{0:<3}'.format(w) for w in week]),end='') #imprimir iniciales de la semana 4 veces
                    i=i+1
                print('\n| ',end='')            
                day1, day2, day3, day4 = 0,0,0,0 
                week1 = True #para utilizar la función en el R7
                day = 1
                loop = 0
                month=1 + nextMonth
                start_pos = dia_semana((year,month,1))
                print('{0:<3}'.format('')*start_pos, end='')
                while(day<=40):
                    if day>=29:
                        if leap == True and month == 2 and day == 29:
                            print('{0:<3}'.format(29), end='') #formato de impresión dejando 3 espacios entre números y letras
                        elif month in dias30 and day <= 30:
                            print('{0:<3}'.format(day), end='')
                        elif month in dias31 and day <= 31:
                            print('{0:<3}'.format(day), end='')
                        else:
                            print('{0:<3}'.format(''), end='')
                        start_pos+=1
                        day = day +1                        
                    else:
                        print('{0:<3}'.format(day), end='')                
                        start_pos+=1
                        day = day +1
                    if start_pos == 7:
                        loop += 1
                        if loop == 1:
                            day1=day
                        if loop == 2:
                            day2=day
                        if loop == 3:
                            day3=day
                        if loop == 4:
                            day4=day
                        print('|',end=' ')
                        month = month + 1
                        if week1:
                            if(month<13):
                                day = 1
                                start_pos = dia_semana((year,month,1))
                                print('{0:<3}'.format('')*start_pos, end='')
                        if loop == 4:
                            print()
                            print('|',end=' ')
                            start_pos = 0
                            day=day1
                            day1=0
                            week1=False
                            loop=0
                            month=month - 4
                        if week1 == False and loop == 1:
                            start_pos = 0
                            day=day2
                        if week1 == False and loop == 2:
                            start_pos = 0
                            day=day3
                        if week1 == False and loop == 3:
                            start_pos = 0
                            day=day4
                print()
                print()
                nextMonth = nextMonth + 4
            cont=cont+1

#R9
def fecha_futura(p_date: tuple, days: int) -> tuple:
    '''Función que dada una fecha y una cantidad de días devuelve la fecha después de esa cantidad de días.'''
    
    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(p_date)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(p_date)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')

    if(days < 0 or not isinstance(days, int)):
        raise Exception('El valor de días ingresado debe ser no negativo entero')

    while days > 0:
        p_date = dia_siguiente(p_date)
        days -= 1
    
    return p_date

def fecha_despues(fecha1: tuple, fecha2: tuple)->bool:
    '''Indica si la fecha en el primer parametro es despues que el segundo'''

    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(fecha1) or not fecha_es_tupla(fecha2)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(fecha1) or not fecha_es_valida(fecha2)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')

    #Fechas iguales
    if(fecha1 == fecha2):
        return False

    #Comparamos años primero
    if(fecha1[0] > fecha2[0]): #Año de fecha1 es mayor
        return True
    if(fecha1[0] < fecha2[0]): #Año de fecha1 es menor
        return False
    
    #comparamos meses
    if(fecha1[1] > fecha2[1]): #Mes de fecha1 es mayor
        return True
    if(fecha1[1] < fecha2[1]): #Mes de fecha1 es menor
        return False

    #comparamos dias
    if(fecha1[2] > fecha2[2]): #Mes de fecha1 es mayor
        return True
    if(fecha1[2] < fecha2[2]): #Mes de fecha1 es menor
        return False


#R10
def dias_entre (fecha1: tuple, fecha2: tuple) -> int:
    '''Funcion que determina el número de días naturales entre las dos fechas.'''
    '''Validaciones de la fecha'''
    if(not fecha_es_tupla(fecha1) or not fecha_es_tupla(fecha2)):
        raise Exception('La fecha ingresada no es válida: El formato es incorrecto o se tienen número no positivo, no enteros')

    if(not fecha_es_valida(fecha1) or not fecha_es_valida(fecha2)):
        raise Exception('La fecha ingresada no es válida: La fecha no es parte del calendario gregoriano')
    
    '''Misma fecha'''
    if(fecha1 == fecha2):
        return 0

    diasTranscurridos = 0

    if(fecha_despues(fecha1,fecha2)): #fecha1 viene despues

        while(fecha2 != fecha1):

            diasTranscurridos += 1

            fecha2 = dia_siguiente(fecha2)

        return diasTranscurridos
    
    while(fecha1 != fecha2): #fecha2 viene despues

        diasTranscurridos += 1

        fecha1 = dia_siguiente(fecha1)

    return diasTranscurridos



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
    # assert fecha_hoy() == (2020, 5, 30)

    # R6
    # Esta prueba requiere de cambiar de cambiar la fecha a mano
    # Tener cuidado si se corren las pruebas pues probablemente tire errores
    # assert edad_hoy((1998, 12, 13)) == (21, 5, 17)
    # assert edad_hoy((1998, 9, 30)) == (21, 8, 0)
    # assert edad_hoy((1995, 1, 3)) == (25, 4, 27)
    # assert edad_hoy((1995, 5, 30)) == (25, 0, 0)

    # R7
    assert dia_semana((2020, 1, 1)) == 3
    assert dia_semana((1999, 2, 1)) == 1
    assert dia_semana((1764, 4, 1)) == 0
    assert dia_semana((1983, 4, 1)) == 5
    assert dia_semana((2002, 5, 25)) == 6
    assert dia_semana((2006, 7, 4)) == 2
    assert dia_semana((2007, 12, 13)) == 4

    # R9
    testCase.assertRaises(Exception, fecha_futura, (1400, 12, 75), 0)
    testCase.assertRaises(Exception, fecha_futura, (1400, 12, 75, 0), 1)
    testCase.assertRaises(Exception, fecha_futura, (1900, 1, 15), -10)
    assert fecha_futura((1689, 1, 1), 15) == (1689, 1, 16)
    assert fecha_futura((2020, 2, 28), 1) == (2020, 2, 29)
    assert fecha_futura((2002, 10, 1), 3) == (2002, 10, 4)
    assert fecha_futura((1616, 12, 12), 20) == (1617, 1, 1)
    assert fecha_futura((1616, 12, 12), 0) == (1616, 12, 12)

    #Fecha mayor o menor
    testCase.assertRaises(Exception, fecha_despues, (1400, 12, "hola"),(1400, 12, 75))
    testCase.assertRaises(Exception, fecha_despues, (1400, 13, 24),(1400, 12, 75))
    testCase.assertRaises(Exception, fecha_despues, (1400, 13, 24),22)
    assert fecha_despues((2020, 4, 20), (2020, 4, 20)) == False
    assert fecha_despues((2019, 4, 20), (2020, 4, 20)) == False
    assert fecha_despues((2020, 4, 20), (2019, 4, 20)) == True
    assert fecha_despues((2020, 4, 20), (2020, 3, 20)) == True
    assert fecha_despues((2020, 5, 20), (2020, 7, 20)) == False
    assert fecha_despues((2020, 4, 19), (2020, 4, 20)) == False
    assert fecha_despues((2020, 4, 29), (2020, 4, 15)) == True
    
    #R10
    testCase.assertRaises(Exception, dias_entre, (1400, 12, "hola"),(1400, 12, 75))
    testCase.assertRaises(Exception, dias_entre, (1400, 13, 24),(1400, 12, 75))
    testCase.assertRaises(Exception, dias_entre, (1400, 13, 24),22)
    assert dias_entre((2020, 4, 20),(2020, 4, 20)) == 0
    assert dias_entre((2019, 4, 20),(2020, 4, 20)) == 366
    assert dias_entre((2020, 4, 20),(2019, 4, 20)) == 366
    assert dias_entre((2020, 4, 20),(2020, 5, 20)) == 30
    assert dias_entre((2020, 5, 20),(2020, 4, 20)) == 30
    assert dias_entre((2020, 1, 31),(2020, 2, 1)) == 1
    assert dias_entre((2020, 2, 28),(2020, 3, 1)) == 2
    assert dias_entre((2020, 9, 30),(2020, 9, 15)) == 15
    assert dias_entre((2020, 9, 15),(2020, 9, 30)) == 15
