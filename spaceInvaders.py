import tkinter as tk

# PARAMETERS
WIDTH = 600
HEIGHT = 450

def make_enemy_sprite():
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01101110110",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000"
    ]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == 1:
                img.put = ("#ffffff", (x,y))

    return img

def make_player_sprite():
    h=16
    w=24

    img = tk.PhotoImage(width=w, height=h)

    for y in range(h):
        for x in range(w):
            if 6 <= x <= 17 and y>=6:
                img.put("#9900FF", (x,y))


    return img

root = tk.Tk()
root.title("Space Invaders")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player_img = make_player_sprite()
enemy_img = make_enemy_sprite()

# create player
player = canvas.create_image(WIDTH//2, HEIGHT-40, image=player_img, anchor="center")


def start():
    # create player
    player = canvas.create_image(WIDTH//2, HEIGHT-40, image=player_img, anchor="center")
    game_loop()

# enemy formation; enemies move as group
ROWS = 4
COLS = 8
CELL = 32

enemies = [] # store enemies in list

def create_enemy_formation():
    enemies.clear()
    start_x = 100
    start_y = 60

    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c*CELL
            y = start_y + r*CELL

            e = canvas.create_image(x, y, image=enemy_img, anchor="nw")
            enemies.append(e)

# player controls
def move_left(event):
    canvas.move(player, -15, 0)

def move_right(event):
    canvas.move(player, 15, 0)

# bind
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# lasers
lasers = [] # list of lasers

def make_laser_sprite():
    img = tk.PhotoImage(width=4, height=10)

    for y in range(10):
        for x in range(4):
            img.put("#48ff00", (x,y))
    
    return img

laser_img = make_laser_sprite()

def shoot(event):
    if len(lasers)>0:
        return
    # bounding box
    px1, px2, py1, py2 = canvas.bbox(player)
    l = canvas.create_image((px1+px2)//2, py1, image=laser_img, anchor="s")
    lasers.append(l)

root.bind("<space>", shoot)

# collisions -- helper function, returns bool
def collision(a,l): # a: alien, l: laser
    ax1, ay1, ax2, ay2 = canvas.bbox(a) # alien bbox
    lx1, ly1, lx2, ly2 = canvas.bbox(l) # laser bbox

    return ax1 < lx2 and ax2 < lx1 and ay1 < ly2 and ay2 > ly1 # when True, have overlap

# formation movement
enemy_dx = 4

def move_enemies():
    global enemy_dx

    hit_wall = False
    for e in enemies:
        x1, y1, x2, y2 = canvas.bbox(e)

        if x2 >= WIDTH-10 and enemy_dx > 0:
            hit_wall = True

        if x1 <= 10 and enemy_dx < 0:
            hit_wall = True

    if hit_wall:
        enemy_dx = -enemy_dx
        for e in enemies:
            canvas.move(e, 0, 15) # move enemy, don't move on x, move down on y by 15

    else:
        for e in enemies:
            canvas.move(e, enemy_dx, 0) # move enemy, move by dx, don't move on y

# game loop
def game_loop():
    global alive

    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "red")
        return
    
    move_enemies()

    # laser movement
    for l in lasers[:]: # [:] copy of list, protects original list
        canvas.move(l, 0, -12)
        x1, y1, x2, y2 = canvas.bbox(l)
        if y2<0:
            canvas.delete(l)
            lasers.remove(l)

    # laser-alien collision
    for l in lasers[:]:
        for e in enemies[:]:
            if collision(l, e):
                canvas.delete(l)
                canvas.delete(e)

                if l in lasers:
                    lasers.remove(l)

                if e in enemies:
                    enemies.remove(e)
            
            break

    # end game condition
    for e in enemies:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        px1, py1, px2, py2 = canvas.bbox(player)

        if ey2 <= py1:
            alive = False


    root.after(40, game_loop)

def reset(event = None):
    global alive, enemy_dx
    canvas.delete("all")
    lasers.clear()
    enemies.clear()

    alive = True
    enemy_dx = 4

    create_enemy_formation()
    start()

root.bind("r", reset)

reset()
root.mainloop()