import tkinter as tk


class MyButton(tk.Button):

    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.is_mine = False

    def __repr__(self):
        return f"MyButton{self.x} {self.y}"



class MineSweeper:

    ROWS = 5
    COLUMNS = 7
    window = tk.Tk()

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROWS):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgest(self):
        for i in range(MineSweeper.ROWS):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        self.create_widgest()
        self.print_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)


game = MineSweeper()
game.start()