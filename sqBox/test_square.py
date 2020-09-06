import unittest
import shapes

a = shapes.Square(5, 6)
b = shapes.Square(4, 7, 'blue')
print('Square a')
print(a)
print('Square b')
print(b)
print('Square a + b')
print(a+b)

class TestSquare(unittest.TestCase):
    
    def test_add(self):
        addSq = (a + b)
        self.assertEqual(addSq.area, 117)
        self.assertEqual(addSq.color, 'blackish blue' )

    def test_add_error(self):
        self.assertRaises(TypeError, a.__add__,  10)

if __name__ == '__main__':
    # allows test to be run this .py file in the cmd prompt
    unittest.main()