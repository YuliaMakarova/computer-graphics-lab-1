import tkinter as tk

class CanvasApp(tk.Tk):
    """
    Класс CanvasApp представляет приложение для рисования прямоугольников с использованием библиотеки tkinter.

    Атрибуты:
    - canvas: холст для рисования прямоугольников
    - hx: шаг изменения по горизонтали
    - hy: шаг изменения по вертикали
    - x1: левая верхняя координата x текущего прямоугольника
    - y1: левая верхняя координата y текущего прямоугольника
    - x2: правая нижняя координата x текущего прямоугольника
    - y2: правая нижняя координата y текущего прямоугольника
    - rectangles: список идентификаторов созданных прямоугольников на холсте

    Методы:
    - draw: рисует прямоугольник на холсте и обновляет координаты для следующего
    - delete: удаляет последний нарисованный прямоугольник и восстанавливает предыдущие координаты
    - close: закрывает приложение
    """

    def __init__(self):
        """
        Инициализирует приложение, создает холст, задает начальные параметры прямоугольников и привязывает события.
        """
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self)
        self.hx = 10
        self.hy = 10
        self.x1 = 20
        self.y1 = 20
        self.x2 = 300
        self.y2 = 200
        self.rectangles = []
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.bind('<Return>', self.draw)
        self.bind('<Escape>', self.close)
        self.bind('<KeyPress-d>', self.delete)

    def draw(self, event):
        """
        Рисует прямоугольник на холсте и обновляет координаты для следующего прямоугольника.

        :param event: событие, вызывается при нажатии клавиши Enter
        """
        if self.x1 < self.x2 and self.y1 < self.y2:
            rectangle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black")
            self.rectangles.append(rectangle)
            self.x1 += self.hx
            self.y1 += self.hy
            self.x2 -= self.hx
            self.y2 -= self.hy

    def delete(self, event):
        """
        Удаляет последний нарисованный прямоугольник и восстанавливает предыдущие координаты.

        :param event: событие, вызывается при нажатии клавиши "D"
        """
        if len(self.rectangles) != 0:
            last_rectangle = self.rectangles.pop()
            self.canvas.delete(last_rectangle)
            self.x1 -= self.hx
            self.y1 -= self.hy
            self.x2 += self.hx
            self.y2 += self.hy

    def close(self, event):
        """
        Закрывает приложение при нажатии клавиши Escape.

        :param event: событие, вызывается при нажатии клавиши Escape
        """
        self.destroy()

if __name__ == "__main__":
    app = CanvasApp()
    app.mainloop()
