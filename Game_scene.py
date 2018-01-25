# Created by: Mr. Coxall
# Edited by: Tochi Kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
from Game_level import*
from pause_scene import*
import time 
from Game_over_scene import *
from main_menu_scene import *
import sound



paddle_speed = 10
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
        if self.size.w > 760:
          #iPad
           brick_w, brick_h = 64, 32
        else:
          #iPhone
          brick_w, brick_h = 32, 16
        min_x = self.size.x - 1055
        min_y = self.size.y/2 * 0.70
        self.fire_button_down = False
        self.Ball_move_speed = 20.0
        self.Balls = []
        self.bricks = []
        self.level = 0
        self.shoot_ball = []
        self.time = 50
        self.dead = False
        self.started = False
        self.lives_left = 3
        
        
        
        # this will hold the speed and direction of the ball as an ordered pair
        self.ball_velocity = Vector2()
        self.ball_velocity.x = +5.0 #5.0
        self.ball_velocity.y = -5.0 #5.0
        
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
        paddle_position.y = self.size.y * 0.10
        self.paddle_target = paddle_position.x
        self.paddle = SpriteNode('pzl:PaddleRed',
                                    parent = self,
                                    position = paddle_position,
                                    scale = 1.00)
                                
        Ball_position = Vector2()
        Ball_position.x = self.screen_center_x
        Ball_position.y = self.size.y/4
        self.Ball = SpriteNode('pzl:BallBlue', #'./assets/sprites/Ball.png',
                              parent = self,
                              position = Ball_position,
                              color = 'white',
                              scale = 0.70)#0.07)
        fire_button_position = Vector2()
        fire_button_position.x = self.size.x * 0.90
        fire_button_position.y = self.size.y * 0.10
        self.fire_button = SpriteNode('./assets/sprites/red_button.png',
                                      parent = self,
                                      position = fire_button_position,
                                      alpha = 0.5,
                                      scale = 0.90)
        #self.time_position = Vector2()
        #self.time_position.x = self.size.x/2
        #self.time_position.y = self.size.y * 0.95
        #self.time_label = LabelNode(text = 'time: 50',
                                     #font=('Helvetica', 40),
                                    # parent = self,
                                    #position = self.time_position)
       # self.hearts_position = Vector2()
       # self.hearts_position.x = self.size.x * 0.10
        #self.hearts_position.y = self.size.y * 0.95
        #self.hearts = [SpriteNode('plf:HudHeart_full',
                                      #position = (30 + i * 45, 720),
                                     # parent = self)
                                     # for i in range (3)]
                                      
        #self.pause_position = Vector2()
        #self.pause_position.x = self.size.x * 0.90
        #self.pause_position.y = self.size.y * 0.95
        #self.pause_button = SpriteNode('iow:pause_32',
                                       #position = (self.pause_position),
                                       #parent = self,
                                       #scale = 1.50)
            
                                  
    def new_game(self):
      self.load_level(levels[self.level])
      self.ball_lost()
      #while self.time >= 0:
        #self.time = self.time - 1
        #self.time_label.text = 'time: ' + str(self.time)
        #time.sleep(1)
      #if self.time == 0:
         #print ('Blast off')

    def load_level(self, level_str):
       lines = level_str.splitlines()
       if self.size.w > 760:
         #iPad
         brick_w, brick_h = 64, 32
       else:
         #iPhone
         brick_w, brick_h = 32, 16
       min_x = self.size.x - 1055
       min_y = self.size.y/2 * 0.70
       for y, line in enumerate(reversed(lines)):
         for x, char in enumerate(line):
           if char == ' ': continue
           pos = Point(x * brick_w + min_x, min_y + y * brick_h)
           brick = Brick(char, position=pos, parent=self)
           brick.size = (brick_w, brick_h)
           self.bricks.append(brick)
       self.Balls.append(self.Ball)
    
   # def count_down(self):
     #  while self.time >= 0:
       #   self.time = self.time - 1
        #  self.time_label.text = 'time: ' + str(self.time)
       #   #time.sleep(1)
     #  if self.time == 0:
      #    print('stop')
    def update(self):
        # this method is called, hopefully, 60 times a second
        if config.gamescene == True:
          config.gamescene = False
          self.dismiss_modal_scene()
        self.move_paddle()
        if (self.started == False):
            self.load_level(levels[self.level])
            self.started = True
        # check every update to see if a ball has touched a brick
        else:
            pass
            
           #move the ball
        self.Ball.position = self.Ball.position + self.ball_velocity
        
        # now check if the ball has touched the paddle
        if self.Ball.frame.intersects(self.paddle.frame):
            # you should change the velocity to a different angle here
           self.ball_velocity.y = self.ball_velocity.y * (-1)
           if config.sound == True:
              sound.set_volume(50)
              sound.play_effect('8ve:8ve-tap-mellow')
           else :
              sound.set_volume(0)
              
        # bounce ball off walls
        if self.Ball.position.y <= 0:
            self.ball_velocity.y = self.ball_velocity.y * (0)
            self.present_modal_scene(GameOver())
        
         
            # really it should not bounce, the game should end
        if self.Ball.position.x <= 0:
            self.ball_velocity.x = self.ball_velocity.x * (-1)
        if self.Ball.position.x >= self.size_of_screen_x:
            self.ball_velocity.x = self.ball_velocity.x * (-1)
        if self.Ball.position.y >= self.size_of_screen_y:
            self.ball_velocity.y = self.ball_velocity.y * (-1)
        if self.size.w > 760:
         #iPad
         brick_w, brick_h = 64, 32
        else:
         #iPhone
         brick_w, brick_h = 32, 16
         
        if len(self.bricks) > 0 and len(self.shoot_ball) > 0:
            #print('missile check')
            for brick in self.bricks:
                for shoot in self.shoot_ball:
                    if brick.frame.contains_rect(shoot.frame):
                        shoot.remove_from_parent()
                        self.shoot_ball.remove(shoot)
                        brick.remove_from_parent()
                        self.bricks.remove(brick)
                        
        if len(self.bricks) > 0 and len(self.Balls) > 0:
          for brick in self.bricks:
              for self.Ball in self.Balls:
                  if brick.frame.contains_rect(self.Ball.frame):
                      brick.remove_from_parent()
                      self.bricks.remove(brick)
         
        if self.Ball.frame.intersects(brick.frame):
           #self.ball_velocity.y = self.ball_velocity.y * (-1)
           self.ball_velocity.y = self.ball_velocity.y * (-1)
			
    def move_paddle(self):
       new = self.paddle_target - self.paddle.position.x
       if abs(new) > paddle_speed:
         new = paddle_speed * cmp(new, 0)
       self.paddle.position += new, 0
       
       
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        x, y = touch.location
        if self.fire_button.frame.contains_point(touch.location):
           self.create_new_ball()
           if config.sound == True:
             sound.set_volume(50)
             sound.play_effect('8ve:8ve-beep-bop')
        #elif self.pause_button.frame.contains_point(touch.location):
              #self.present_modal_scene(PauseScene())
        else:
            self.paddle_target = x
            
        
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        self.paddle_target = touch.location.x 
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.fire_button.frame.contains_point(touch.location):
           self.create_new_ball()
        
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
        shoot_ball_start_position.y = self.paddle.position.y
        
        shoot_ball_end_position = Vector2()
        shoot_ball_end_position.x = shoot_ball_start_position.x
        shoot_ball_end_position.y = self.size_of_screen_y + 100
        
        
        self.shoot_ball.append(SpriteNode('./assets/sprites/shoot_ball.png',
                             position = shoot_ball_start_position,
                             scale = (0.20),
                             parent = self))
        
        
          # make ball move forward
        ballShootAction = Action.move_to(shoot_ball_end_position.x, 
                                         shoot_ball_end_position.y, 
                                         5.0)
        
        self.shoot_ball[len(self.shoot_ball)-1].run_action(ballShootAction)
       

    
