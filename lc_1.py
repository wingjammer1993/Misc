class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        string_arr = []
        for idx, i in enumerate(s):
            if i == ' ':
                string_arr.append(0)
            else:
                string_arr.append(1)
            length += 1

        run = 0
        for i in range(length-1, -1, -1):
            if string_arr[i] == 1:
                run += 1
            elif run > 0:
                break

        return run






sol = Solution()
k = sol.lengthOfLastWord(" a ")
print(k)


