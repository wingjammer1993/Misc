input_num = input()
dic_num = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
list_num = list(input_num)

for element in list_num:
    if int(element) in dic_num:
        dic_num[int(element)] = dic_num[int(element)] + 1

for element in dic_num:
    print("{}"' '"{}".format(element, dic_num[int(element)]))