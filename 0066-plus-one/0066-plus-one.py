class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        array = digits 
        Numero = int("".join(map(str, array)))
        Numero += 1
        array = [int(digito) for digito in str(Numero)]
        return array



  