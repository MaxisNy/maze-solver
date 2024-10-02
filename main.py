from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, canvas_width, canvas_height) -> None:
        self.width = canvas_width
        self.height = canvas_height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        
        # use close method for the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=canvas_width, height=canvas_height, bg="white")
        self.__canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)

class Point():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():

    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas: Canvas, fillColor: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fillColor, width=2)

def main():
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(500, 500))
    win.draw_line(line, "red")
    win.wait_for_close()
    
if __name__ == "__main__":
    main()

