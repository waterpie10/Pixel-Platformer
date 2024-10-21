#completely functioning game!!!

from tkinter import Tk, Canvas, Button
import levels

window = Tk()
window.title("WIP Game")
window.geometry("1280x720")
canvas = Canvas(window, width=1280, height=720, bg="black")
canvas.pack()
vertical_speed = 0
horizontal_speed = 0
key_left = key_right = key_up =  key_down  = False
platforms = []
deathplatforms = []
levelnum = 0
teleport_object = None
visual_level = None
player = None
levelscompleted = []
for i in range(5):
    levelscompleted.append(False)

is_jumping = False
score = 0
is_paused = False

def create_player(level):
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == "s":
                x1 = col*80 + 25  # Left coordinate
                y1 = row*80 + 25  # Top coordinate
                x2 = x1 + 30  # Right coordinate
                y2 = y1 + 30  # Bottom coordinate
                player = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="blue")
                return player
            




def draw_level(level):
    global platforms, teleport_object
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == "p":
                platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+30, fill="red", outline="red")
                platforms.append(platform)
            elif level[row][col] == "rr":
                platform = canvas.create_rectangle(col*80, row*80, col*80+30, row*80+80, fill="red", outline="red")
                platforms.append(platform)
            elif level[row][col] == "rl":
                platform = canvas.create_rectangle(col*80+50, row*80, col*80+80, row*80+80, fill="red", outline="red")
                platforms.append(platform)
            elif level[row][col] == "rc":
                platform = canvas.create_rectangle(col*80+30, row*80+30, col*80+75, row*80+75, fill="red", outline="red")   
                platforms.append(platform)
            elif level[row][col] == "bc":
                platform = canvas.create_rectangle(col*80+30, row*80+30, col*80+75, row*80+75, fill="blue", outline="blue")   
                platforms.append(platform)
            elif level[row][col] == "lp":
                platform = canvas.create_rectangle(col*80, row*80, col*80+110, row*80+30, fill="red", outline="red")
                platforms.append(platform)
            elif level[row][col] == "cb":
                platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="blue", outline="blue")
                platforms.append(platform)
            elif level[row][col] == "d":
                platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="", outline="")
                deathplatforms.append(platform)
            elif level[row][col] == "thisway":
                canvas.create_text(col*80+40, row*80+40, text="This way ->", font=("Arial", 20), fill="white")
            elif level[row][col] == "blue":
                canvas.create_text(col*80+40, row*80+40, text="Do you trust blue...", font=("Arial", 20), fill="white")
            elif level[row][col] == "red":
                canvas.create_text(col*80+40, row*80+40, text="...or red?", font=("Arial", 20), fill="white")
            elif level[row][col] == "sc":
                canvas.create_text(col*80+60, row*80+40, text="Score: " + str(score), font=("Arial", 20), fill="white")
            elif level[row][col] == "t":
                platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="", outline="")
                teleport_object = platform

    canvas.update()


def key_press(event):
    global vertical_speed, horizontal_speed, key_left, key_right, key_up, key_down, is_jumping, is_paused
    if event.keysym == "a":
        key_left = True
    elif event.keysym == "d":
        key_right = True
    elif event.keysym == "w":
        key_up = True
        is_jumping = True
    elif event.keysym == "Escape":
        is_paused = not is_paused

def key_release(event):
    global vertical_speed, horizontal_speed, key_left, key_right, key_up, key_down
    if event.keysym == "a":
        key_left = False
        
    elif event.keysym == "d":
        key_right = False
        
    elif event.keysym == "w":
        key_up = False

        
        

        
def platform_collision():
    global player, platforms, is_jumping
    player_box = canvas.bbox(player)

    for platform in platforms:
        platform_box = canvas.bbox(platform)
        if (player_box[2] > platform_box[0] and player_box[0] < platform_box[2] and
            player_box[3] > platform_box[1] and player_box[1] < platform_box[3]):
            is_jumping = False
            return True


    return False


def teleport_collision():
    global player, platforms, teleport_object
    if player == None or teleport_object == None:
        return False
    player_box = canvas.bbox(player)
    teleport_box = canvas.bbox(teleport_object)
    if (player_box[0] < teleport_box[2] and player_box[2] > teleport_box[0] and player_box[1] < teleport_box[3] 
        and player_box[3] > teleport_box[1]):
        return True
        

def death_collision():
    global player, deathplatforms
    player_box = canvas.bbox(player)

    for platform in deathplatforms:
        platform_box = canvas.bbox(platform)
        if (player_box[2] > platform_box[0] and player_box[0] < platform_box[2] and
            player_box[3] > platform_box[1] and player_box[1] < platform_box[3]):
            return True


    return False


def determine_level():
    global levelnum, levelscompleted, score

    if teleport_collision():
        if not levelscompleted[0]:
            levelnum = 1
            levelscompleted[0] = True
            score += 1
        elif not levelscompleted[1]:
            levelnum = 2
            levelscompleted[1] = True
            score += 1
        elif not levelscompleted[2]:
            levelnum = 3
            levelscompleted[2] = True
            score += 1
        elif not levelscompleted[3]:
            levelnum = 4
            levelscompleted[3] = True

paused_text = None

def game_loop():
    global vertical_speed, horizontal_speed, level, player, visual_level, levelnum, key_up, platforms, deathplatforms 
    global is_jumping, paused_text

    if paused_text != None:
            canvas.delete(paused_text)
    
    if is_paused:
        paused_text = canvas.create_text(125, 75, text="Paused", font=("Arial", 30), fill="white")
        canvas.update()
        canvas.after(10, game_loop)
        return
    else:
        
        

        determine_level()

        if levelnum == 0:
            level = levels.get_level0()
            visual_level = draw_level(level)
            player = create_player(level)
            levelnum = "#"
        elif levelnum == 1:
            canvas.delete("all")
            level = []
            platforms = []
            deathplatforms = []
            level = levels.get_level1()
            visual_level = draw_level(level)
            player = create_player(level)
            levelnum = "#"
        elif levelnum == 2:
            canvas.delete("all")
            level = []
            platforms = []
            deathplatforms = []
            level = levels.get_level2()
            visual_level = draw_level(level)
            player = create_player(level)
            levelnum = "#"
        elif levelnum == 3:
            canvas.delete("all")
            level = []
            platforms = []
            deathplatforms = []
            level = levels.get_level3()
            visual_level = draw_level(level)
            player = create_player(level)
            levelnum = "#"
        elif levelnum == 4:
            canvas.delete("all")
            level = []
            platforms = []
            deathplatforms = []
            level = levels.get_level4()
            visual_level = draw_level(level)
            player = create_player(level)
            levelnum = "#"
        elif level == "#":
            pass
        

        friction = 1.2
        horizontal_speed /= friction

        if key_left:
            horizontal_speed = -5
        if key_right:
            horizontal_speed = 5
        
        if key_up and not is_jumping:
            vertical_speed = -18
            key_up = False

        vertical_speed += 0.8

        # Check for a collision with a platform after applying gravity
        canvas.move(player, 0, vertical_speed)
        if platform_collision():
            canvas.move(player, 0, -vertical_speed)
            vertical_speed = 0

        canvas.move(player, horizontal_speed, 0)
        if platform_collision():
            canvas.move(player, -horizontal_speed, 0)

        if death_collision():
            canvas.delete("all")
            canvas.create_text(640, 360, text="You died!", font=("Arial", 50), fill="red")
            canvas.create_text(640, 425, text="Score: " + str(score), font=("Arial", 30), fill="white")
            canvas.update()

        canvas.update()
        canvas.after(10, game_loop)

canvas.bind_all("<KeyPress>", key_press)
canvas.bind_all("<KeyRelease>", key_release)

game_loop()
window.mainloop()