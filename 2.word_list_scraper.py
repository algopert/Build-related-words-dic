import requests
import re
import time

with open('out.txt', 'r') as file:
    word_list = file.read().splitlines()
    

for _word in word_list:
    time.sleep(5)
    x = requests.get('https://relatedwords.io/'+_word)
    _str = x.text[13000:15000]
    qq = _str.split('\n')

    for _line in qq:
        if "Below is a massive list of" in _line:
            # print(ii, _line)
            result = re.findall("<i>(.*?)</i>", _line[:500])
            # print(result)
            break
        
    if len(qq)>1:
        _line = _word+", "+', '.join(result)+'\n'
        print(_line)
        f = open('relatedWords.csv', 'a')
        f.write(_line)
        f.close()
    else:
        print("------", _word)
