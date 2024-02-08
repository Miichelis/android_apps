import random
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

# APP SIZE
Window.size = (500, 700)

Builder.load_file("my.kv")


class MyLayout(Widget):
    global found
    found = False

    def clear(self):
        self.ids.calculator_input.text = "0"

    def number_press(self, num):
        num_before = self.ids.calculator_input.text

        if num_before == "0":
            self.ids.calculator_input.text = ""
            self.ids.calculator_input.text = str(num)
        else:
            self.ids.calculator_input.text += str(num)

    def actions(self, action):

        if self.ids.calculator_input.text[-1] not in ["+", "-", "%", "/", "+/-", "x"]:
            self.ids.calculator_input.text += action

        else:
            prev = self.ids.calculator_input.text
            next = ""
            for i in range(len(prev) - 1):
                next += prev[i]
                if i == len(prev) - 2:
                    next += action

            self.ids.calculator_input.text = next


        c = 0
        ar1 = ""
        ar2 = ""
        if self.ids.calculator_input.text[-1] == action:
            found = True

        if not found:
            ar1 += self.ids.calculator_input.text

        else:
            if c == 1:
                ar2 += self.ids.calculator_input.text
            c += 1

        print(ar1)

        if self.ids.calculator_input.text[-1] == "=":
            output = int(ar1) + int(ar2)
            self.ids.calculator_input.text = ""
            self.ids.calculator_input.text = str(output)


class Calculator(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    app = Calculator()
    app.run()
