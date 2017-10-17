import collections
from collections import defaultdict
from operator import itemgetter

class Solution(object):

    def minStickers(self, stickers, target):

        target_set = list(target)
        count = 0
        possible_sets = []
        min_candidate = []
        min_count = 10000

        for sticker in stickers:
            intersect_set = [x for x in target_set if x in sticker]
            if len(intersect_set):
                possible_sets.append((list(intersect_set), sticker))

        exclusivity_dict = defaultdict(list)
        score_record = defaultdict(list)
        for index, key in enumerate(possible_sets):
            for idx, comparee in enumerate(possible_sets):
                if key[0] != comparee:
                    exclusive = [x for x in comparee[0] if x not in key]
                    exclusivity_dict[index].append((comparee[0], comparee[1], len(exclusive)))
            sorted_list = sorted(exclusivity_dict[index], key=itemgetter(2), reverse=True)
            word = list(key[0])
            score_record[index] = []
            score_record[index].append((key[0],key[1]))
            target_word = list(target)
            target_word = [x for x in target_word if x not in word]
            new_length = 0
            for identity, element in enumerate(sorted_list):
                new_word = list(word)
                new_word.extend(element[0])
                old = len(target_word)
                target_word = [x for x in target_word if x not in new_word]
                new_length = len(target_word)
                if old > new_length:
                    word.extend(element[0])
                    score_record[index].append((element[0], element[1]))
                if new_length == 0:
                    break
            if new_length != 0:
                del score_record[index]

        if 0 == len(score_record):
            min_count = -1
        else:
            max_len = 0
            full_list = []
            repeat_words = []
            all_tokens = list(target_set)
            count_list_val = {item: all_tokens.count(item) for item in all_tokens}
            for keys in score_record:
                count = len(score_record[keys])
                for val in score_record[keys]:
                    full_list.extend(val[1])
                count_list_key = {item: full_list.count(item) for item in full_list}
                for elem in count_list_val:
                    if count_list_val[elem] > count_list_key[elem]:
                        for x in range(1, (count_list_val[elem]-count_list_key[elem])+1):
                            repeat_words.append(elem)


                if len(repeat_words):
                   repeat = list(repeat_words)
                    max_new = []
                    while len(repeat):
                        max_len = 0
                        old_len = len(repeat)
                        intersect_sset = []
                        for val in score_record[keys]:
                            val_new = list(val[1])
                            for el in repeat:
                                if el in val_new:
                                    intersect_sset.append(el)
                                    val_new.remove(el)
                            if len(intersect_sset) > max_len:
                                max_new = list(intersect_sset)
                                max_len = len(intersect_sset)
                            intersect_sset = []
                        for el in max_new:
                            repeat.remove(el)
                        new_len = len(repeat)
                        if old_len == new_len:
                            break
                        else:
                            count = count + 1


                if count < min_count:
                    min_count = count
                    min_candidate = score_record[keys]
                    print(min_candidate)

        if min_candidate:
            all_letters = [x for x, y in min_candidate]
            all_letters = [item for sublist in all_letters for item in sublist]
            count_all_letters = {item: all_letters.count(item) for item in all_letters}
            all_tokens = list(target_set)
            count_list_val = {item: all_tokens.count(item) for item in all_tokens}
            unnecessary_words = []
            for elem in count_list_val:
                if count_all_letters[elem] > count_list_val[elem]:
                    unnecessary_words.append(elem)

            for elem in min_candidate:
                disjoint = [x for x in elem[0] if x not in unnecessary_words]
                if 0 == len(disjoint) and len(elem[0]) <= len(unnecessary_words):
                    min_count = min_count - 1

        return min_count


if __name__ == "__main__":
    stick = ["soil","since","lift","are","lot","twenty","put"]
    tag = "appearreason"
    s = Solution()
    number = s.minStickers(stick, tag)
    print(number)


