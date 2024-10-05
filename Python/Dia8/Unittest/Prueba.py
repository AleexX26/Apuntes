import unittest
import CambiarTexto

class ProbarCambiaTexto(unittest.TestCase):
    def test_cambiar_texto(self):
        palabra = "buen dia"
        resultado = CambiarTexto.todoMayusculas(palabra)
        self.assertEqual(resultado, "BUEN Dia")

if __name__ == "__main__":
    unittest.main()
