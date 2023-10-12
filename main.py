import tkinter as tk


# Создаем класс CanvasApp, который наследует от tk.Tk и представляет наше приложение
class CanvasApp(tk.Tk):
    def __init__(self):
        # Инициализируем родительский класс tk.Tk
        tk.Tk.__init__(self)

        # Создаем холст (Canvas) для рисования
        self.canvas = tk.Canvas(self)

        # Начальные координаты и размеры прямоугольников
        self.hx = 10  # Шаг изменения по горизонтали
        self.hy = 10  # Шаг изменения по вертикали
        self.x1 = 20  # Левая верхняя координата x
        self.y1 = 20  # Левая верхняя координата y
        self.x2 = 300  # Правая нижняя координата x
        self.y2 = 200  # Правая нижняя координата y

        # Список для хранения идентификаторов созданных прямоугольников
        self.rectangles = []

        # Размещаем холст так, чтобы он заполнил все доступное пространство окна
        self.canvas.pack(fill=tk.BOTH, expand=1)

        # Привязываем события клавиш к соответствующим методам
        self.bind('<Return>', self.draw)  # Нажатие Enter вызывает метод draw
        self.bind('<Escape>', self.close)  # Нажатие Escape вызывает метод close
        self.bind('<KeyPress-d>', self.delete)  # Нажатие клавиши "D" вызывает метод delete

    # Метод для рисования прямоугольников
    def draw(self, event):
        if self.x1 < self.x2 and self.y1 < self.y2:
            # Создаем прямоугольник на холсте
            rectangle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black")
            # Добавляем идентификатор прямоугольника в список
            self.rectangles.append(rectangle)
            # Изменяем координаты и размер для следующего прямоугольника
            self.x1 += self.hx
            self.y1 += self.hy
            self.x2 -= self.hx
            self.y2 -= self.hy

    # Метод для удаления последнего прямоугольника
    def delete(self, event):
        if len(self.rectangles) != 0:
            # Получаем идентификатор последнего прямоугольника из списка
            last_rectangle = self.rectangles.pop()
            # Удаляем прямоугольник с холста
            self.canvas.delete(last_rectangle)
            # Восстанавливаем предыдущие координаты и размер
            self.x1 -= self.hx
            self.y1 -= self.hy
            self.x2 += self.hx
            self.y2 += self.hy

    # Метод для закрытия приложения
    def close(self, event):
        self.destroy()


if __name__ == "__main__":
    app = CanvasApp()
    app.mainloop()
