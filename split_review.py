#!/usr/bin/env python3

import sys
import MeCab
import pandas as pd

# corpus would look like... ["the", "restaurant", "is", "very", "good", "."]



# returns text devided by \n
def devide_to_lines(review_text):

    return

# returns corpus ["", "", ..., ""]
# 分かち書き
def devide_with_spaces():
    return 

def main():
    # first arg => input filename, second arg => output filename
    args = sys.argv
    # args[0] => 'split_review.py'
    input_filename = args[1]
    output_filename = args[2]
    # ファイル読み込み with panda
    reader = pd.read_csv(input_filename, skiprows=[0], chunksize=50)

    for df in reader:
        for index, row in df.iterrows():
            print(row[3])
            print('--------')
            # reviews = extract_reviews(df)

if __name__ == '__main__':
    main()