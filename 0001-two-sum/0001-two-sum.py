class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diccionario = {} 
        for n, numero in enumerate(nums):
            valor = target - nums[n] 
            if valor in diccionario:
                return  [diccionario[valor], n]
            diccionario[numero] = n 
