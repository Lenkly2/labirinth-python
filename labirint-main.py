from pygame import *
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height


        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))


        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x = self.rect.x - self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8) or sprite.collide_rect(player,wall9) or sprite.collide_rect(player,wall10) or sprite.collide_rect(player,wall11) or sprite.collide_rect(player,walllock) or sprite.collide_rect(player,walllock2):
                self.rect.x = self.rect.x + self.speed
        if keys[K_d] and self.rect.x < 950:
            self.rect.x = self.rect.x + self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8) or sprite.collide_rect(player,wall9) or sprite.collide_rect(player,wall10) or sprite.collide_rect(player,wall11) or sprite.collide_rect(player,walllock) or sprite.collide_rect(player,walllock2):
                self.rect.x = self.rect.x - self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8) or sprite.collide_rect(player,wall9) or sprite.collide_rect(player,wall10) or sprite.collide_rect(player,wall11) or sprite.collide_rect(player,walllock) or sprite.collide_rect(player,walllock2):
                self.rect.y = self.rect.y + self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y = self.rect.y + self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6) or sprite.collide_rect(player,wall7) or sprite.collide_rect(player,wall8) or sprite.collide_rect(player,wall9) or sprite.collide_rect(player,wall10) or sprite.collide_rect(player,wall11) or sprite.collide_rect(player,walllock) or sprite.collide_rect(player,walllock2):
                self.rect.y = self.rect.y - self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)
        
        
    direction = 'left'
    def move2(self):
        if self.rect.x == 150:
            self.direction = 'right'
        elif self.rect.x == 600:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
    def move3(self):
        if self.rect.y == 50:
            self.direction = 'right'
        elif self.rect.y == 500:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.y += self.speed
        if self.direction == 'left':
            self.rect.y -= self.speed
    def move4(self):
        if self.rect.x == 150:
            self.direction = 'right'
        elif self.rect.x == 800:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
    def move5(self):
        if self.rect.x == 250:
            self.direction = 'right'
        elif self.rect.x == 550:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
bullets = sprite.Group()

class Bullet(Object):
    def update(self): #функція пострілу праворуч
        self.rect.x += 10
        if self.rect.x > 1000:
            self.kill()

window = display.set_mode((1000,600))
picture = transform.scale(image.load('background.jpg'),(1000,600))
player = Object('hero.png',100,400,50,50,5)
enemy = Object('cyborg.png',150,50,150,150,5)
enemy2 = Object('cyborg.png',815,50,150,150,5)
enemy3 = Object('cyborg.png',200,450,150,150,5)
gover = Object('gover.png',0,0,1000,600,0)
gwin = Object('win.png',0,0,1000,600,0)
gold = Object('fgold.png',950,450,50,50,0)
Key = Object('key.png',750,100,50,50,0)
Key2 = Object('key.png',750,250,50,50,0)
Key3 = Object('key.png',750,250,50,50,0)
heart1 = transform.scale(image.load('heart.png'),(50,50))
heart2 = transform.scale(image.load('heart.png'),(50,50))
heart3 = transform.scale(image.load('heart.png'),(50,50))
nxlevel = transform.scale(image.load('nlvv.jpg'),(200,100))
restart = transform.scale(image.load('restart.png'),(200,100))
wall = Wall(255,0,0,150,0,25,200)
wall2 = Wall(255,0,0,150,0,800,25)
wall3 = Wall(255,0,0,950,0,25,400)
wall4 = Wall(255,0,0,150,575,800,25)
wall5 = Wall(255,0,0,350,200,25,250)
wall6 = Wall(255,0,0,350,425,250,25)
wall7 = Wall(255,0,0,490,200,340,25)
wall8 = Wall(255,0,0,710,200,25,225)
wall9 = Wall(255,0,0,805,0,25,200)
wall10 = Wall(255,0,0,150,400,25,200)
wall11 = Wall(255,0,0,150,200,200,25)
walllock = Wall(255,255,0,1950,400,25,200)
walllock2 = Wall(255,255,0,1600,225,25,225)
health = 3
level = 1
death = 0
boss_definded = 0
clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_e:
                player.fire()
    if level == 1:
        window.blit(picture,(0,0))
        player.reset()
        player.move()
        enemy.reset()
        enemy2.reset()
        enemy3.reset()
        enemy.move2()
        enemy2.move3()
        enemy3.move4()
        Key.reset()
        Key2.reset()
        bullets.update()
        bullets.draw(window)
        wall.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()

        walllock.draw_wall()
        walllock2.draw_wall()
        if sprite.collide_rect(player,Key2):
            walllock2.rect.x = 1200
            Key2.rect.x = 1200
        if sprite.collide_rect(player,Key):
            walllock.rect.x = 1200
            Key.rect.x = 1200



            
        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,enemy2) or sprite.collide_rect(player,enemy3):
            death = 1

        if death == 1:
            player.speed = 0
            if player.speed == 0:
                gover.reset()
            window.blit(restart,(0,0))

            if restart.get_rect().collidepoint(mouse.get_pos()):
                player.rect.x = 100
                player.rect.y = 400
                death = 0
                player.speed = 5
                Key.rect.x = 750
                Key2.rect.x = 750
                walllock.rect.x = 950
                walllock2.rect.x = 550
                enemy.direction = 'right'
                player.reset()
                

        if sprite.collide_rect(player,gold):
            player.speed = 0
            if player.speed == 0:
                gwin.reset()
            
            window.blit(nxlevel,(0,0))
            if nxlevel.get_rect().collidepoint(mouse.get_pos()):
                player.speed = 5
                player.rect.x = 100
                player.rect.y = 400
                enemy3.direction = "right"
                Key.rect.x = 750
                Key2.rect.x = 300
                Key2.rect.y = 75
                enemy3.rect.y = 50
                enemy2.rect.y = 450
                walllock.rect.x = 950
                walllock2 = Wall(255,255,0,700,200,100,25)
                enemy2.rect.x -= 150
                enemy.rect.x -= 75

                level = 2
    if level == 2:
        window.blit(picture,(0,0))
        player.reset()
        player.move()
        wall = Wall(255,0,0,50,0,25,200)
        wall2 = Wall(255,0,0,50,0,900,25)
        wall4 = Wall(255,0,0,50,575,900,25)
        wall7 = Wall(255,0,0,400,200,300,25)
        wall8 = Wall(255,0,0,675,0,25,200)
        wall10 = Wall(255,0,0,50,400,25,200)
        gold.rect.y = 100
        wall3.rect.y = 200
        wall11.rect.x = 1200
        walllock.rect.y = 0
    
        Key.rect.y = 75
        wall5 = Wall(255,0,0,250,0,25,450)
        wall9 = Wall(255,0,0,800,0,25,450) 
        wall6 = Wall(255,0,0,400,200,25,250)
        enemy.reset()
        enemy2.reset()
        enemy3.reset()
        enemy.move3()
        enemy2.move3()
        enemy3.move5()
        Key.reset()
        Key2.reset()
        bullets.update()
        bullets.draw(window)
        wall.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()



        walllock.draw_wall()
        walllock2.draw_wall()
        if sprite.collide_rect(player,Key2):
            walllock2.rect.x = 1200
            Key2.rect.x = 1200
        if sprite.collide_rect(player,Key):
            walllock.rect.x = 1200
            Key.rect.x = 1200



            
        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,enemy2) or sprite.collide_rect(player,enemy3):
            death = 1

        if death == 1:
            player.speed = 0
            if player.speed == 0:
                gover.reset()
            window.blit(restart,(0,0))

            if restart.get_rect().collidepoint(mouse.get_pos()):
                player.rect.x = 100
                player.rect.y = 400
                death = 0
                player.speed = 5
                Key.rect.x = 750
                Key2.rect.x = 750
                walllock.rect.x = 950
                walllock2.rect.x = 550
                enemy.direction = 'right'
                player.reset()
                

        if sprite.collide_rect(player,gold):
            player.speed = 0
            if player.speed == 0:
                gwin.reset()
            
            window.blit(nxlevel,(0,0))
            if nxlevel.get_rect().collidepoint(mouse.get_pos()):
                player.speed = 5
                player.rect.x = 100
                player.rect.y = 400
                level = 3
    if level == 3:
        window.blit(picture,(0,0))
        player.reset()
        player.move()
        enemy2.reset()
        if health ==3:
            window.blit(heart1,(25,50))
            window.blit(heart2,(50,50))
            window.blit(heart3,(75,50))
        if health ==2:
            window.blit(heart1,(25,50))
            window.blit(heart2,(50,50))
        if health ==1:
            window.blit(heart1,(25,50))

        wall.rect.x = 1000
        wall2.rect.x = 1000
        wall3.rect.x = 1000
        wall4.rect.x = 1000
        wall5.rect.x = 1000
        wall6.rect.x = 1000
        wall7.rect.x = 1000
        wall8.rect.x = 1000
        wall9.rect.x = 1000
        wall10.rect.x = 1000
        wall11.rect.x = 1000
        walllock.rect.x = 1000
        walllock2.rect.x = 1000
        Key.rect.x = 1000

        bullets.update()
        bullets.draw(window)

        if sprite.collide_rect(player,enemy2):
            health -= 1
            if health > 0:
                player.rect.x -= 30
            if health <= 0:
                player.speed = 0
                gover.reset()
                window.blit(restart,(0,0))
                if restart.get_rect().collidepoint(mouse.get_pos()):
                    player.speed = 5
                    player.rect.x = 100
                    player.rect.y = 400
                    player.reset()
                    health = 3

            
            if boss_definded == 1: 
                
                player.speed = 0
                if player.speed == 0:
                    gwin.reset()
                    
                window.blit(nxlevel,(0,0))
                if nxlevel.get_rect().collidepoint(mouse.get_pos()):
                    player.speed = 5
                    level = 3
                    player.rect.x = 100
                    player.rect.y = 400

    display.update()
    clock.tick(60)