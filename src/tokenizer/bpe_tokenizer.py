# File: /SES-DocGuard/SES-DocGuard/src/tokenizer/bpe_tokenizer.py

import os
import json
import numpy as np
from collections import Counter

class BPETokenizer:
    def __init__(self, vocab_size=32000, merge_operations=50000, min_frequency=2):
        self.vocab_size = vocab_size
        self.merge_operations = merge_operations
        self.min_frequency = min_frequency
        self.bpe_codes = {}
        self.vocab = Counter()

    def train(self, texts):
        for text in texts:
            tokens = text.split()
            self.vocab.update(tokens)

        # Filter vocabulary based on min_frequency
        self.vocab = {word: freq for word, freq in self.vocab.items() if freq >= self.min_frequency}
        self._learn_bpe()

    def _learn_bpe(self):
        # Initialize BPE codes
        bpe_codes = {}
        for _ in range(self.merge_operations):
            pairs = Counter()
            for word, freq in self.vocab.items():
                symbols = word.split()
                for i in range(len(symbols) - 1):
                    pairs[(symbols[i], symbols[i + 1])] += freq

            if not pairs:
                break

            # Get the most frequent pair
            best_pair = pairs.most_common(1)[0][0]
            bpe_codes[best_pair] = len(bpe_codes)

            # Merge the best pair in the vocabulary
            new_vocab = {}
            for word, freq in self.vocab.items():
                new_word = self._merge_word(word, best_pair)
                new_vocab[new_word] = new_vocab.get(new_word, 0) + freq
            self.vocab = new_vocab

        self.bpe_codes = bpe_codes

    def _merge_word(self, word, pair):
        first, second = pair
        new_word = word.replace(' '.join(pair), ''.join(pair))
        return new_word

    def encode(self, text):
        tokens = text.split()
        encoded_tokens = []
        for token in tokens:
            if token in self.vocab:
                encoded_tokens.append(token)
            else:
                encoded_tokens.append('<unk>')  # Unknown token
        return encoded_tokens

    def save(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.bpe_codes, f)

    def load(self, filepath):
        with open(filepath, 'r') as f:
            self.bpe_codes = json.load(f)