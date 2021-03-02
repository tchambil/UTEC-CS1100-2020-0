import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution import Solution
except Exception as e:
    raise Exception(
        f'No se pudo importar su clase Solution de "solution.py", por favor recordar trabajar a partir del template. El error es: {e}')


def Pregunta1(data):
    tam = [int(temp) for temp in data[0]]
    w, h = tam
    paint = []
    for x in range(h):
        fi = [int(temp) for temp in data[1][x]]
        paint.append(fi)
    pro = [int(temp) for temp in data[2]]
    r, s, cc = pro
    for fi in range(h):
        for col in range(w):
            if paint[fi][col] == 0:
                paint[fi][col] = cc

    return paint


def CalcularNotas(n):
    x = (5 - (n % 5))
    if (n >= 28 and x % 2 != 0):
        return n + x
    return n


def Pregunta2(data):
    for i in range(1, data[0][1] + 1):
        for j in range(data[0][0]):
            data[i][j] = CalcularNotas(data[i][j])
    return data

class TestSolution(unittest.TestCase):
    @weight(2)
    def test1(self):
        data1 = [[8, 5], [[2, 1, 1, 1, 1, 1, 1, 1],
                          [2, 1, 0, 0, 0, 0, 0, 1],
                          [2, 1, 0, 0, 0, 0, 0, 1],
                          [2, 1, 0, 0, 0, 0, 0, 1],
                          [2, 1, 1, 1, 1, 1, 1, 1]],
                 [1, 2, 1]]
        stb =Solution()
        solution_result = stb.Pregunta1(data1)
        result = Pregunta1(data1)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(4)
    def test2(self):
        data1 = [[8,5],
                [[2,2,2,1,1,1,3,3],
                [2,2,1,1,0,1,1,3],
                [2,1,1,0,0,0,1,1],
                [2,1,0,0,0,0,0,1],
                [2,1,1,1,1,1,1,1]],
                [1,4,1]]
        stb =Solution()
        solution_result = stb.Pregunta1(data1)
        result = Pregunta1(data1)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

    @weight(4)
    @visibility('after_due_date')
    def test3(self):
        data1 = [[10, 7],
                [[2,2,1,1,1,1,3,3,1,1],
                [2,0,0,0,0,1,1,3,1,1],
                [2,1,0,0,0,0,1,1,2,2],
                [2,1,0,0,0,0,1,1,2,2],
                [2,1,1,1,0,0,1,1,2,2],
                [3,3,3,3,3,3,3,3,3,2],
                [3,3,3,3,3,3,3,3,3,2]],
                 [1, 1, 5]]
        stb =Solution()
        solution_result = stb.Pregunta1(data1)
        result = Pregunta1(data1)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')


    @weight(4)
    def test4(self):
        data=[[4, 10],
                [55, 49, 41, 48],
                [63, 53, 30, 67],
                [40, 26, 53, 33],
                [28, 62, 34, 27],
                [34, 32, 49, 60],
                [51, 47, 58, 50],
                [28, 42, 68, 48],
                [22, 68, 70, 49],
                [20, 54, 60, 62],
                [69, 65, 58, 48]]
        stb = Solution()
        solution_result = stb.Pregunta2(data)
        result = Pregunta2(data)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
    @weight(2)
    def test5(self):
        data2 = [[2, 5],
                 [60,42],
                 [55,20],
                 [53,27],
                 [31,51],
                 [33,66]]
        stb = Solution()
        solution_result = stb.Pregunta2(data2)
        result = Pregunta2(data2)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')
    @weight(4)
    def test6(self):
        data2 = [[4,20],
                [31,30,50,33],
                [64,41,57,39],
                [41,50,49,32],
                [58,64,34,44],
                [70,37,39,43],
                [62,67,53,60],
                [53,19,27,24],
                [54,25,38,48],
                [22,33,55,25],
                [41,54,69,43],
                [69,62,26,45],
                [60,51,55,45],
                [38,50,45,70],
                [55,25,56,54],
                [70,27,24,54],
                [53,55,27,25],
                [39,26,60,26],
                [32,46,49,23],
                [60,69,32,48],
                [36,19,64,47]]
        stb = Solution()
        solution_result = stb.Pregunta2(data2)
        result = Pregunta2(data2)
        self.assertCountEqual(solution_result, result,
                              f'Test 2 fallido. Resultado esperado: {result}. Resultado obtenido: {solution_result}.')

if __name__ == '__main__':
    unittest.main()