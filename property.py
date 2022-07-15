from kivy.app import App
from kivy.uix.button import Button


def on_press_button(instance):
    print('Вы нажали на кнопку!')


class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=on_press_button)

        return button


if __name__ == '__main__':
    app = MainApp()
    app.run()
