# https://leetcode.com/problems/minimum-common-value/
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_ptr = 0
        nums2_ptr = 0
        while nums1_ptr < len(nums1) \
        and nums2_ptr < len(nums2) :
            if nums1[nums1_ptr] == nums2[nums2_ptr] :
                return nums1[nums1_ptr]
            elif nums1[nums1_ptr] < nums2[nums2_ptr] :
                nums1_ptr += 1
            elif nums1[nums1_ptr] > nums2[nums2_ptr] :
                nums2_ptr += 1
        return -1
