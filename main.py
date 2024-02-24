#Astromania By Geordan Sfetsos
import pygame as p
from random import randint
import os
p.init()    
#imports and setups
astrod_image = p.image.load("img/astrod.png")
astrod_image = p.transform.scale(astrod_image, (50, 50))
star_image = p.image.load("img/star.png")
star_image = p.transform.scale(star_image, (50, 50))
player_image = p.image.load("img/player.png")
player_image = p.transform.scale(player_image, (40, 40))
win = p.display.set_mode((1000,600))
shoot = p.mixer.Sound(os.path.join("sounds", 'shoot.mp3'))
death = p.mixer.Sound(os.path.join("sounds", 'end.mp3'))
expload = p.mixer.Sound(os.path.join("sounds", 'explod.mp3'))
background_music = p.mixer.music.load(os.path.join("sounds", 'background.mp3'))
shoot.set_volume(0.5)
#sound and imagers
class player:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.y_speed = 0
    def update(self):
        self.y += self.y_speed
        self.y_speed = 0
        if self.y <= 0:
            self.y = 599-self.height
        if self.y >= 600-self.height:
            self.y = 1
        return self.x, self.y
    def up(self):
        self.y_speed -= 5
    def down(self):
        self.y_speed += 5
    def detect(self, x, y, width, height):
        if x <= self.x+self.width and x+width >= self.x:
            if y <= self.y+self.height and y+height >= self.y:
                return True
            else:
                return False
        else:
            return False
#player class
class astrod:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_speed = -3
    def update(self):
        self.x += self.x_speed
        return (self.x, self.y)
#astrod class
class star:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_speed = -3
    def update(self):
        self.x += self.x_speed
        return (self.x, self.y)
#star class
class bullet:
    def __init__(self, shotter_y, shotter_height, speed):
        self.speed = speed
        self.y = shotter_y-(shotter_height/2)+35
        self.x = 20
        self.width = 50
        self.height = 10
    def move(self):
        self.x += self.speed
        return p.Rect(self.x, self.y, self.width, self.height)
    def detect(self, x, y, width, height):
        if x <= self.x+self.width and x+width >= self.x:
            if y <= self.y+self.height and y+height >= self.y:
                return True
            else:
                return False
        else:
            return False
#bullet class
class button:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def update(self):
        return p.Rect(self.x, self.y, self.width, self.height)
    def detect(self, x, y, width, height):
        if x <= self.x+self.width and x+width >= self.x:
            if y <= self.y+self.height and y+height >= self.y:
                return True
            else:
                return False
        else:
            return False
#button class
def leng(main):
    counter = 0
    for i in main:
        counter += 1
    return counter
#length cal for debug
def megaroid(y):
    to_Re = []
    to_Re.append(astrod(1000, y-50, 50, 50))
    to_Re.append(astrod(1025, y-50, 50, 50))
    to_Re.append(astrod(1025, y-25, 50, 50))
    to_Re.append(astrod(1025, y-75, 50, 50))
    to_Re.append(astrod(1050, y-50, 50, 50))
    to_Re.append(astrod(1050, y, 50, 50))
    to_Re.append(astrod(1050, y-100, 50, 50))
    to_Re.append(astrod(1075, y-50, 50, 50))
    to_Re.append(astrod(1075, y-25, 50, 50))
    to_Re.append(astrod(1075, y-75, 50, 50))
    to_Re.append(astrod(1100, y-50, 50, 50))
    return to_Re
#megaroid
def main():
    run = True
    frames = 0
    player_ = player(20,20,40,40)
    astrods = []
    stars = []
    bullets = []
    astrods_holder = []
    stars_holder = []
    bullets_holder = []
    astrods_destroed = 0
    p.mixer.music.play(-1) 
    home_screen = True
    start_button = button(450, 400, 100, 50)
    high_score = 0
    full_auto = False
    full_auto_counter = 0
    full_auto_counter_time = 0
    level = 1
    #vars
    while run:
        if home_screen:
            if high_score < astrods_destroed:
                high_score = astrods_destroed
            #high score detector
            run = True
            frames = 0
            player_ = player(20,20,40,40)
            astrods = []
            stars = []
            bullets = []
            astrods_holder = []
            stars_holder = []
            bullets_holder = []
            astrods_destroed = 0
            home_screen = True
            start_button = button(450, 400, 100, 50)
            easy_button = button(300, 400, 100, 50)
            hard_button = button(600, 400, 100, 50)
            full_auto = False
            full_auto_counter = 0
            full_auto_counter_time = 0
            #reset vars
            p.time.Clock().tick(60)
            win.fill("black")
            #background and frame rate
            for i in p.event.get():
                if i.type == p.QUIT:
                    run = False
                if i.type == p.MOUSEBUTTONDOWN:
                    x = p.mouse.get_pos()[0]
                    y = p.mouse.get_pos()[1]
                    if start_button.detect(x,y,0,0):
                        home_screen = False
                    if easy_button.detect(x,y,0,0):
                        home_screen = False
                        level = 0
                    if hard_button.detect(x,y,0,0):
                        home_screen = False
                        level = 1
            #detect click and other input
            p.draw.rect(win,(0,0,0),start_button.update())
            p.draw.rect(win,(0,0,0),easy_button.update())
            font = p.font.Font("font.ttf",  30)
            txtsurf = font.render("Play", True, (255,255,255))
            win.blit(txtsurf,(450, 410))
            font = p.font.Font("font.ttf",  30)
            txtsurf = font.render("Easy", True, (255,255,255))
            win.blit(txtsurf,(300, 410))
            font = p.font.Font("font.ttf",  30)
            txtsurf = font.render("Hard", True, (255,255,255))
            win.blit(txtsurf,(600, 410))
            font = p.font.Font("font.ttf",  120)
            txtsurf = font.render("Astromania", True, (255,255,255))
            win.blit(txtsurf,(20, 50))
            font = p.font.Font("font.ttf",  60)
            txtsurf = font.render("High score: " + str(high_score), True, (255,255,255))
            win.blit(txtsurf,(200, 300))
            p.display.update()
            #rendering
        elif level == 0:
            frames += 1
            if frames == 10:
                frames = 0
                if randint(0,6) <= 1:
                    astrods.append(astrod(1000,randint(0,600-50),50,50))
                if randint(0, 20) == 1:
                    stars.append(star(1000, randint(0,600-50), 50, 50))
                if randint(0, 40) == 1:
                    astrods += megaroid(randint(0, 450))
            p.time.Clock().tick(60)
            #frame rate and star and astrod maker
            for i in p.event.get():
                if i.type == p.QUIT:
                    run = False
                if i.type == p.KEYDOWN:
                    if i.key == p.K_e:
                        bullets.append(bullet(player_.y, player_.height, 10))
                        p.mixer.Sound.play(shoot)
            #input
            keys = p.key.get_pressed()
            if keys[p.K_w]:
                player_.up()
            if keys[p.K_s]:
                player_.down()
            win.fill("black")
            #input and background color
            if full_auto:
                full_auto_counter += 1
                full_auto_counter_time += 1
                if full_auto_counter > 300:
                    full_auto = False
                    full_auto_counter_time = 0
                    full_auto_counter = 0
                else:
                    if full_auto_counter_time == 10:
                        bullets.append(bullet(player_.y, player_.height, 10))
                        p.mixer.Sound.play(shoot)
                        full_auto_counter_time = 0
            for i in astrods:
                for c in bullets:
                    if c.x > 1000:
                        bullets_holder = []
                        for v in bullets:
                            if v != c:
                                bullets_holder.append(v)
                        bullets = bullets_holder
                    if c.detect(i.x,i.y,i.width,i.height):
                        p.mixer.Sound.play(expload)
                        astrods_destroed += 1
                        astrods_holder = []
                        for f in astrods:
                            if f != i:
                                astrods_holder.append(f)
                        astrods = astrods_holder
                        bullets_holder = []
                        for v in bullets:
                            if v != c:
                                bullets_holder.append(v)
                        bullets = bullets_holder
                if player_.detect(i.x, i.y, i.width, i.height):
                    home_screen = True
                    p.mixer.Sound.play(death)
                win.blit(astrod_image, i.update())
                if i.x < -50:
                    astrods_holder = []
                    for b in astrods:
                        if b != i:
                            astrods_holder.append(b)
                    astrods = astrods_holder
            for i in stars:
                win.blit(star_image, i.update())
                if player_.detect(i.x, i.y, i.width, i.height):
                    full_auto = True
                    full_auto_counter -= 300
                    stars_holder = []
                    for v in stars:
                        if v != i:
                            stars_holder.append(v)
                    stars = stars_holder
                if i.x < 0-50:
                    stars_holder = []
                    for v in stars:
                        if v != i:
                            stars_holder.append(v)
                    stars = stars_holder
            for i in bullets:
                p.draw.rect(win,(255,255,255),i.move())
            win.blit(player_image, player_.update())
            font = p.font.Font("font.ttf",  30)
            txtsurf = font.render("Asteroids destroed: " + str(astrods_destroed), True, (255,255,255))
            win.blit(txtsurf,(200, 20))
            p.display.update()    
            #rendering and some logic 
        elif level == 1:
            frames += 1
            if frames == 10:
                frames = 0
                if randint(0,4) >= 1:
                    astrods.append(astrod(1000,randint(0,600-50),50,50))
                if randint(0, 20) == 1:
                    stars.append(star(1000, randint(0,600-50), 50, 50))
            p.time.Clock().tick(60)
            #frame rate and star and astrod maker
            for i in p.event.get():
                if i.type == p.QUIT:
                    run = False
                if i.type == p.KEYDOWN:
                    if i.key == p.K_e:
                        bullets.append(bullet(player_.y, player_.height, 10))
                        p.mixer.Sound.play(shoot)
            #input
            keys = p.key.get_pressed()
            if keys[p.K_w]:
                player_.up()
            if keys[p.K_s]:
                player_.down()
            win.fill("black")
            #input and background color
            if full_auto:
                full_auto_counter += 1
                full_auto_counter_time += 1
                if full_auto_counter > 300:
                    full_auto = False
                    full_auto_counter_time = 0
                    full_auto_counter = 0
                else:
                    if full_auto_counter_time == 10:
                        bullets.append(bullet(player_.y, player_.height, 10))
                        p.mixer.Sound.play(shoot)
                        full_auto_counter_time = 0
            for i in astrods:
                for c in bullets:
                    if c.x > 1000:
                        bullets_holder = []
                        for v in bullets:
                            if v != c:
                                bullets_holder.append(v)
                        bullets = bullets_holder
                    if c.detect(i.x,i.y,i.width,i.height):
                        p.mixer.Sound.play(expload)
                        astrods_destroed += 1
                        astrods_holder = []
                        for f in astrods:
                            if f != i:
                                astrods_holder.append(f)
                        astrods = astrods_holder
                        bullets_holder = []
                        for v in bullets:
                            if v != c:
                                bullets_holder.append(v)
                        bullets = bullets_holder
                if player_.detect(i.x, i.y, i.width, i.height):
                    home_screen = True
                    p.mixer.Sound.play(death)
                win.blit(astrod_image, i.update())
                if i.x < 0:
                    home_screen = True
                    p.mixer.Sound.play(death)
            for i in stars:
                win.blit(star_image, i.update())
                if player_.detect(i.x, i.y, i.width, i.height):
                    full_auto = True
                    full_auto_counter -= 300
                    stars_holder = []
                    for v in stars:
                        if v != i:
                            stars_holder.append(v)
                    stars = stars_holder
                if i.x < 0-50:
                    stars_holder = []
                    for v in stars:
                        if v != i:
                            stars_holder.append(v)
                    stars = stars_holder
            for i in bullets:
                p.draw.rect(win,(255,255,255),i.move())
            win.blit(player_image, player_.update())
            font = p.font.Font("font.ttf",  30)
            txtsurf = font.render("Asteroids destroed: " + str(astrods_destroed), True, (255,255,255))
            win.blit(txtsurf,(200, 20))
            p.display.update()    
            #rendering and some logic 
    p.quit()
main()
