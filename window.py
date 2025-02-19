from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Tkinter Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):      
        self.__root.update_idletasks() 
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw() 

    def close(self):
        self.__running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()

# rectangel or lines for -> paths for and walls



