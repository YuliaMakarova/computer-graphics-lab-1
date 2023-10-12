import sys
import os
import unittest
import tkinter as tk
from main import CanvasApp

# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))

class TestCanvasApp(unittest.TestCase):
    """
    Класс TestCanvasApp содержит юнит-тесты для проверки функциональности класса CanvasApp.

    Атрибуты:
    - root: корневое окно Tkinter
    - app: экземпляр CanvasApp, объект, который будет тестироваться
    - canvas: холст приложения для тестирования

    Методы:
    - setUp: выполняется перед каждым тестом, создает корневое окно и экземпляр CanvasApp
    - tearDown: выполняется после каждого теста, закрывает корневое окно
    - test_draw: тест для проверки метода draw
    - test_delete: тест для проверки метода delete

    Параметры методов:
    - event: объект события, используется для имитации событий клавиш
    """

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
