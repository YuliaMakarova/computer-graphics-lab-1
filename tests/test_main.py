import sys
import os
import unittest
import tkinter as tk
from main import CanvasApp

# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))

# Создаем класс TestCanvasApp, который будет содержать тесты
class TestCanvasApp(unittest.TestCase):
    def setUp(self):
        # Создаем корневое окно Tkinter
        self.root = tk.Tk()
        # Создаем экземпляр CanvasApp
        self.app = CanvasApp()
        # Получаем доступ к холсту приложения
        self.canvas = self.app.canvas

    def tearDown(self):
        # Закрываем корневое окно после завершения каждого теста
        self.root.destroy()

    def test_draw(self):
        # Тест для проверки метода draw
        initial_rectangles = len(self.canvas.find_all())  # Получаем начальное количество прямоугольников
        event = tk.Event()  # Создаем событие (для имитации события клавиши Enter)
        self.app.draw(event)  # Вызываем метод draw
        updated_rectangles = len(self.canvas.find_all())  # Получаем обновленное количество прямоугольников
        self.assertEqual(updated_rectangles, initial_rectangles + 1)  # Сравниваем с ожидаемым результатом

    def test_delete(self):
        # Тест для проверки метода delete
        event = tk.Event()  # Создаем событие
        self.app.draw(event)  # Рисуем прямоугольник
        initial_rectangles = len(self.canvas.find_all())  # Получаем начальное количество прямоугольников
        event = tk.Event()  # Создаем событие (для имитации события клавиши "d")
        self.app.delete(event)  # Вызываем метод delete
        updated_rectangles = len(self.canvas.find_all())  # Получаем обновленное количество прямоугольников
        self.assertEqual(updated_rectangles, initial_rectangles - 1)  # Сравниваем с ожидаемым результатом



if __name__ == '__main__':
    unittest.main()
