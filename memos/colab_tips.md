# Colab の tips

## 参照
＊[公式ドキュメント](https://colab.research.google.com/notebooks/io.ipynb)


## secret
* サイドバーのlock マークをclickして秘密データを登録
```
from google.colab import userdata
userdata.get('secretName')
```

## open in colab
* 自分の github レポジトリは自動で colab に取り込める
  * オリジンのnotebook https://github.com/kzmszk/llm_primer/blob/main/ollama.ipynb
  * colab 上のURLは
  * https://colab.research.google.com/github/kzmszk/llm_primer/blob/main/ollama.ipynb
  * [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kzmszk/llm_primer/blob/main/ollama.ipynb)

## snippet
* ヘルプにsnippet検索機能がある。自分のコードを追加もできるらしい。snippetを登録しているnotebookを参照したほうが良いかも。

## code の非表示
* 下記のコードをセルに追加すると非表示にできる
```
# @title
```

## ローカルファイル
* upload & download 
```
from google.colab import files

# upload
uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# download
with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')
```
* google drive連携
```
from google.colab import drive
drive.mount('/content/drive')

with open('/content/drive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat /content/drive/My\ Drive/foo.txt
```
