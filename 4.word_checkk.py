f = open('relatedWords.csv', 'r')
word_list = f.read().splitlines()
f.close

new_word_list = []
for _word_pack in word_list:
    my_words = _word_pack.split(", ")
    _word = {"mainword": my_words[0], "extra": my_words[1:]}
    new_word_list.append(_word)

# __length= len(new_word_list)
# for i in range(__length-1):
#     www = list(set(new_word_list[i]["extra"]) & set(new_word_list[i+1]["extra"]))
#     if(len(www)>0):
#         print(i+1, new_word_list[i+1], len(www))
word_pair_list = []
for _word_pack in new_word_list:
    for _related in _word_pack["extra"]:
        if len(_related) < 3 or " " in _related:
            continue
        _word_pair = {"main": _word_pack["mainword"], "related": _related}
        word_pair_list.append(_word_pair)

print(word_pair_list)
print(len(word_pair_list))

word_pair_list.sort(key=lambda item: len(item['related']))

# kkk = sorted(word_pair_list, key = lambda k: (-len(word_pair_list[k]["related"]), k))
# print(word_pair_list, len(word_pair_list))

packer = {}
for word_pair in word_pair_list:
    try:
        packer[str(len(word_pair['related']))]
    except:
        packer[str(len(word_pair['related']))] = []
    packer[str(len(word_pair['related']))].append(word_pair)


for pack in packer:
    print("length",pack, "---", "count",len(packer[pack]))
    
    f = open(f'pairlist{pack}.csv', 'w')
    for words in packer[pack]:
        print(words)
        f.write(words['main'] + ', ' + words['related']+"\n")
    f.close()

# print(packer["3"], len(packer["3"]))