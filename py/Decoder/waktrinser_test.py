import unittest
from waktrinser import Waktrinser

class WaktrinserTest(unittest.TestCase):
    def test_decode_string(self):
        waktrinser = Waktrinser()
        self.assertEqual(waktrinser.decode_string('[#1] Maîtrise Zone', [0, 0.8], 50), '40 Maîtrise Zone')
        self.assertEqual(waktrinser.decode_string('[#1] Point{[>1]?s:} de Vie', [0, 2, 2, 2], 110), '220 Points de Vie')
        self.assertEqual(waktrinser.decode_string('{[~3]?[#1] Maîtrise [#3]:[#1] Maîtrise sur [#2] élément{[>2]?s:} aléatoire{[>2]?s:}}', [160, 0, 3, 0], 200), '160 Maîtrise sur 3 éléments aléatoires')
        self.assertEqual(waktrinser.decode_string('Renvoie |[#7.3]*100|% des dégâts', [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0.001], 100), 'Renvoie 10% des dégâts')

    def test_decode_effect(self):
        waktrinser = waktrinser()
        self.assertEqual(waktrinser.decode_effect({'description': {'fr': '[#1] Maîtrise Zone'}, 'params': [0, 0.8]}, 50), '40 Maîtrise Zone')

if __name__ == '__main__':
    unittest.main()
