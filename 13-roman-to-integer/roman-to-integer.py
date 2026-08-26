class Solution:
    def romanToInt(self, s: str) -> int:
        diccionario = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        resultado = 0
        for i in range(len(s) - 1):
            actual = s[i] 
            siguiente = s[i+1]
            if diccionario[actual] < diccionario[siguiente]:
                resultado -= diccionario[actual]
            else:
                resultado += diccionario[actual]
        resultado += diccionario[s[-1]]
        return resultado        




        