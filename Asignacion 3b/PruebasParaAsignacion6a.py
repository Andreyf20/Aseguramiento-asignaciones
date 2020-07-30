from unittest import TestCase

from asignacion3b import *

testCase = TestCase()


def PruebasR3_dia_siguiente():

    try:

        testCase.assertRaises(Exception, dia_siguiente, 32)

        testCase.assertRaises(Exception, dia_siguiente, (1, 2, -3))

        testCase.assertRaises(Exception, dia_siguiente, (1700, 10, 10, 12))

        testCase.assertRaises(Exception, dia_siguiente, (1581, 12, 31))

        assert dia_siguiente((2012, 12, 12)) == (2012, 12, 13)

        print("Pruebas para R3 (dia_siguiente) exitosa.")

    except AssertionError:

        print("Error al hacer pruebas para R3 (dia_siguiente)")


def PruebasR6_edad_hoy():

    try:

        testCase.assertRaises(Exception, edad_hoy, 1)

        testCase.assertRaises(Exception, edad_hoy, (1581, 12, 31))

        assert edad_hoy((1995, 1, 3)) == (25, 6, 26)

        assert edad_hoy((1998, 12, 13)) == (21, 7, 16)

        assert edad_hoy((1995, 5, 30)) == (25, 2, 1)

        print("Pruebas para R6 (edad_hoy) exitosa.")

    except AssertionError:

        print("Error al hacer pruebas para R6 (edad_hoy)")


def PruebasR7_dia_semana():

    try:

        testCase.assertRaises(Exception, dia_semana, 32)

        testCase.assertRaises(Exception, dia_semana, (1, 2, -3))

        testCase.assertRaises(Exception, dia_semana, (1700, 10, 10, 12))

        testCase.assertRaises(Exception, dia_semana, (1581, 12, 31))

        assert dia_semana((2012, 12, 12)) == 3

        print("Pruebas para R7 (dia_semana) exitosa.")

    except AssertionError:

        print("Error al hacer pruebas para R7 (dia_semana)")


def PruebasR8_imprimir_3x4():

    try:

        testCase.assertRaises(Exception, imprimir_3x4, 1582)

        imprimir_3x4(1583)

        print("Pruebas para R8 (imprimir_3x4) exitosa.")

    except AssertionError:

        print("Errores al hacer pruebas para R8 (imprimir_3x4)")


def PruebasR10_dias_entre():

    try:

        testCase.assertRaises(Exception, dias_entre, 1, 2,)

        testCase.assertRaises(Exception, dias_entre,
                              (-1500, 13, 13), (12, 12, 12))

        assert dias_entre((1600, 11, 11), (1600, 11, 11)) == 0

        assert dias_entre((1600, 11, 11), (1600, 11, 16)) == 5

        assert dias_entre((1600, 11, 16), (1600, 11, 11)) == 5

        print("Pruebas para R10 (dias_entre) exitosa.")

    except AssertionError:

        print("Error al hacer pruebas para R1 (dias_entre)")


PruebasR3_dia_siguiente()
PruebasR6_edad_hoy()
PruebasR7_dia_semana()
PruebasR8_imprimir_3x4()
PruebasR10_dias_entre()
