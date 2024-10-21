from tkinter import Tk, Canvas, Button, Entry
import levels
from PIL import Image, ImageTk
# def save_game():
#     global levelscompleted, score
#     savefile = open("savefile.txt", "w")
#     for i in range(len(levelscompleted)):
#         if levelscompleted[i]:
#             savefile.write("1")
#         else:
#             savefile.write("0")
#     savefile.write("\n")
#     savefile.write(str(score))
#     savefile.close()

# def load_game():
#     global levelscompleted, score
#     savefile = open("savefile.txt", "r")
#     savefile.readline()
#     savefile.readline()
#     levelscompleted = []
#     for i in range(5):
#         if savefile.read(1) == "1":
#             levelscompleted.append(True)
#         else:
#             levelscompleted.append(False)
#     score = int(savefile.readline())
#     savefile.close()


window = None
canvas = None
vertical_speed = None
horizontal_speed = None
key_left = key_right = key_up =  key_down  = False
platforms = []
deathplatforms = []
winplatforms = []
movingplatforms = []
levelnum = None
teleport_object = None
visual_level = None
player = None
levelscompleted = []
is_jumping = False
score = None
is_paused = False
paused_text = None
gravity_cheat = False
direction = None
score_text = None
image_garbage_collection_prevention = None
bosskey = None
desktop_image = None

def initialise_game():
    global window, canvas, vertical_speed, horizontal_speed, key_left, key_right, key_up,  key_down 
    global platforms, deathplatforms, levelnum, teleport_object, visual_level, player, levelscompleted
    global is_jumping, score, is_paused, paused_text, movingplatforms, gravity_cheat, direction, winplatforms
    global score_text, bosskey, desktop_image, image_garbage_collection_prevention


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
    winplatforms = []
    movingplatforms = []
    levelnum = 0
    teleport_object = None
    visual_level = None
    player = None
    levelscompleted = []
    for i in range(6):
        levelscompleted.append(False)

    is_jumping = False
    score = 0
    is_paused = False
    paused_text = None
    gravity_cheat = False
    direction = 1
    score_text = None
    image_garbage_collection_prevention = []
    bosskey = False
    desktop_image = None

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

    def get_fire_image():
        fire_image = Image.open("fire.png")
        fire_image = fire_image.resize((80, 80), Image.ANTIALIAS)
        fire_image = ImageTk.PhotoImage(fire_image)
        return fire_image
    
   

    def draw_level(level):
        global platforms, teleport_object, score_text
        for row in range(len(level)):
            for col in range(len(level[row])):
                
                #general platforms used throughout the game
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
                elif level[row][col] == "mp":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+30, fill="white", outline="purple")
                    platforms.append(platform)
                    movingplatforms.append(platform)

                #celebratory blocks for reaching last level
                elif level[row][col] == "r":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="red", outline="red")
                    platforms.append(platform)
                elif level[row][col] == "o":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="orange", outline="orange")
                    platforms.append(platform)
                elif level[row][col] == "y":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="yellow", outline="yellow")
                    platforms.append(platform)
                elif level[row][col] == "g":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="green", outline="green")
                    platforms.append(platform)
                elif level[row][col] == "b":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="blue", outline="blue")
                    platforms.append(platform)
                elif level[row][col] == "i":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="indigo", outline="indigo")
                    platforms.append(platform)
                elif level[row][col] == "v":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="violet", outline="violet")
                    platforms.append(platform)

                elif level[row][col] == "f":
                    fire = get_fire_image()
                    image_garbage_collection_prevention.append(fire)
                    fire_image = canvas.create_image(col*80, row*80, image=fire, anchor="nw")
                    deathplatforms.append(fire_image)
                    
                
                #death platforms which will end the player's game if they touch them
                elif level[row][col] == "d":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="", outline="")
                    deathplatforms.append(platform)

                #winning platform which do the same thing as death platforms but produce a victory screen
                elif level[row][col] == "w":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="", outline="")
                    winplatforms.append(platform)
                
                #text placed at various points in the game 
                elif level[row][col] == "thisway":
                    canvas.create_text(col*80+40, row*80+40, text="This way ->", font=("Arial", 20), fill="white")
                elif level[row][col] == "blue":
                    canvas.create_text(col*80+40, row*80+40, text="Do you trust blue...", font=("Arial", 20), fill="white")
                elif level[row][col] == "red":
                    canvas.create_text(col*80+40, row*80+40, text="...or red?", font=("Arial", 20), fill="white")
                elif level[row][col] == "almost":
                    canvas.create_text(col*80+40, row*80+40, text="You're almost there...", font=("Arial", 20), fill="white")
                elif level[row][col] == "congrats":
                    canvas.create_text(col*80+40, row*80+40, text="Congratulations! You've beat the game!", font=("Arial", 20), fill="white")
                elif level[row][col] == "jump":
                    canvas.create_text(col*80+60, row*80+40, text="Jump down now to enter your name\ninto the leaderboard", font=("Arial", 20), fill="white")
                
                #score text
                elif level[row][col] == "sc":
                    score_text = canvas.create_text(col*80+60, row*80+40, text="Score: " + str(score), font=("Arial", 20), fill="white")
                
                #teleport object which tells the game to load the next level
                elif level[row][col] == "t":
                    platform = canvas.create_rectangle(col*80, row*80, col*80+80, row*80+80, fill="", outline="")
                    teleport_object = platform

        canvas.update()


    def key_press(event):
        global vertical_speed, horizontal_speed, key_left, key_right 
        global key_up, key_down, is_jumping, is_paused, gravity_cheat, score, bosskey, desktop_image
        if event.keysym == "a":
            key_left = True
        elif event.keysym == "d":
            key_right = True
        elif event.keysym == "w":
            key_up = True
            is_jumping = True
        elif event.keysym == "Escape":
            is_paused = not is_paused
        elif event.keysym == "g":
            gravity_cheat = not gravity_cheat
        elif event.keysym == "p":
            score += 1  
        elif event.keysym == "0":
            bosskey = not bosskey
            
                

    def key_release(event):
        global vertical_speed, horizontal_speed, key_left, key_right, key_up, key_down
        if event.keysym == "a":
            key_left = False
            
        elif event.keysym == "d":
            key_right = False
            
        elif event.keysym == "w":
            key_up = False

            
            

            
    def platform_collision():
        global player, platforms, movingplatforms, is_jumping
        player_box = canvas.bbox(player)

        for platform in platforms + movingplatforms:
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
    
    def win_collision():
        global player, winplatforms
        player_box = canvas.bbox(player)

        for platform in winplatforms:
            platform_box = canvas.bbox(platform)
            if (player_box[2] > platform_box[0] and player_box[0] < platform_box[2] and
                player_box[3] > platform_box[1] and player_box[1] < platform_box[3]):
                return True


        return False


    def determine_level():
        global levelnum, levelscompleted, score, movingplatforms

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
                score += 1
            elif not levelscompleted[4]:
                levelnum = 5
                levelscompleted[4] = True
                score += 1

    


    def restart_game():
        global window
        window.destroy()
        initialise_game()

    def store_score(name, score):
        scorefile = open("scores.txt", "a")
        scorefile.write(name + ": " + str(score) + "\n")
        scorefile.close()

    def get_bosskey_image():
        bosskey_image = Image.open("bosskey.png")
        bosskey_image = bosskey_image.resize((1280, 720), Image.ANTIALIAS)
        finalimage = ImageTk.PhotoImage(bosskey_image)
        image_garbage_collection_prevention.append(finalimage)
        return finalimage

    def game_loop():
        global vertical_speed, horizontal_speed, level, player, visual_level, levelnum, key_up, platforms, deathplatforms 
        global is_jumping, paused_text, movingplatforms, gravity_cheat, direction, score_text, score, bosskey, desktop_image

        if paused_text != None or desktop_image != None:
                if paused_text != None:
                    canvas.delete(paused_text)
                else:
                    canvas.delete(desktop_image)
        if is_paused or bosskey:
            if is_paused:
                paused_text = canvas.create_text(125, 75, text="Paused", font=("Arial", 30), fill="white")
            elif bosskey:
                desktop_image = canvas.create_image(0, 0, image=get_bosskey_image(), anchor="nw")
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
            elif levelnum == 5:
                canvas.delete("all")
                level = []
                platforms = []
                deathplatforms = []
                movingplatforms = []
                level = levels.get_level5()
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

            if gravity_cheat:
                vertical_speed += 0.3
            else:    
                vertical_speed += 0.8

            # if movingplatforms != []:
            #     for platform in movingplatforms:
            #         if canvas.coords(platform)[2] > 1280:
            #             canvas.move(platform, -5, 0)
            #         if canvas.coords(platform)[0] < 0:
            #             canvas.move(platform, 5, 0)

            if movingplatforms:
                platform = movingplatforms[0]
                coords = canvas.coords(platform)
                if coords[2] > 1120 and direction > 0:  # Change 1280 to the width of your canvas
                    direction = -1
                elif coords[0] < 110 and direction < 0:
                    direction = 1

                canvas.move(platform, 2 * direction, 0)

            # Check for a collision with a platform after applying gravity/ this collision works perfectly
            # canvas.move(player, 0, vertical_speed)
            # if platform_collision():
            #     canvas.move(player, 0, -vertical_speed)
            #     vertical_speed = 0

            # canvas.move(player, horizontal_speed, 0)
            # if platform_collision():
            #     canvas.move(player, -horizontal_speed, 0)

            #testing left/top border restriction
            canvas.move(player, 0, vertical_speed)
            if platform_collision() or canvas.coords(player)[1] < 0:  # check for top border
                canvas.move(player, 0, -vertical_speed)
                vertical_speed = 0

            canvas.move(player, horizontal_speed, 0)
            if platform_collision() or canvas.coords(player)[0] < 0:  # check for left border
                canvas.move(player, -horizontal_speed, 0)


            if death_collision():
                canvas.delete("all")
                canvas.create_text(640, 100, text="You died!", font=("Arial", 50), fill="red")
                canvas.create_text(640, 150, text="Score: " + str(score), font=("Arial", 30), fill="white")
                canvas.create_text(280, 175, text="Enter your name for the leaderboard:", font=("Arial", 20), fill="white")
                name_entry = Entry(window, font=("Arial", 15))
                name_entry.place(x=280, y=225, anchor="center")
                submit_button = Button(window, text="Submit", font=("Arial", 15), command=lambda: store_score(name_entry.get(), score))
                submit_button.place(x=280, y=275, anchor="center")

                canvas.create_text(1000, 175, text="Leaderboard:", font=("Arial", 20), fill="white")
                scorefile = open("scores.txt", "r")
                scores = scorefile.readlines()
                scorefile.close()
                for i in range(len(scores)):
                    canvas.create_text(1000, 225 + i*20, text=scores[i], font=("Arial", 15), fill="white")

                restart_button = Button(window, text="Restart", font=("Arial", 30), command=lambda: restart_game())
                restart_button.place(x=640, y=360, anchor="center")
                canvas.update()
            
            if win_collision():
                canvas.delete("all")
                canvas.create_text(640, 360, text="You won!", font=("Arial", 50), fill="green")
                canvas.create_text(640, 425, text="Score: " + str(score), font=("Arial", 30), fill="white")
                restart_button = Button(window, text="Restart", font=("Arial", 30), command=lambda: restart_game())
                restart_button.place(x=640, y=500, anchor="center")
                canvas.update()

            canvas.itemconfig(score_text, text="Score: " + str(score))

            canvas.update()
            canvas.after(10, game_loop)

    canvas.bind_all("<KeyPress>", key_press)
    canvas.bind_all("<KeyRelease>", key_release)

    game_loop()
    window.mainloop()

