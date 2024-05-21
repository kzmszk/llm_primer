# 推論環境

## Ollama
* gguf 形式のモデルに対応。
* embedding は一部のモデルのみ（少ない）

## vllm
* [公式](https://github.com/vllm-project/vllm)
* 高速らしい
* 量子化 (GPTQ, AWQ) も対応
* [embedding は対応中](https://github.com/vllm-project/vllm/pull/3187)

## embedding
* [bge-m3 専用サーバ](https://github.com/puppetm4st3r/baai_m3_simple_server)
* [multilinugual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large)