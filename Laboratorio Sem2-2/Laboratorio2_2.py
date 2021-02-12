class Solution:
    def Pregunta1(self, x,y,a):
        if a == "A":
            return (int((x * y - (30 / 100) * (x * y))))
        elif a == "B":
            return (int((x * y - (20 / 100) * (x * y))))
        elif a == "C":
            return (int((x * y - (10 / 100) * (x * y))))
        elif a == "D":
            return (int((x * y - (5 / 100) * (x * y))))

    def Pregunta2(self, text):
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

    def Pregunta3(self,notas):
        result = []
        for i in notas:
            if (i % 5 == 4 or i % 5 == 2 or i % 5 == 0) and i > 30:
                result.append(i + (5 - (i % 5)))
            else:
                result.append(i)
        return result

x = 10
y = 2
a = 'A'
text = "U n 1 v 3 r s 1 d 4 d, d 3, 1 n g 3 n 1 3 r 1 4, y, t 3 c n 0 l 0 g 1 4,"
notas = [68,46,54,24,37,23,48,51,45]
print(Solution().Pregunta1(x,y,a))
print(Solution().Pregunta2(text))
print(Solution().Pregunta3(notas))
'''
68
46 
55
24
40
23
48
51
50
'''
