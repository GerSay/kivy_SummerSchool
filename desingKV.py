from kivy.app import App
from kivy.uix.button import Button


def on_press_button():
    print('Вы нажали на кнопку!')


class ButtonApp(App):
    def build(self):
        return Button()


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
