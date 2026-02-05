import tkinter as tk
import random

score = 0
player = None


# declare constants
WIDTH = 400
HEIGHT = WIDTH*.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20
MOVE_SPEED = 20

# build window
root=tk.Tk()
root.title("- , `  . a void   -   t h  e   -  blo ck  s .. .   .")

canvas=tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "#2B2B2B")
canvas.pack()

# make player
def make_player():
    global player
    player = canvas.create_rectangle(180, 250, 180+PLAYER_SIZE, 250+PLAYER_SIZE, fill = "#B6B6B6")

# make list to hold enemies
enemies = []

# movement functions

def move_left(event):
    canvas.move(player, -MOVE_SPEED, 0)

def move_right(event):
    canvas.move(player, MOVE_SPEED, 0)

def move_up(event):
    canvas.move(player, 0, -MOVE_SPEED)

def move_down(event):
    canvas.move(player, 0, MOVE_SPEED)

# binding buttons
root.bind("a", move_left)
root.bind("d", move_right)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

root.bind("w", move_up)
root.bind("s", move_down)

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# enemies
enemy_colors = ["#4B4B4B","#504F4F","#636161","#7E7D7D","#8D8B8B", "#9C9B9B"]
def spawn_enemy():
    x = random.randint(0, WIDTH-ENEMY_SIZE)
    enemy = canvas.create_rectangle( x, 0, x+ENEMY_SIZE, ENEMY_SIZE, fill = enemy_colors[random.randint(0,5)])
    enemies.append(enemy)


# make alive bool
alive = True

def run_game(score):
    graveyard = canvas.create_rectangle(0, HEIGHT-10, WIDTH, HEIGHT, fill = "cyan")
    global alive
    if not alive:
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "game-o v e  r .. .   .", fill = "#ffffff", font = ("Courier", 20))
        return
    
    if random.randint(1,20)==1:
        spawn_enemy()

    for enemy in enemies:
        canvas.move(enemy, 0, 10)

        if canvas.bbox(enemy) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
            px1, py1, px2, py2 = canvas.bbox(player)

            if ex1<px2 and ex2>px1 and ey1<py2 and ey2>py1:
                alive = False
        
        if canvas.bbox(enemy) and canvas.bbox(graveyard):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
            gx1, gy1, gx2, gy2 = canvas.bbox(graveyard)
            
            if ex1<gx2 and ex2>gx1 and ey1<gy2 and ey2>gy1:
                score+=1
                print(score)

    
    root.after(50, run_game)

def game(score):
    make_player()
    run_game(score)

# reset button
def reset(score):
    canvas.delete("all")
    global alive
    alive = True
    score = 0
    game(score)

reset_button = tk.Button(root, text = "reset", command = reset, bg = "#2B2B2B", font = ("Courier", 10))
reset_button.pack()


game(score)
root.mainloop()