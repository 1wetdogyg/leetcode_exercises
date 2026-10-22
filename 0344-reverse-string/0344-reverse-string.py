class Solution:
    def reverseString(self, s: list[str]) -> None: 
        copia = s[:]
        bandera = 0
        for i in range(len(copia)-1, -1, -1):
            s[bandera] = copia[i]
            bandera += 1  
            
        