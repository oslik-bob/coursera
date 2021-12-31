"""
    est_wrong_types_raise_exception - проверяет, что передаваемый в функцию 
    аргумент типа float или str вызывает исключение TypeError. 
    Тестовый набор входных данных:  'string',  1.5

    test_negative - проверяет, что передача в функцию factorize отрицательного
    числа вызывает исключение ValueError. 
    Тестовый набор входных данных:   -1,  -10,  -100

    test_zero_and_one_cases - проверяет, что при передаче в функцию целых 
    чисел 0 и 1, возвращаются соответственно кортежи (0,) и (1,). 
    Набор тестовых данных: 0 → (0, ),  1 → (1, )

    test_simple_numbers - что для простых чисел возвращается кортеж, 
    содержащий одно данное число. 
    Набор тестовых данных: 3 → (3, ),  13 → (13, ),   29 → (29, )

    test_two_simple_multipliers — проверяет случаи, когда передаются числа 
    для которых функция factorize возвращает кортеж с числом элементов 
    равным 2. 
    Набор тестовых данных: 6 → (2, 3),   26 → (2, 13),   121 --> (11, 11)

    test_many_multipliers - проверяет случаи, когда передаются числа для 
    которых функция factorize возвращает кортеж с числом элементов больше 2. 
    Набор тестовых данных: 1001 → (7, 11, 13) ,   9699690 → (2, 3, 5, 7, 11, 13, 17, 19)

   ВАЖНО!  Все входные данные должны быть такими, как указано в условии. 
   Название переменной в каждом тестовом случае должно быть именно "x". 
   При этом несколько различных проверок в рамках одного теста должны быть 
   обработаны как подслучаи с указанием x: subTest(x=...). 
   В задании необходимо реализовать ТОЛЬКО класс TestFactorize, 
   кроме этого реализовывать ничего не нужно. Импортировать unittest и 
   вызывать unittest.main() в решении также не нужно.
"""
import unittest
    

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for i in ('string', 1.5):
            with self.subTest(x=i):
                self.assertRaises(TypeError, factorize, i)
        
    def test_negative(self):
        for i in (-1, -10, -100):
            with self.subTest(x=i):
                self.assertRaises(ValueError, factorize, i)
        
    def test_zero_and_one_cases(self):
        for i in (0, 1):   
            with self.subTest(x=i):
                self.assertEqual(factorize(i), (i, ))
        
    def test_simple_numbers(self):
        for i in (3, 13, 29):
            with self.subTest(x=i):
                self.assertEqual(factorize(i), (i, ))
                        
    def test_two_simple_multipliers(self):
        for i, t in ((6, (2, 3)), (26, (2, 13)), (121, (11, 11))):
            with self.subTest(x=i):
                self.assertEqual(factorize(i), t)
    
    def test_many_multipliers(self):
        for i, t in ((1001, (7, 11, 13)), 
                     (9699690, (2, 3, 5, 7, 11, 13, 17, 19))):
            with self.subTest(x=i):
                self.assertEqual(factorize(i), t)
    
