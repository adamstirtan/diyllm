import re


class TokenizerV1:
    def __init__(self, vocabulary):
        self.str_to_index = vocabulary
        self.index_to_str = {i:s for s,i in vocabulary.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_index[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.index_to_str[i] for i in ids])
        text = re.sub(r'\s([,.?_!"()\'])', r'\1', text)
        return text

class TokenizerV2:
    def __init__(self, vocabulary):
        self.str_to_index = vocabulary
        self.index_to_str = {i:s for s,i in vocabulary.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_index
            else "<|unk|>" for item in preprocessed
        ]
        ids = [self.str_to_index[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.index_to_str[i] for i in ids])
        text = re.sub(r'\s([,.?_!"()\'])', r'\1', text)
        return text