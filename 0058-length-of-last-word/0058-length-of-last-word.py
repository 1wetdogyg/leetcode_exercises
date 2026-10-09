class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        palabras = 0
        bandera = False 
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and bandera:
                return palabras
            else:
                if s[i] != " ":
                    palabras += 1
                    bandera = True
        return palabras

                 
                 

