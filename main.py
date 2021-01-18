import re


def word_count(string):
    z = string.lower().split()
    dic = {}
    for word in z:
        word = word.strip()
        word = re.sub('[^A-Za-z0-9-\']+', '', word)
        if word != '' and word not in dic and bool(re.match(r'^[\']', word)) == False:
            word_count = z.count(word)
            dic.update({word: word_count})
    return dic


def sort(string):
    dic = word_count(string)
    a = {k: v for k, v in sorted(
        dic.items(), key=lambda x: x[1], reverse=True)}
    max_word = list(a.keys())
    return max_word[0:3]
