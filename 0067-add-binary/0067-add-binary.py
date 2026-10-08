class Solution:
    def addBinary(self, a: str, b: str) -> str:
        suma_decimal = int(a, 2) + int(b, 2)
        
        return bin(suma_decimal)[2:]
        
        
            
             
        