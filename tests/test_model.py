# File: /SES-DocGuard/SES-DocGuard/tests/test_model.py

import unittest
from src.model.transformer import TransformerModel
from src.tokenizer.bpe_tokenizer import BPETokenizer

class TestTransformerModel(unittest.TestCase):

    def setUp(self):
        self.tokenizer = BPETokenizer(vocab_size=32000, merge_operations=50000)
        self.model = TransformerModel(num_encoder_layers=12, num_decoder_layers=12, hidden_size=768)

    def test_tokenization(self):
        sample_text = "This is a sample text for tokenization."
        tokens = self.tokenizer.tokenize(sample_text)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_model_forward_pass(self):
        sample_input = self.tokenizer.tokenize("This is a test input.")
        output = self.model(sample_input)
        self.assertIsNotNone(output)
        self.assertEqual(output.shape[0], 1)  # Assuming batch size of 1
        self.assertEqual(output.shape[1], self.model.hidden_size)

if __name__ == '__main__':
    unittest.main()