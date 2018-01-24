# Created by: Mr. Coxall
# Edited by;: Tochi kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui
from Help_scene import*

from main_menu_scene import *


class CreditScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'gold', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.brick_text = LabelNode(font = ('Chalkduster',72),
                                    text = 'CREDIT',
                                    color = 'white',
                                    position = (self.size.x /2,self.size.y * 0.90),
                                    parent = self)
                                    
                                    
        self.start_button = LabelNode(text = 'Designed by: Tochi kazi',
                                      font=('Chalkduster', 20),
                                      parent = self,
                                      position = self.size / 2,
                                      scale = 0.75)
                                      
        self.back_button_position = Vector2()
        self.back_button_position.x = self.size.x/2 - 350
        self.back_button_position.y = self.size.y/2 + 300
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = self.back_button_position)
                                       
        
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
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
