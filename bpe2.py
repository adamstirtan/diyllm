import tiktoken

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")
encoded_text = tokenizer.encode(raw_text, allowed_special={"<|endoftext|>"})

print(f"Encoded {len(encoded_text)} tokens.")