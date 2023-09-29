import sys
import os

# Получите текущий каталог (где находится test_main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Добавьте каталог lab1 (где находится main.py) в sys.path
sys.path.append(os.path.join(current_dir, '..'))

import unittest
import tkinter as tk
from main import CanvasApp


class TestCanvasApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = CanvasApp()
        self.canvas = self.app.canvas

    def tearDown(self):
        self.root.destroy()

    def test_draw(self):
        initial_rectangles = len(self.canvas.find_all())
        event = tk.Event()
        self.app.draw(event)
        updated_rectangles = len(self.canvas.find_all())
        self.assertEqual(updated_rectangles, initial_rectangles + 1)

    def test_delete(self):
        event = tk.Event()
        self.app.draw(event)
        initial_rectangles = len(self.canvas.find_all())
        event = tk.Event()
        self.app.delete(event)
        updated_rectangles = len(self.canvas.find_all())
        self.assertEqual(updated_rectangles, initial_rectangles - 1)


if __name__ == '__main__':
    unittest.main()