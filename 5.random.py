import random

for xxx in range(3,18):
    print(xxx)

    with open(f'pairlist{xxx}.csv', 'r') as file:
        word_list = file.read().splitlines()

        

    pp =  len(word_list)



    index_list = list(range(0,pp)) # list of integers from 1 to 99
                                # adjust this boundaries to fit your needs
    random.shuffle(index_list)
    print(index_list) # <- List of unique random numbers
    new_word_list = []
    for index in index_list:
        new_word_list.append(word_list[index])
        
    print(new_word_list)
    with open(f'new_pairlist{xxx}.csv', 'w') as f:
        f.write('\n'.join(new_word_list))
        
