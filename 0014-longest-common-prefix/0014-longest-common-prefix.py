class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefijo = strs[0]

        for palabra in strs[1:]:
            while not palabra.startswith(prefijo):
                prefijo = prefijo[:-1]

                if prefijo == "":
                    return ""

        return prefijo

        