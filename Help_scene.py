# Created by: Mr. Coxall
# Edited by;: Tochi kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui
from credit_scene import*

from main_menu_scene import *


class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.tutorial_text = LabelNode(text = '- Use the red button which is the shoot button on the left to shoot balls continually form the bar',
                                      font=('Chalkduster', 20),
                                      parent = self,
                                      position = self.size / 2,
                                      scale = 0.75)
                                      
        self.brick_text = LabelNode(font = ('Chalkduster',72),
                                    text = 'HELP',
                                    color = 'white',
                                    position = (self.size.x /2,self.size.y * 0.90),
                                    parent = self)
                                    
        self.back_button_position = Vector2()
        self.back_button_position.x = 150
        self.back_button_position.y = 700
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = self.back_button_position)
        self.help_button_position = Vector2()
        self.help_button_position.x = 900
        self.help_button_position.y = 700
        self.credit_button = SpriteNode('./assets/sprites/credits_button.png',
                                         position = self.help_button_position,
                                         size = (100,100),
                                         parent = self)
                                         
                                       #size = (300,120))
                                       
        
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
        elif self.credit_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditScene())
    
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
    
