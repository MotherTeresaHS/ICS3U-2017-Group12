# Created by: Mr. Coxall
# Edited by: Tochi Kazi
# Created on: Nov 2017
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
from Help_scene import*
from Game_scene import*
from settings_scene import*
from main_menu_scene import*





class SettingScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self,
                                     size = self.size)
        self.setting_text = LabelNode(font = ('Chalkduster',72),
                                      text = 'SETTINGS',
                                      color = 'black',
                                      position = (self.size.x /2,self.size.y * 0.90),
                                      parent = self)
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                     position = (150,100),
                                     parent = self)
        self.sound_button = SpriteNode('./assets/sprites/sound_button.png',
                                      parent = self,
                                      position = (300,400),
                                      alpha = 1)
        self.soundoff_button = SpriteNode('./assets/sprites/soundoff_button.png',
                                           parent = self,
                                           position = (300,300),
                                           alpha = 0)
                                           
        self.music_button = SpriteNode('./assets/sprites/music_button.png',
                                       parent = self,
                                       position = (600,400))
                                      
        self.musicoff_button = SpriteNode('./assets/sprites/musicoff_button.png',
                                              parent = self,
                                              position = (600,300),
                                              alpha = 0)
                                              
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        # after 2 seconds, move to main menu scene
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.sound_button.frame.contains_point(touch.location):
            self.sound_button.alpha = 0
            self.soundoff_button.alpha = 1
        elif self.music_button.frame.contains_point(touch.location):
            self.music_button.alpha = 0
            self.musicoff_button.alpha = 1
        elif self.musicoff_button.frame.contains_point(touch.location):
           self.musicoff_button.alpha = 0
           self.music_button.alpha = 1
        elif self.soundoff_button.frame.contains_point(touch.location):
           self.soundoff_button.alpha = 0
           self.sound_button.alpha = 1
           
           
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
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
