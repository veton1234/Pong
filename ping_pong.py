from pygame import *
from random import randint

class Game(sprite.Sprite):
    def __init__(self,imazh,px,py,pw,ph,speed):
        super().__init__()
        self.image = transform.scale(image.load(imazh),(ph,pw))
        self.pw = pw
        self.ph = ph
        self.speed = speed
        
        self.rect = self.image.get_rect() 
        self.rect.x = px
        self.rect.y = py
   
    def reset(self):
        wind.blit(self.image,(self.rect.x, self.rect.y))


class Player(Game):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 600: 
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 600: 
            self.rect.y += self.speed
        

ww = 700
wh = 500
wind = display.set_mode((700,500))
back = transform.scale(image.load('back1.png'),(ww,wh))
p1 = Player('paddle.jpg', 30, 50, 100, 50, 5)
p2 = Player('paddle.jpg', 600, 50, 100, 50, 5)
ball = Game('ball.png',312, 250, 30, 30, 1)

font.init()
font = font.SysFont(None,35)
lose = font.render('Player 1 lost!',True,(180,0,0))
lose1 = font.render('Player 2 lost!',True,(180,0,0))

clock = time.Clock()
speedx = 3
speedy = 3
FPS = 60
score1 = 0
score2 = 0
maxscore = 5
gameover = False
finish = False
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:
        wind.blit(back,(0,0))
        text = font.render('Score: '+ str(score1),1,(255,255,255),None)
        wind.blit(text,(10,10))
        text1 = font.render('Score: '+ str(score2),1,(255,255,255),None)
        wind.blit(text1,(550,10))
        p1.update()
        p2.update1()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            speedx *= -1
            speedy *= 1

        if ball.rect.y > wh-50 or ball.rect.y < 0:
            speedy *= -1
        
        if ball.rect.x < 0:
            score2 += 1
            ball = Game('ball.png',312, 250, 30, 30, 1)

        if ball.rect.x > ww:
            score1 += 1
            ball = Game('ball.png',312, 250, 30, 30, 1)

        if score1 == maxscore:
            finish == True
            gameover = True
            wind.blit(lose1,(200,200))
            

        if score2 == maxscore:
            finish == True
            gameover = True
            wind.blit(lose,(200,200))
            
        p1.reset()
        p2.reset()
        ball.reset()
            

        

    display.update()
    clock.tick(FPS)