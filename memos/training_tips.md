# LLM 学習のメモ


|   |   |
|---|---|
|   |   |

## ためす
### general
* [生成AI概論コース(真面目)](https://github.com/microsoft/generative-ai-for-beginners)
* [stanford cs25](https://web.stanford.edu/class/cs25/)
* [ML paper of the Week](https://github.com/dair-ai/ML-Papers-of-the-Week?tab=readme-ov-file)

### finetuning
* [phi3-mini unsloth でFTする](https://colab.research.google.com/drive/1zral6IXIwSd3nQGQSE_5WM_4RyqLFKYA?usp=sharing)
* [Finetuning ベストプラクティス w&b](https://assets-global.website-files.com/642b4436f5352516bbf9ca61/651af64bcf7b9f75c71eb928_LLMWhitepaper2-FinalFinal-compressed.pdf)
* [GaLore](https://note.com/oshizo/n/nedc0afbaf10c)

### LLMをゼロから作る系
* https://zenn.dev/selllous/articles/transformers_pretrain_to_ft
* https://note.com/kan_hatakeyama/n/nbeab063ddd94
* https://qiita.com/umaxiaotian/items/5d059181803809065a7a
* https://github.com/ce-lery/japanese-mistral-300m-recipe



## 一言まとめ
### [LLM作るのは簡単](https://logmi.jp/tech/articles/329756)
* データとGPT-NeoXでok
* 分散学習は中規模までならData Parallelだけのほうが楽。
* Data Parallel: PyTorch FSDP, DeepSpeed Zero
* 3D Parallel: Megatron, Megatron DeepSpeed, GPT NeoX
* Mixture of Expert は面倒くさい

### [unsloth](https://note.com/npaka/n/na3f5abf30629)
* mistral/llama 系列のファインチューニングが高速になる
* phi3 もできるっぽい[note](https://colab.research.google.com/drive/1zral6IXIwSd3nQGQSE_5WM_4RyqLFKYA?usp=sharing)。


### [ファインチューニングを極小メモリで可能にする](https://github.com/GreenBitAI/green-bit-llm)
* llama3 8b を 24GB GPUでフルパラメタファインチューニングできる

### [acceralteでbatchサイズを最適化する](https://qiita.com/m__k/items/518ac10399c6c8753763)
* シンプルなやり方から acceralate の導入、バッチサイズの最適化まで。

### [margekit-evolve](https://soysoftware.sakura.ne.jp/archives/3872)
* sakana.ai の進化的最適化マージを実装した
* llama3-70b をローカルで実行して評価値を取得しながら進化
* すごい性能がよいらしい

### [Chat Vectorでマージ](https://qiita.com/jovyan/items/ee6affa5ee5bdaada6b4)
* 2つのモデルの差分を作成して、他のモデルにマージすることで強化

### [PhiでMoE](https://zenn.dev/zaburo_ch/articles/88e35e5c80f974)

### [日本語LLM評価セットまとめ](https://note.com/npaka/n/ndec10f78fe2f)

### [Elyza-task-100 の自動評価スクリプト](https://github.com/Northern-System-Service/gpt4-autoeval)

### [WandB 評価ベストプラクティス](https://site.wandb.ai/wp-content/uploads/2024/04/LLM-Evaluation-Whitepaper.pdf)


### [指示データセットは少なくてもOK](https://www.databricks.com/jp/blog/limit-less-more-instruction-tuning)

> MPT-7B-InstructとMPT-30B-Instructに対応するインストラクション・チューニングデータセットで あるInstruct-v1 （59.3kサンプル、 dolly_hhrlhfとも 呼ばれる ）と Instruct-v3 （56.2kサンプル）、および LIMAデータセット （1kサンプル）です。 (1)MMLUやBIG-benchのような伝統的なNLPベンチマークをベースと した、Mosaicの効率的なオープンソースEvalGauntletと、(2) GPT-4をジャッジとするAlpacaEvalの モデルベース評価スイートを用いて、モデルのパフォーマンスを評価します。

### [指示データセットをローカルLLMで作る](https://qiita.com/toshi_456/items/2794bdbf6d95e6140db1)

### [事前学習用のデータを生成する方法](https://huggingface.co/blog/cosmopedia)
* phiでやってることを再現しようとしてる。コード付き。英語だけかな。
* https://huggingface.co/HuggingFaceTB

### [事前学習に warmup stable decay learning rate schedulerを導入して成功した MiniCPM](https://arxiv.org/abs/2404.06395)

@import "./markdown_howto.md"