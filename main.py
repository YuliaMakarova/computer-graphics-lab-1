import tkinter as tk


class CanvasApp(tk.Tk):
    def __init__(self):
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
        self.bind("<KeyPress-d>", self.delete)

    def draw(self, event):
        if self.x1 < self.x2 and self.y1 < self.y2:
            self.rectangles.append(self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black"))
            self.x1 += self.hx
            self.y1 += self.hy
            self.x2 -= self.hx
            self.y2 -= self.hy

    def delete(self, event):
        if len(self.rectangles) != 0:
            self.canvas.delete(self.rectangles.pop())
            self.x1 -= self.hx
            self.y1 -= self.hy
            self.x2 += self.hx
            self.y2 += self.hy

    def close(self, event):
        self.destroy()


if __name__ == "__main__":
    app = CanvasApp()
    app.mainloop()
