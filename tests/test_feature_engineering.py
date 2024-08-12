import unittest
from src.feature_engineering import generate_features

class TestFeatureEngineering(unittest.TestCase):
    
    def test_generate_features(self):
        data = load_data('data/raw/sample.csv')
        features = generate_features(data)
        self.assertIn('SMA_20', features.columns)
        self.assertIn('Return', features.columns)

if __name__ == '__main__':
    unittest.main()
