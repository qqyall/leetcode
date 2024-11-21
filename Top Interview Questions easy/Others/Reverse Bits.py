class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # n&1 - битовое И
            # пример: 7&1 = 0111&0001 = 0001 = 1
            # 14&5 = 1110&0101 = 0100 = 4
            # Короче, делая побитовое И с 1 ты узнаешь, какой последний бит у числа 0 или 1
            # На основании этого свойства ниже реализовал метод, определяющий, является ли число четным, кстати
            res = (res<<1) + (n&1)
            n >>= 1
        return res
        
    def checkPrime(self, n):
        if n&1 == 0:
            return 'Prime'
        return 'NotPrime'


sol = Solution()
print(sol.reverseBits(int('00000010100101000001111010011100')))

print(sol.checkPrime(13))
