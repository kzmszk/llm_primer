# Dify 使ってみた

## やってみた
* toolはそれほどない。calendar アクセスとか自分で作るしかない？誰か作ってる？Tool Hub があればいいんだけど。
* input/output の線は一つだけ。分岐とかマージとかない。
* 無料でも　gpt3.5 系はしばらく使える(200requests?)
* ソースコードの出力機能とか、どっかにある？
* code interpreterは実行しなかった (self-hosted only?)

### chatbot と Agent と workflow
* chatbot はユーザクエリを受け取って回答を生成する。Retrievalは仕えるがAPI系のツールは使えない。chatなので対話履歴が利用される
* Agent はユーザクエリを受け取って回答を生成する。API系のツールを使うことができる
* workflow はファイルを受け取って何か生成したいとき用のもよう

### RAGを作成する
* 最低必要なノードは
  * 開始: 常に必要
  * 知識取得: RAGのメイン。事前にドキュメントを登録。
  * LLM: LLM問い合わせの制御
  * 回答: LLMの回答を出力
* 知識取得のoutput をLLMのコンテキストに設定し、プロンプトに指定する。コンテキストの取り扱いがわかりにくい。
* ハイブリッド検索とかできる
* 質問分類はあまり精度が良くない。
  * ラベルごとに処理を分岐できる

### Self-Hosting

### 作ってみた
* [作ったもの](https://cloud.dify.ai/apps)
* 変数の受け渡しに慣れること
* ロジックは単純なのしか作れない（今は）

## 参考
* [Difyでいろいろ作ってみた（割とガチめ）](https://future-architect.github.io/articles/20240402a/)
* [Dify概要 by npaka](https://note.com/npaka/n/n74d706ea225b)
* [Difyで生成アプリを作ってみよう](https://qiita.com/minorun365/items/4c5dba1de7977c386249)