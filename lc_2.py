class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_list = str.split(' ')

        if len(word_list) != len(pattern):
            return False
        else:
            hash_map = {}
            for idx, i in enumerate(pattern):
                if i not in hash_map:
                    if idx < len(word_list):
                        if word_list[idx] not in hash_map.values():
                            hash_map[i] = word_list[idx]
                        else:
                            return False
                    else:
                        return False
                else:
                    if word_list[idx] != hash_map[i]:
                        return False

            return True




s = Solution()
print(s.wordPattern('aaa', 'amr amr amr amr'))