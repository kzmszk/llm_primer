import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'misdelivery/mamba-char-japanese-790m' # mamba 
model = AutoModelForCausalLM.from_pretrained(model_name, revision='test').to('cuda:0')
tokenizer = AutoTokenizer.from_pretrained(model_name, revision='test')

ds = load_dataset("elyza/ELYZA-tasks-100", revision="1.0.0")


def pred(example):
  
  with torch.no_grad():
      input_ids = tokenizer.encode(f"以下は、タスクを説明する指示です。要求を適切に満たす応答を書きなさい。\n\n### 指示:{example['input']}\n\n\n### 応答:\n", add_special_tokens=False, return_tensors="pt")
      output_ids = model.generate(
        input_ids.to(model.device),
        max_length=1024,
        do_sample=True,
        temperature=0.6,
        repetition_penalty=1.2
    )

  output_ids.tolist()[0]
  out = tokenizer.decode(output_ids.tolist()[0], skip_special_tokens=True)
  #print(result)
  example[model_name] = out
  return example

ds = ds.map(pred, batched=False)
ds["test"].to_csv(f"{model_name.replace('/', '-')}.csv", index=False)