class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]

        answer[0] nums in nums1 NOT in nums2
        answer[1] nums in nums2 NOT in nums1

        answer = [[], []]
        for i in range(nums1): for k in range(nums2): if nums1 i != nums2 i, append nums1 to answer [0] - continue or at else statement
        for i in range(nums2): for k in range(nums1): if nums 2 != nums1, append nums2 to answer [1] - continue
        return answer
        """
        # [1 2 3] [2 4 6]
        #  0 1 2   0 1 2 

        # [1 2 3 3] [1 1 2 2]
        #  0 1 2 3   0 1 2 3

        answer = [[], []]

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                 continue
            else:
                if nums1[i] not in answer[0]:
                    answer[0].append(nums1[i])
                else:
                    continue

        for i in range(len(nums2)):
            if nums2[i] in nums1:
                 continue
            else:
                if nums2[i] not in answer[1]:
                    answer[1].append(nums2[i])
                else:
                    continue

        return answer


        