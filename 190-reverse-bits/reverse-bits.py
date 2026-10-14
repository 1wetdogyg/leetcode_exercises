class Solution:
    def reverseBits(self, n: int) -> int:
        respuesta = []
        binario= (f"{n:032b}")[::-1]
        return int(binario, 2)

     


        