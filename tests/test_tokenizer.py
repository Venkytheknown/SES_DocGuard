# File: /SES-DocGuard/SES-DocGuard/tests/test_tokenizer.py

import unittest
from src.tokenizer.bpe_tokenizer import BPETokenizer

class TestBPETokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = BPETokenizer(vocab_size=32000, merge_operations=50000)

    def test_tokenization(self):
        text = "This is a test sentence."
        tokens = self.tokenizer.tokenize(text)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_detokenization(self):
        text = "This is a test sentence."
        tokens = self.tokenizer.tokenize(text)
        detokenized_text = self.tokenizer.detokenize(tokens)
        self.assertEqual(text, detokenized_text)

    def test_special_tokens(self):
        special_tokens = ['<pad>', '<unk>', '<bos>', '<eos>', '<sep>', '<cls>', '<mask>']
        for token in special_tokens:
            self.assertIn(token, self.tokenizer.special_tokens)

    def test_vocab_size(self):
        self.assertEqual(self.tokenizer.vocab_size, 32000)

if __name__ == '__main__':
    unittest.main()