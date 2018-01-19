# Created by: Mr. Coxall
# Edited by;: Tochi kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui
from Help_scene import*
from Game_scene import*
from main_menu_scene import*


class PauseScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.brick_text = LabelNode(font = ('Chalkduster',72),
                                    text = 'PAUSED',
                                    color = 'black',
                                    position = (self.size.x /2,self.size.y * 0.90),
                                    parent = self)
                                    
                                      
        self.play_button_position = Vector2()
        self.play_button_position.x = 500
        self.play_button_position.y = 500
        self.play_button = SpriteNode('./assets/sprites/play_button.png',
                                       parent = self,
                                       position = self.play_button_position)
                                       
        self.quit_button = SpriteNode('./assets/sprites/quit_button.png',
                                       position = (500,200),
                                       parent = self)
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.play_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        elif self.quit_button.frame.contains_point(touch.location):
            self.present_modal_scene(MainMenuScene())






