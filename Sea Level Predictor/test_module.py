import unittest
import pandas as pd
from sea_level_predictor import create_sea_level_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_data_loading(self):
        # Test if the data loads correctly
        df = pd.read_csv('epa-sea-level.csv')
        self.assertTrue(df.shape[0] > 0)  # Check if the data has rows
        self.assertIn('Year', df.columns)
        self.assertIn('CSIRO Adjusted Sea Level', df.columns)

if __name__ == '__main__':
    unittest.main()
