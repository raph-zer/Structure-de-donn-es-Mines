from tkinter import Tk, Canvas, Label, Button, TOP, LEFT, RIGHT, BOTTOM
from random import randrange
from math import sqrt, abs

class Target:

    def __init__(self):
        self.__root = Tk()
        self.__root.geometry()
        self.__canvas = Canvas(self.__root, width=400, height=400, bg="red")
        self.__canvas.pack(side=TOP, padx=5, pady=5)
        self.draw_target()
        quit_button = Button(self.__root, text="Quit", command=self.__root.destroy)
        quit_button.pack(side=RIGHT, padx=3, pady=3)
        self.__button_shoot = Button(self.__root, text="Shoot", command=self.__shoot)
        self.__button_shoot.pack(side=LEFT, padx=5, pady=5)
        self.__score = 0
        self.__label_score = Label(self.__root, text=f"score : {self.__score}")
        self.__label_score.pack(side=BOTTOM, padx=5, pady=5)
        self.__tries = 5
        self.__root.bind_all('f', self.__oneshot)
        self.__crosshairs = (200,200)
        self.__recenter = 0
        while self.__tries > 0 :
            self.__movecross(self.__recenter)
        

    def execute(self):
        self.__root.mainloop()

    def draw_circle(self, x, y, r, color):
        """Draw a circle of centre (x, y) and radius r."""
        self.__canvas.create_oval(x - r, y + r, x + r, y - r, outline='red', fill=color)

    def draw_target(self):
        """The Canvas is now displaying a target."""
        self.__canvas.create_line(200, 0, 200, 400, fill='red')
        self.__canvas.create_line(0, 200, 400, 200, fill='red')
        cercle = 1
        for radius in range(180, 14, -30):
            if cercle == 5:
                self.draw_circle(200, 200, radius, 'red')
                self.__canvas.create_text(190, 210 - radius, text=f"{cercle}", font=('Times', '12', 'bold'), fill='ivory')
            else:
                self.draw_circle(200, 200, radius, 'ivory')
                self.__canvas.create_text(190, 210 - radius, text=f"{cercle}", font=('Times', '12', 'bold'), fill='red')
            cercle += 1
        self.__canvas.create_line(200, 0, 200, 400, fill='red')
        self.__canvas.create_line(0, 200, 400, 200, fill='red')

    def __increment_score(self, x, y):
        distance = sqrt((x - 200) ** 2 + (y - 200) ** 2)
        self.__score += (6 - distance // 30) * (distance < 6 * 30)

    def __shootonce(self):
        (x,y) = self.__crosshairs
        self.draw_circle(x, y, 5, 'black')
        self.__increment_score(x, y)
        self.__label_score['text'] = f"score : {self.__score}"

    def __oneshot(self, event):
        if self.__tries > 0 :
            self.__shootonce()
            self.__tries -= 1

    def __shoot(self):
        while self.__tries > 0:
            self.__shootonce()
            self.__tries -= 1
        self.__button_shoot['state'] = 'disabled'

    def draw_crosshairs(self, x, y):
        self.__canvas.create_line(x, 0, x, 400, fill='black')
        self.__canvas.create_line(0, y, 400, y, fill='black')
        self.draw_circle(x, y, 5, 'black')

    def __movecross(self,p):
        (x,y) = self.__crosshairs
        if x == 0 or x == 400 or y == 0 or y == 400 :
            self.__rebound()
        xsign = x//abs(x)
        ysign = y//abs(y)
        proba = randrange(100)
        x -= xsign*((proba <= p)-(proba > p))
        proba = randrange(100)
        y -= ysign*((proba <= p)-(proba > p))
        self.__crosshairs = (x,y)
        self.draw_crosshairs(x,y)

        
    def __rebound(self):
        """make the crosshairs rebound on the side"""
        (x,y) = self.__crosshairs
        if x == 0 :
            x = 1
        if x == 400 :
            x = 309
        if y == 0 :
            y = 1
        if y == 400 :
            y = 309
        self.__crosshairs = (x,y)
        self.draw_crosshairs(x,y)


if __name__ == '__main__':
    target = Target()
    target.execute()
