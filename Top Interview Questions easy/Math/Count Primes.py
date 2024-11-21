class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        a = [_ for _ in range(n+1)]
        a[1] = 0
        lst = []
        i = 2
        while i < n:
            if a[i] != 0:
                lst.append(a[i])
                for j in range(i, n+1, i):
                    a[j] = 0
            print(a)
            print(lst)
            i += 1
        return(len(lst))
        print(len(lst))


sol = Solution()
#print(sol.countPrimes(5000000))
sol.countPrimes(25)
