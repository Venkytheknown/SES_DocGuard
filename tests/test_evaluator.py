# File: /SES-DocGuard/SES-DocGuard/tests/test_evaluator.py

import unittest
from src.evaluator.metrics import calculate_metrics

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.ground_truth = {
            'CMM': {'true_positive': 10, 'false_positive': 2, 'false_negative': 1},
            'ESM': {'true_positive': 8, 'false_positive': 1, 'false_negative': 3},
            'AMM': {'true_positive': 5, 'false_positive': 0, 'false_negative': 2}
        }

    def test_accuracy(self):
        metrics = calculate_metrics(self.ground_truth)
        self.assertAlmostEqual(metrics['accuracy'], 0.75, places=2)

    def test_precision(self):
        metrics = calculate_metrics(self.ground_truth)
        self.assertAlmostEqual(metrics['precision'], 0.83, places=2)

    def test_recall(self):
        metrics = calculate_metrics(self.ground_truth)
        self.assertAlmostEqual(metrics['recall'], 0.71, places=2)

    def test_f1_score(self):
        metrics = calculate_metrics(self.ground_truth)
        self.assertAlmostEqual(metrics['f1_score'], 0.76, places=2)

if __name__ == '__main__':
    unittest.main()