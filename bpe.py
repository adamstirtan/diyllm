from importlib.metadata import version

import tiktoken

print("tiktoken version:", version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

#text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of Burlington."
text = "aksjldfkajsdflasdf"

print(text)

ids = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

print(ids)

for id in ids:
    print(id, tokenizer.decode([id]))

decoded_text = tokenizer.decode(ids)

print(decoded_text)