# Created by: Mr. Coxall
# Created by: Tochi Kazi
# Created on: Nov 2017
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time
from main_menu_scene import *
from Game_scene import *
import config


class GameOver(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add game logo background 
        self.game_logo = SpriteNode('./assets/sprites/brick_wall.png',
                                       parent = self,
                                       position = self.size/2,
                                       size = self.size)
        
        self.game_over_text = LabelNode(font = ('Chalkduster',72),
                                    text = 'GAME_OVER',
                                    color = 'white',
                                    position = (self.size.x/2,self.size.y * 0.90),
                                    parent = self)
        self.home_button = SpriteNode('./assets/sprites/home_button.png',
                                      parent = self,
                                      position = (self.size.x/2 , self.size.y/4),
                                      scale = 2.00)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        # after 2 seconds, move to main menu scene
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        if self.home_button.frame.contains_point(touch.location):
            config.gamescene = True
            self.dismiss_modal_scene()
    
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
    
