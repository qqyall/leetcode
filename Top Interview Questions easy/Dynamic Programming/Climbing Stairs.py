class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        lst = [0 for _ in range(n)]
        lst[0], lst[1] = 1, 2
            
        for i in range(2, n):
            lst[i] = lst[i - 1] + lst[i - 2]

        return lst[n-1]

class Solution2:
    def climbStairs(self, n: int) -> int:
        stack = []
        stack.append(n)

        queue = []
        queue.append(n)


        while len(queue)>0:
            tmp = queue.pop(0)

            if tmp - 1 > 2:
                stack.append(tmp - 1)
                queue.append(tmp - 1)

            if tmp - 2 > 2:
                stack.append(tmp - 2)
                queue.append(tmp - 2)
            
        values = {}
        values[1] = 1
        values[2] = 2

        while len(stack) > 0:
            num = stack.pop(len(stack) - 1)
            if num not in values:
                value = values.get(num - 1) + values.get(num - 2)
                values[num] = value

        return values.get(n)
    
        
sol = Solution1()
ar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1000]
for i in ar:
    print(i, sol.climbStairs(i))
