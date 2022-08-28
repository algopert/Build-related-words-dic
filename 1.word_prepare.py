with open('word_pack.txt', 'r') as file:
    word_list = file.read().splitlines()
    
word_list = list(set(word_list)) 
word_list.sort()


print(word_list, len(word_list))

with open('out.txt', 'w') as f:
    f.write('\n'.join(word_list))