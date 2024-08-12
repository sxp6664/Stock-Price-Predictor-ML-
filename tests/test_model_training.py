import unittest
from src.model_training import train_random_forest_model

class TestModelTraining(unittest.TestCase):
    
    def test_train_random_forest_model(self):
        data = load_data('data/processed/sample.csv')
        model, X_test, y_test = train_random_forest_model(data, 'Close')
        self.assertIsNotNone(model)
        self.assertEqual(len(X_test), len(y_test))

if __name__ == '__main__':
    unittest.main()
