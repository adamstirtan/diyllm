import re
from tokenizer import TokenizerV2

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(raw_text[:100])
print("Total characters:", len(raw_text))

preprocessed = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

print("Vocabulary size:", len(all_tokens))

vocabulary = {token: index for index, token in enumerate(all_tokens)}

tokenizer = TokenizerV2(vocabulary)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of Burlington."

text = " <|endoftext|> ".join([text1, text2])

ids = tokenizer.encode(text)
print("Encoded IDs:", ids)

decoded_text = tokenizer.decode(ids)
print("Decoded text:", decoded_text)