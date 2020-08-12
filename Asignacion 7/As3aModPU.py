from asignacion3b import edad_hoy,dia_siguiente
import unittest

class As3aModPU(unittest.TestCase):

    def test_edad_hoy(self):

        self.assertRaises(Exception,edad_hoy,1)

        self.assertRaises(Exception,edad_hoy,(1581,12,31))

        self.assertEqual(edad_hoy((1995, 8, 11)),(25, 0, 1),"(25, 0, 1) es la salida correcta")

        self.assertEqual(edad_hoy((1995,9,28)),(24, 11, 16),"(24, 11, 16) es la salida correcta")

        self.assertEqual(edad_hoy((1995, 8, 12)),(25,0,0),"(25,0,0) es la salida correcta")

        print("Pruebas unitarias en edad_hoy exitosas.")

    def test_dia_siguiente(self):

        self.assertRaises(Exception,dia_siguiente,'32')

        self.assertRaises(Exception,dia_siguiente,(1, 2, -3))

        self.assertRaises(Exception,dia_siguiente,(1700,10,10,12))

        self.assertRaises(Exception,dia_siguiente,(1581, 12, 31))

        self.assertEqual(dia_siguiente((2012, 12, 12)),(2012,12,13),"(2012,12,13) es la salida correcta")

        self.assertEqual(dia_siguiente((2012, 12, 31)),(2013,1,1),"(2013,1,1) es la salida correcta")

        self.assertEqual(dia_siguiente((2012, 11, 30)),(2012,12,1),"(2012,12,1) es la salida correcta")


        print("Pruebas unitarias en dia_siguiente exitosas.")


# Para ejecutar prueba
# cd a Asignacion 7/
# => python -m pytest -v --cov=. --cov-report=html .\As3bModPU.py
