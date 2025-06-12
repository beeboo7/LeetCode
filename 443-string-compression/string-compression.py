class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # for i in len(chars):
        # if len(chars) == 1: output.append(s)
        # check left and right
        # if i == 0 left not needed
        # return length of new array

        # a a b b c c c
        # 0 1 2 3 4 5 6

        write = 0  # index to write the compressed chars
        read = 0   # index to read through the original list

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count occurrences of the current char
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the char
            chars[write] = char
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write  # this is the new length

