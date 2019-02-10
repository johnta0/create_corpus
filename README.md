# create corups

1. csv ファイルを読み込む
2. `split_review.py` で
   1. レビューの部分だけを「。」区切りで改行し、ひとつのファイルにまとめる
   2. 分かち書きをする（「。」も１単語）

## Use

```
$ ./split_review.py <csv_filename> <devided_by_newline.txt> <wakatigaki_filename.txt>
```
