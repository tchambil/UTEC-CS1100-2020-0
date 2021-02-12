import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from Laboratorio2_2 import Solution
except Exception as e:
    raise Exception(
        f'No se pudo importar su clase Solution de "solution.py", por favor recordar trabajar a partir del template. El error es: {e}')


def descuento(x,y,a):
    if a == "A":
        return (int((x * y - (30 / 100) * (x * y))))
    elif a == "B":
        return (int((x * y - (20 / 100) * (x * y))))
    elif a == "C":
        return (int((x * y - (10 / 100) * (x * y))))
    elif a == "D":
        return (int((x * y - (5 / 100) * (x * y))))

def latex(text):
    result =''
    for i in text:
        if i == "4":
            i = "a"
        elif i == "1":
            i = "i"
        elif i == "3":
            i = "e"
        elif i == "0":
            i = "o"
        elif i == (","):
            i = " "
        elif i == " ":
            i = ""
        else:
            i
        result = result+ i
    return result

def redondearnota(notas):
    result = []
    for i in notas:
        if (i % 5 == 4 or i % 5 == 2 or i % 5 == 0) and i > 30:
            result.append(i + (5 - (i % 5)))
        else:
            result.append(i)
    return result

class TestSolution(unittest.TestCase):
    @weight(2)
    def test1(self):
        x = 10
        y = 2
        a = 'A'
        stb = Solution()
        solution_result = stb.Pregunta1(x,y,a)
        result = descuento(x,y,a)
        self.assertEqual(solution_result, result,f'Test 1 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(2)
    def test2(self):
        x = 5
        y = 3
        a = 'B'
        stb = Solution()
        solution_result = stb.Pregunta1(x,y,a)
        result = descuento(x,y,a)

        self.assertEqual(solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(2)
    @visibility('after_due_date')
    def test3(self):
        x = 15
        y = 4
        a = 'C'
        stb = Solution()
        solution_result = stb.Pregunta1(x,y,a)
        result = descuento(x,y,a)

        self.assertEqual(solution_result, result,
                         f'Test 3 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(3)
    def test4(self):
        text = "U n 1 v 3 r s 1 d 4 d, d 3, 1 n g 3 n 1 3 r 1 4, y, t 3 c n 0 l 0 g 1 4,"
        stb = Solution()
        solution_result = stb.Pregunta2(text)
        result = latex(text)

        self.assertEqual(solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(4)
    def test5(self):
        text = "I n ,   c 0 m p u t 3 r ,   s c 1 3 n c 3 ,   4 ,   g r 4 p h ,   1 s ,   4 n ,   4 b s t r 4 c t ,   d 4 t 4 ,   t y p 3 ,   t h 4 t ,   1 s ,   m 3 4 n t ,   t 0 ,   1 m p l 3 m 3 n t ,   t h 3 ,   u n d 1 r 3 c t 3 d ,   g r 4 p h ,   4 n d ,   d 1 r 3 c t 3 d ,   g r 4 p h ,   c 0 n c 3 p t s ,   f r 0 m ,   m 4 t h 3 m 4 t 1 c s ,   s p 3 c 1 f 1 c 4 l l y ,   t h 3 ,   f 1 3 l d ,   0 f ,   g r 4 p h ,   t h 3 0 r y.,"
        stb = Solution()
        solution_result = stb.Pregunta2(text)
        result = latex(text)
        self.assertEqual(solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
    @weight(2)
    def test6(self):
        notas = [68, 46, 54, 24, 37, 23, 48, 51]
        stb = Solution()
        solution_result = stb.Pregunta3(notas)
        result = redondearnota(notas)
        self.assertCountEqual (solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
    @weight(2)
    def test7(self):
        notas = [5,38,42,55,21,44]
        stb = Solution()
        solution_result = stb.Pregunta3(notas)
        result = redondearnota(notas)
        self.assertCountEqual (solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
    @weight(3)
    def test8(self):
        notas = [7,41,42,33,47,52,60,40]
        stb = Solution()
        solution_result = stb.Pregunta3(notas)
        result = redondearnota(notas)
        self.assertCountEqual (solution_result, result,
                         f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
if __name__ == '__main__':
    unittest.main()