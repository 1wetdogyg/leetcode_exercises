class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        triangulo=[]
        for i in range (numRows):
            fila = [1] * (i+1)
            for j in range (1,i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            triangulo.append(fila)
        return triangulo



        