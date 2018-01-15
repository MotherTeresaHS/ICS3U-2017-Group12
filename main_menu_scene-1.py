# Created by: Mr. Coxall
# Edited by: Tochi Kazi
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from Help_scene import*
from Game_scene import*

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode('assets/sprites/brick_wall.png',
                                     position = self.size/2,
                                     parent = self,
                                     size = self.size)
                                    
        
        self.brick_text = LabelNode(font = ('Chalkduster',72),
                                    text = 'BRICK',
                                    color = 'gold',
                                    position = (self.size.x /2,self.size.y * 0.90),
                                    parent = self)
                                    
                                   	
        self.breaker_text = LabelNode(font = ('Chalkduster',72),
                                      text = 'DESTROYER',
                                      color = 'gold',
                                      position = (self.size.x/2, self.size.y * 0.80),
                                      parent = self)
        self.start_button = SpriteNode('assets/sprites/start.png',
                                      position = (self.size.x/2, self.size.y * 0.40),
                                      size = (300,120),
                                      parent = self)
                                      
        self.help_button = SpriteNode('assets/sprites/help.png',
                                          position = (self.size.x/2, self.size.y * 0.20),
                                          size = (300,120),
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
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        elif self.help_button.frame.contains_point(touch.location):
              self.present_modal_scene(HelpScene())
        
              
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
    