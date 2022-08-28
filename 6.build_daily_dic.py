
pack_list = []
for xxx in range(4, 9):
    with open(f'new_pairlist{xxx}.csv', 'r') as file:
        word_list = file.read().splitlines()

    pack_list.append(word_list)


print(len(pack_list))
daily_dic = []
pp = 1
for index in range(len(pack_list[4])):
    for kk in range(len(pack_list)):
        daily_dic.append(str(pp) + ', ' + pack_list[kk][index])
        pp += 1


print(daily_dic)

with open('daily_dic.csv', 'w') as f:
    f.write('\n'.join(daily_dic))
