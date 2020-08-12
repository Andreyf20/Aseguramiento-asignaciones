from asignacion3b import dia_semana
import unittest

class As3bModPU(unittest.TestCase):

    def test_dia_semana(self):

        self.assertRaises(Exception,dia_semana,32)

        self.assertRaises(Exception,dia_semana,(1,2,-3))

        self.assertRaises(Exception,dia_semana,(1700,10,10,12))

        self.assertRaises(Exception,dia_semana,(1581,12,31))

        self.assertEqual(dia_semana((2012, 12, 12)),3,"3 es la salida correcta")

        print("Pruebas unitarias en dia_Semana exitosas.")
    
# Para ejecutar prueba
# cd a Asignacion 7/
# => python -m pytest -v --cov=. --cov-report=html .\As3bModPU.py