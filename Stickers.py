import itertools

class Solution(object):

    def power_set(self, target_sticker):
        i_set = target_sticker
        return itertools.chain.from_iterable(itertools.combinations(i_set, r) for r in range(1, len(i_set) + 1))

    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        max_len = 0
        final_stick_list = {}
        max_set = []
        max_stick = ""
        target_set = list(target)

        while len(target_set):

            list_power_set = list(set(self.power_set(target_set)))
            list_power_set.sort(key=lambda t: len(t), reverse=True)
            len_old = len(target_set)
            max_len = 0
            max_set = []
            max_stick = ""
            for element in list_power_set:
                for sticker in stickers:
                    element = list(element)
                    intersect_set = [x for x in element if x in sticker]
                    if len(intersect_set) > max_len:
                        max_set = intersect_set
                        max_len = len(intersect_set)
                        max_stick = sticker
                if len(max_set):
                    final_stick_list[max_stick] = max_set
                    target_set = [x for x in target_set if x not in max_set]
                    break
            if len(target_set) == len_old:
                break

        if len(final_stick_list) and 0 == len(target_set):
            count = 0
        else:
            count = -1

        if 0 == len(target_set):
            for key, val in final_stick_list.items():
                count = count+1
                key_list = list(key)
                count_list_key = {item: key_list.count(item) for item in val}
                max_key = max(count_list_key.values())
                count_list_val = {item: val.count(item) for item in val}
                max_val = max(count_list_val.values())
                if max_val > max_key:
                    count = count + max_val - max_key

        return count






if __name__ == "__main__":
    stick = ["these","guess","about","garden","him"]
    tag = "atomher"
    s = Solution()
    number = s.minStickers(stick, tag)
    print(number)


