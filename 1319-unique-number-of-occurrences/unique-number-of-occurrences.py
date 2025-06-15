class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        int must occur unique amount of times, else false

        occurences = []
        arr_iter = iter(1)
        sort array in ascending order .sort()
        for i in range len arr,
            count = 1
            if arr i == next(arr_iter)
                count += 1
                occurences.append(count)
            else:
                occurences.append(count)
        return occurences

        occurences.sort()
        for i in range len occurences:
            if i = len occurances - 1:
                if occurences i == occurences i - 1
                    return False
                else:
                    continue
                    
            if occurences[i] == occurences[i + 1]:
                    return False
                else:
                    return True

        """

        arr.sort()
        occurrences = []
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                occurrences.append(count)
                count = 1

        # Append the last group's count
        occurrences.append(count)

        # Now check if all occurrences are unique
        occurrences.sort()
        for i in range(1, len(occurrences)):
            if occurrences[i] == occurrences[i - 1]:
                return False

        return True