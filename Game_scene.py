# Created by: Mr. Coxall
# Edited by: Tochi Kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
from numpy import random
from Game_level import*
from pause_scene import*
import time 
#from copy import deepcopy


paddle_speed = 30
min_ball_speed = 5 #10
max_ball_speed = 10 #18

# How much faster the ball gets when it hits a brick:
brick_speedup = 0.01 #0.15

class Brick (SpriteNode):
    def __init__(self, brick_type, *args, **kwargs):
       img = colors.get(brick_type, 'pzl:Red8')
       SpriteNode.__init__(self, img, *args, **kwargs)
       self.brick_type = brick_type



class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        #check
        self.paddle_target = self.size.x/2
        self.start_time = time.time()
        self.bricks = []
        
        self.fire_button_down = False
        self.Ball_move_speed = 20.0
        self.missiles = []
        self.Ball = []
        self.level = 0
        self.alien = []
        self.blocks = []
        self.shoot_ball = []
        self.alien_attack_rate = 1  
        self.alien_attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.dead = False
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/wall_background.png',
                                     position = background_position, 
                                     parent = self, 
                                     color = 'grey',
                                     size = self.size)
                                     
        paddle_position = Vector2()
        paddle_position.x = self.screen_center_x
        paddle_position.y = 100
        self.paddle_target = paddle_position.x
        self.paddle = SpriteNode('pzl:PaddleRed',
                                    parent = self,
                                    position = paddle_position,
                                    size = (120,25))
                                
        Ball_position = Vector2()
        Ball_position.x = self.screen_center_x
        Ball_position.y = 400
        self.Ball = SpriteNode('./assets/sprites/Ball.png',
                                 parent = self,
                                 position = Ball_position,
                                 color = 'white',
                                 size = (20,20))
                                       
        fire_button_position = Vector2()
        fire_button_position.x = self.size_of_screen_x - 100
        fire_button_position.y = 100
        self.fire_button = SpriteNode('./assets/sprites/red_button.png',
                                      parent = self,
                                      position = fire_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_size)
        self.score_position = Vector2()
        self.score_position.x = 500
        self.score_position.y = 720
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                    position = self.score_position)
        self.hearts_position = Vector2()
        self.hearts_position.x = 65
        self.hearts_position.y = 720
        self.hearts = [SpriteNode('plf:HudHeart_full',
                                      position = (30 + i * 45, 700),
                                      parent = self)
                                      for i in range (3)]
                                      
        self.pause_position = Vector2()
        self.pause_position.x = 935
        self.pause_position.y = 720 
        self.pause_button = SpriteNode('iow:pause_32',
                                       position = (self.pause_position),
                                       parent = self,
                                       size = (40,50))
                                  
                                  

        right_wall = Rect(self.size.w, 0, 100, self.size.h)
        left_wall = Rect(-100, 0, 100, self.size.h)
        top_wall = Rect(0, self.size.h-90, self.size.w, 100)
        self.walls = [SpriteNode(position=rect.center(), size=rect.size) for rect in (left_wall,
                      right_wall, top_wall)]
    def new_game(self):
      self.load_level(levels[self.level])
      self.level = 0
      
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.move_paddle() 
        self.bounce_ball()
        self.load_level(levels[self.level])
        
    def load_level(self, level_str):
       lines = level_str.splitlines()
       if self.size.w > 760:
         #iPad
         brick_w, brick_h = 64, 32
       else:
         #iPhone
         brick_w, brick_h = 32, 16
       min_x = 230 
       min_y = 500 
       for y, line in enumerate(reversed(lines)):
         for x, char in enumerate(line):
           if char == ' ': continue
           pos = Point(x * brick_w + min_x, min_y + y * brick_h)
           brick = Brick(char, position=pos, parent=self)
           brick.size = (brick_w, brick_h)
           self.bricks.append(brick)
			
    def move_paddle(self):
       new = self.paddle_target - self.paddle.position.x
       if abs(new) > paddle_speed:
         new = paddle_speed * cmp(new, 0)
       self.paddle.position += new, 0
       
       
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        x, y = touch.location
        self.bounce_ball()
        if self.fire_button.frame.contains_point(touch.location):
           self.create_new_ball()
           
        
        elif self.pause_button.frame.contains_point(touch.location):
              self.present_modal_scene(PauseScene())
        else:
            self.paddle_target = x
            
        
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        self.paddle_target = touch.location.x 
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        if self.pause_button.frame.contains_point(touch.location):
              self.present_modal_scene(PauseScene())
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def create_new_ball(self):
        # when the user hits the fire button
        
        
        
        shoot_ball_start_position = Vector2()
        shoot_ball_start_position.x = self.paddle.position.x
        shoot_ball_start_position.y = 100
        
        shoot_ball_end_position = Vector2()
        shoot_ball_end_position.x = shoot_ball_start_position.x
        shoot_ball_end_position.y = self.size_of_screen_y + 100
        
        
        self.shoot_ball.append(SpriteNode('./assets/sprites/shoot_ball.png',
                             position = shoot_ball_start_position,
                             size = (30,30),
                             parent = self))
        
        
          # make ball move forward
        ballShootAction = Action.move_to(shoot_ball_end_position.x, 
                                         shoot_ball_end_position.y + 100, 
                                         5.0)
        
        self.shoot_ball[len(self.shoot_ball)-1].run_action(ballShootAction)
       

    def bounce_ball(self):
    
        
        ball_end_position = Vector2()
        ball_end_position.x = self. screen_center_x
        ball_end_position.y = 100
        ball_speed = Vector2()
        ball_speed.x = 1 # how fast the ball moves in the x direction 
        ball_speed.y = 2 
        
         #border check
        if ball_end_position.y + 15 < 100 or ball_end_position.y + 15 > 660:
           ball_start_position.y *= -1
        if ball_end_position.x < 0 or ball_end_position.x > 960:
           ball_start_position.x *= -1
        
        ballBounceAction = Action.move_to(ball_end_position.x,
                                          ball_end_position.y + 15)
        self.Ball.run_action(ballBounceAction)
       
        
        ballnewposition = ball_end_position.x, ball_end_position.y + 10
    
