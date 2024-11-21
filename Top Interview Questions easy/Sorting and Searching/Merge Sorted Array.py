class Solution:   
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # case 1: nums2[ind] > nums1[0] and nums2[ind] > nums1[1] ... but nums2[ind] < nums1[shift]   
        # 1 3 5 [8] 9 0 0  |<-- insert 7    (7 is more than 1, 3 and 5, but less than 8. so we need to shift 8 and all latest elements to right by 1) 
        # 1 3 5 [8] 8 9 0  |we shift last 4 signs to right (1 last disapered)
        # 1 3 5 [7] 8 9 0  |<-- replace 8 with 7
        #
        # case 2: nums2[ind] > all of nums1
        # 1 3 5 7 8 [0] 0  |<-- insert 9
        # 1 3 5 7 8 [9] 0  |we put 9 instead of nums1[shift + m] (first 0 in nums1)
        
        shift = 0
        for ind in range(n):
            while nums2[ind] > nums1[shift] and shift < ind + m:
                shift+=1
            j = m + n - 1
            while j != shift:
                nums1[j] = nums1[j-1]
                j-=1                   
            nums1[shift] = nums2[ind]
        print(nums1)


sol = Solution()

a1 = [1, 5, 8, 0, 0, 0]
a2 = [0, 7, 11]
sol.merge(a1, 3, a2, 3)
