from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window
import random
import math

Window.size = (530, 700)


egg_types = ['Egg.png', 'Egg2.png', 'Egg3.png', 'Egg4.png', 'Egg5.png']

egg_count = 0

lives = 3

speed_ratio = 0.1

game_over = False

update_clock = None


## sound is a work in progress because it doesn't work I think lmao
sound = SoundLoader.load('clucky.mp3')
class Chicken(Widget):
    def on_touch_down(self, touch):
        if (not game_over) and self.collide_point(*touch.pos):
            #make the chicken play a sound
            if sound:
                sound.play()


class Egg(Widget):
    def on_touch_down(self, touch):
        if (not game_over) and self.collide_point(*touch.pos):
            if(abs(self.dx - touch.pos[0]) < 50 and
               Window.height - 100 - abs(self.pos[1]) - touch.pos[1] < 50):
                self.parent.remove_widget(self)
                global egg_count
                egg_count+= 1

    def get_egg(self):
 
        return egg_types[random.randint(0,4)]

    
    def get_rand_x(self):
        self.dx = random.randint(0, Window.width)
        return self.dx
    
    def update(self):
        global game_over
        if not game_over:
            self.pos[1] -= 5*(1 + egg_count*speed_ratio)
        if self.pos[1] < -(Window.height) + 100:
            global lives
            lives -= 1
            self.parent.remove_widget(self)
 
class ScoreLabel(Label):
    pass
 
class LifeLabel(Label):
    pass

class ChickenGame(RelativeLayout):
    chicken = ObjectProperty(None)
    egg = ObjectProperty(None)
 
    def update(self, dt):
      global game_over
      global lives
      self.ids.life_label.text = str(lives)
      self.ids.score_label.text = str(egg_count)
      if lives <= 0:
        game_over = True
        update_clock.cancel()
      if not game_over:
          for child in App.get_running_app().root.children[:]:
              try:
                  child.update()
              except:
                  pass
          if random.randint(0,20) == 3:
              App.get_running_app().root.add_widget(Egg())
    
class ChickenApp(App):
    def build(self):
        global game
        game = ChickenGame()
        global update_clock
        update_clock = Clock.schedule_interval(game.update, 0.03)
        return game
 
if __name__ == '__main__':
    ChickenApp().run()
