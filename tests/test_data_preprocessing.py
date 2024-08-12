import unittest
from src.data_preprocessing import load_data, clean_data

class TestDataPreprocessing(unittest.TestCase):
    
    def test_load_data(self):
        data = load_data('data/raw/sample.csv')
        self.assertIsNotNone(data)
    
    def test_clean_data(self):
        data = load_data('data/raw/sample.csv')
        cleaned_data = clean_data(data)
        self.assertFalse(cleaned_data.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
