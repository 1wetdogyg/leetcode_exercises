class Solution:
    def isValid(self, s: str) -> bool:
        pila = []

        parejas = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for caracter in s:

            if caracter in parejas:
                if not pila or pila[-1] != parejas[caracter]:
                    return False

                pila.pop()

            else:
                pila.append(caracter)

        return len(pila) == 0


        