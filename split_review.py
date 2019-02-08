#!/usr/bin/env python3

import re, sys
import MeCab
import pandas as pd

# corpus would look like... ["the", "restaurant", "is", "very", "good", "."]

# returns corpus ["", "", ..., ""]
# 分かち書き

def newline(input_filename, output_filename):
    df = pd.read_csv(input_filename, sep=',')
    f = open(output_filename, 'w')
    for _, row in df.iterrows():
        review_text = row[3]
        if type(review_text) is not str:
            continue
        review_text = re.sub(r'。', r'。\n', review_text)
        review_text = re.sub(r'\n{2,}', '\n', review_text)
        f.write(review_text)
    f.close()
    return

def wakati(input_filename, output_filename):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    with open(input_filename, 'r') as f:
        wakati_f = open(output_filename, 'w')
        for line in f:
            wakati = tagger.parse(line)
            wakati_f.write(wakati)
        wakati_f.close()


def main():
    # args[1] => csv, args[2] => devided with new line, args[3] => wakati gaki text
    args = sys.argv
    newline(args[1], args[2])
    if args[3] is not None:
        wakati(args[2], args[3])


if __name__ == '__main__':
    main()
