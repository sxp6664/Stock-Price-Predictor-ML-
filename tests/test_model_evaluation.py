import unittest
from src.model_evaluation import evaluate_model

class TestModelEvaluation(unittest.TestCase):
    
    def test_evaluate_model(self):
        data = load_data('data/processed/sample.csv')
        model, X_test, y_test = train_random_forest_model(data, 'Close')
        rmse = evaluate_model(model, X_test, y_test)
        self.assertGreater(rmse, 0)

if __name__ == '__main__':
    unittest.main()
