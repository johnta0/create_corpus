#!/usr/bin/env python3

import sys
import MeCab
import pandas as pd

# corpus would look like... ["the", "restaurant", "is", "very", "good", "."]

# returns corpus ["", "", ..., ""]
# 分かち書き
def devide_with_spaces():
    return 

def main():
    # first arg => input filename, second arg => output filename
    args = sys.argv
    # ファイル読み込み with panda
    df = pd.read_csv(args[1], skiprows=[0], sep=',')

    f = open(args[2], 'w')
    for index, row in df.iterrows():
        review_text = row[3]
        review_text.replace('。', '。\n')
        f.write(review_text)
    f.close()

    # 分かち書き
    tagger = MeCab.Tagger(-OWakati)

    text = open(args[2], 'r')
    wakati = tagger.parse(text)

    f = open(args[3], 'w')
    f.write(wakati)
    f.close()


if __name__ == '__main__':
    main()
