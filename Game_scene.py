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
#from copy import deepcopy


paddle_speed = 30
min_ball_speed = 5 #10
max_ball_speed = 10 #18

# How much faster the ball gets when it hits a brick:
brick_speedup = 0.01 #0.15

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
        
        
        self.fire_button_down = False
        self.Ball_move_speed = 20.0
        self.missiles = []
        self.Ball = []
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
        Ball_position.y = 200
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
        self.hearts = SpriteNode('plf:HudHeart_full',
                                      position = (self.hearts_position),
                                      parent = self)
                                      
        self.pause_position = Vector2()
        self.pause_position.x = 935
        self.pause_position.y = 720 
        self.pause_button = SpriteNode('iow:pause_32',
                                       position = (self.pause_position),
                                       parent = self,
                                       size = (40,50))
       
		#self.pause_button = SpriteNode('iow:pause_32', position=(32, self.size.h-32), parent=self)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.move_paddle() 
    
      			
    def move_paddle(self):
       new = self.paddle_target - self.paddle.position.x
       if abs(new) > paddle_speed:
         new = paddle_speed * cmp(new, 0)
       self.paddle.position += new, 0
       
       
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        x, y = touch.location
        if self.fire_button.frame.contains_point(touch.location):
            # only shoot if you are not dead
            if self.dead == False:
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
        
        if self.fire_button.frame.contains_point(touch.location):
            # only shoot if you are not dead
            if self.dead == False:
                self.create_new_ball()
        else:
            # if I removed my finger, then no matter what spaceship
            pass
        
            
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
        
        # make missile move forward
        ballMoveAction = Action.move_to(shoot_ball_end_position.x, 
                                           shoot_ball_end_position.y + 100, 
                                           5.0)
        self.shoot_ball[len(self.shoot_ball)-1].run_action(ballMoveAction)
        

