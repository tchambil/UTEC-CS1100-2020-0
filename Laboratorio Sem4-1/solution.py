class Solution:
    def Pregunta1(self,data):
        pass

    def CalcularNota(self, n):
        pass
 
    def Pregunta2(self, data2):
        pass

data1 =[[8 ,5],[[2, 1, 1, 1, 1 ,1 ,1, 1],
               [2, 1, 0, 0, 0, 0, 0, 1],
               [2, 1, 0, 0, 0, 0, 0, 1],
               [2, 1, 0, 0, 0, 0, 0, 1],
               [2, 1, 1, 1, 1, 1, 1, 1]],
       [1, 2, 1]]

data2 = [[3, 9],
        [68, 32, 36],
        [46, 29, 42],
        [54, 30, 67],
        [24, 50, 19],
        [37, 27, 30],
        [23, 27, 57],
        [48, 35, 53],
        [51, 31, 45],
        [45, 67, 49]] 
for i in Solution().Pregunta1(data1):
    print (i)
for i in Solution().Pregunta2(data2)[1:]:
    print (i)