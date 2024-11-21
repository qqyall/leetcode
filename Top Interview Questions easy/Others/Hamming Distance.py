class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        string1 = bin(x)
        string2 = bin(y)
        
        if len(string1) < len(string2):
            string1 = string1[:2] + "0" * (len(string2)-len(string1)) + string1[2:]   
        else:
            string2 = string2[:2] + "0" * (len(string1)-len(string2)) + string2[2:]
        
        dist_counter = 0
        for n in range(len(string1)):
            if string1[n] != string2[n]:
                dist_counter += 1

        return dist_counter


sol = Solution()
print(sol.hammingDistance(1, 4))
