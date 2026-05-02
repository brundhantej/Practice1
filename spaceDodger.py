import tkinter as tk
import random

WIDTH = 400
HEIGHT = 500
PLAYER_WIDTH = 40
ASTEROID_SIZE = 30

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Dodger")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.player_x = WIDTH // 2
        self.asteroids = []
        self.score = 0
        self.running = True
        self.base_speed = 5  

        # Player
        self.player = self.canvas.create_rectangle(
            self.player_x, HEIGHT - 40,
            self.player_x + PLAYER_WIDTH, HEIGHT - 10,
            fill="cyan"
        )

        self.score_text = self.canvas.create_text(
            10, 10,
            anchor="nw",
            fill="white",
            font=("Arial", 14, "bold"),
            text="Score: 0  Speed: 5"
        )

        self.root.bind("<a>", self.move_left)
        self.root.bind("<d>", self.move_right)

        self.update()

    def move_left(self, event):
        if self.player_x > 0:
            self.player_x -= 20
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        if self.player_x < WIDTH - PLAYER_WIDTH:
            self.player_x += 20
            self.canvas.move(self.player, 20, 0)

    def spawn_asteroid(self):
        x = random.randint(0, WIDTH - ASTEROID_SIZE)
        asteroid = self.canvas.create_oval(
            x, 0, x + ASTEROID_SIZE, ASTEROID_SIZE,
            fill="red"
        )
        self.asteroids.append(asteroid)

    def update(self):
        if not self.running:
            return

        current_speed = self.base_speed + (self.score // 50)


        if random.random() < 0.03:
            self.spawn_asteroid()

        for asteroid in self.asteroids[:]:  
            self.canvas.move(asteroid, 0, current_speed)

            ax1, ay1, ax2, ay2 = self.canvas.coords(asteroid)
            px1, py1, px2, py2 = self.canvas.coords(self.player)

            if (ax2 > px1 and ax1 < px2 and ay2 > py1 and ay1 < py2):
                self.game_over()
                return

            if ay1 > HEIGHT:
                self.canvas.delete(asteroid)
                self.asteroids.remove(asteroid)
                self.score += 1

        self.canvas.itemconfig(
            self.score_text,
            text=f"Score: {self.score}  Speed: {current_speed}"
        )

        self.root.after(30, self.update)

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24, "bold")
        )


root = tk.Tk()
game = Game(root)
root.mainloop()