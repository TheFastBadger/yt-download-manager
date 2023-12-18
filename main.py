import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import manager

class InputGrid(GridLayout):
    def __init__(self, **kwargs):
        super(InputGrid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Url:"))

        self.url = TextInput(multiline=False)
        self.add_widget(self.url)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        url = self.url.text

        if "watch?v" in url:
            manager.download_video(url, 22)
        elif "playlist?list" in url:
            manager.download_playlist(url, 22)
class ManagerApp(App):
    def build(self):
        return InputGrid()


if __name__ == "__main__":
    ManagerApp().run()
