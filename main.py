from kivy.app import App
from kivy.uix.widget import Widget

class ChickenGame(Widget):
    pass


class ChickenApp(App):
    def build(self):
        return ChickenGame()
    



if __name__ == '__main__':
    ChickenApp().run()
