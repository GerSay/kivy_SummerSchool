import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


# Во время создания лейаута следует учитывать следующие аргументы:
#
# padding: Отступ padding между лейаутом и его дочерними элементами уточняется в
# пикселях. Для этого можно выбрать один из трех способов:
# Список из четырех аргументов: [padding_left, padding_top, padding_right,
# padding_bottom]
# Список из двух аргументов: [padding_horizontal, padding_vertical]
# Один аргумент: padding=10
# spacing: При помощи данного аргумента добавляется расстояние между дочерними
# виджетами.
# orientation: Позволяет изменить значение orientation для BoxLayout по
# умолчанию — с горизонтального на вертикальное.


class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i + 1),
                         size_hint=(.05, .05),
                         pos_hint={"center_x": .5, "center_y": .5},

                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
