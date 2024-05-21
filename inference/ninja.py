from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Local-Novel-LLM-project/Ninja-v1-128k"
new_tokens = 1024

model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.float16, attn_implementation="flash_attention_2", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

system_prompt = "あなたはプロの小説家です。\n小説を書いてください\n-------- "

prompt = input("Enter a prompt: ")
system_prompt += prompt + "\n-------- "
model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")


generated_ids = model.generate(**model_inputs, max_new_tokens=new_tokens, do_sample=True)
print(tokenizer.batch_decode(generated_ids)[0])