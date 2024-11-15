import unittest
import pandas as pd
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        cat_plot = draw_cat_plot()
        self.assertIsNotNone(cat_plot, "Catplot function failed.")

    def test_heat_map(self):
        heat_map = draw_heat_map()
        self.assertIsNotNone(heat_map, "Heatmap function failed.")

if __name__ == "__main__":
    unittest.main()
