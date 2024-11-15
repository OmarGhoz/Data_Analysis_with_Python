import unittest
import time_series_visualizer

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsNotNone(fig, "Line plot function failed.")
    
    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsNotNone(fig, "Bar plot function failed.")
    
    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsNotNone(fig, "Box plot function failed.")

if __name__ == "__main__":
    unittest.main()
