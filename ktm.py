# coding: utf-8
import json
import collections
from collections import Counter


def dakuten_handakuten_komoji(input_list, css_index, output_list):
    osca = input_list.copy()
    if css[css_index] == 'あ':
        osca[i] = 'ぁ'
        output_list.append(osca)
    if css[css_index] == 'い':
        osca[i] = 'ぃ'
        output_list.append(osca)
    if css[css_index] == 'う':
        osca[i] = 'ぅ'
        output_list.append(osca)
    if css[css_index] == 'さ':
        osca[i] = 'ざ'
        output_list.append(osca)
    if css[css_index] == 'し':
        osca[i] = 'じ'
        output_list.append(osca)
    if css[css_index] == 'す':
        osca[i] = 'ず'
        output_list.append(osca)
    if css[css_index] == 'せ':
        osca[i] = 'ぜ'
        output_list.append(osca)
    if css[css_index] == 'か':
        osca[i] = 'が'
        output_list.append(osca)
    if css[css_index] == 'き':
        osca[i] = 'ぎ'
        output_list.append(osca)
    if css[css_index] == 'く':
        osca[i] = 'ぐ'
        output_list.append(osca)
    if css[css_index] == 'け':
        osca[i] = 'げ'
        output_list.append(osca)
    if css[css_index] == 'こ':
        osca[i] = 'ご'
        output_list.append(osca)
    if css[css_index] == 'た':
        osca[i] = 'だ'
        output_list.append(osca)
    if css[css_index] == 'つ':
        osca[i] = 'づ'
        output_list.append(osca)
    if css[css_index] == 'つ':
        osca[i] = 'っ'
        output_list.append(osca)
    if css[css_index] == 'は':
        osca[i] = 'ぱ'
        output_list.append(osca)
    if css[css_index] == 'は':
        osca[i] = 'ば'
        output_list.append(osca)
    if css[css_index] == 'へ':
        osca[i] = 'ぺ'
        output_list.append(osca)
    if css[css_index] == 'へ':
        osca[i] = 'べ'
        output_list.append(osca)
    if css[css_index] == 'ほ':
        osca[i] = 'ぽ'
        output_list.append(osca)
    if css[css_index] == 'ほ':
        osca[i] = 'ぼ'
        output_list.append(osca)
    if css[css_index] == 'ゆ':
        osca[i] = 'ゅ'
        output_list.append(osca)
    if css[css_index] == 'よ':
        osca[i] = 'ょ'
        output_list.append(osca)


def word_reader(oss_last):

    with open('./words.json', mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    # Detect word in created word
    detected_words = list()
    for word in data['words']:
        for ol in oss_last:
            ol_word = ''.join(ol)
            if word in ol_word:
                detected_words.append(ol_word)

    # Count duplicate word which mean detected quotes
    word_counter = dict(Counter(detected_words))
    # sort dictionary
    sorted_word_counter = sorted(word_counter.items(), key=lambda kv: kv[1])
    # sorted list to dictionary
    word_dict = collections.OrderedDict(sorted_word_counter)
    for key, value in word_dict.items():
        print(key, '->', value - 1)


if __name__ == '__main__':
    os = "かい****"  # 7
    while True:
        os = input("Enemy Word(7): ")
        if len(os) == 7:
            break
    cs = "あいあよ"  # 4
    while True:
        cs = input("Player Word(4): ")
        if len(cs) == 4:
            break
    oss = list(os)
    css = list(cs)
    oss_first = list()
    oss_second = list()
    oss_third = list()
    oss_forth = list()
    #! TODO Fix Algorithm in one pattern
    for i, s in enumerate(oss):
        if s == '*' or s == '＊':
            osc = oss.copy()
            osc[i] = css[0]
            oss_first.append(osc)
            dakuten_handakuten_komoji(oss, 0, oss_first)
    for of in oss_first:
        # print(of)
        for i, s in enumerate(of):
            if s == '*' or s == '＊':
                osc = of.copy()
                osc[i] = css[1]
                oss_second.append(osc)
                dakuten_handakuten_komoji(of, 1, oss_second)

    for oc in oss_second:
        for i, s in enumerate(oc):
            if s == '*' or s == '＊':
                osc = oc.copy()
                osc[i] = css[2]
                oss_third.append(osc)
                dakuten_handakuten_komoji(oc, 2, oss_third)
    for ot in oss_third:
        for i, s in enumerate(ot):
            if s == '*' or s == '＊':
                osc = ot.copy()
                osc[i] = css[3]
                oss_forth.append(osc)
                dakuten_handakuten_komoji(ot, 3, oss_forth)

    # print(oss_forth)
    oss_last = list()
    # Array characters to array
    for of in oss_forth:
        oss_last.append(''.join(of))
    # Remove Duplicate
    oss_last = list(set(oss_last))
    word_reader(oss_last)
