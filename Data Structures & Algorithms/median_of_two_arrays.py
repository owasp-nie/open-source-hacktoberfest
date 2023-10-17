class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = []
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] <= nums1[i]:
                nums3.append(nums2[j])
                j += 1
            nums3.append(nums1[i])
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1

        length = len(nums3)
        if length % 2 == 0:
            return float(nums3[length//2] + nums3[length//2 - 1]) / 2
        else:
            return nums3[len(nums3) // 2]

list1 = list(map(int, input("Enter numbers for the first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter numbers for the second list separated by spaces: ").split()))

solution_instance = Solution()
print(solution_instance.findMedianSortedArrays(list1, list2))
