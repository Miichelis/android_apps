import sys
from kivy.core.window import Window
from kivy.utils import platform
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
import time

sys.set_int_max_str_digits(10000000)
# APP SIZE

Builder.load_file("my.kv")


class MyLayout(Widget):

    def clear(self):
        self.ids.calculator_input.text = "0"

    def backspace(self):
        if self.ids.calculator_input.text[-1] != "e":
            prior = self.ids.calculator_input.text
            if prior[len(prior) - 2:len(prior)] == "/*" or prior[len(prior) - 2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior) - 2]
            else:
                if len(self.ids.calculator_input.text) == 1:
                    self.ids.calculator_input.text = "0"
                else:
                    self.ids.calculator_input.text = self.ids.calculator_input.text[0:len(self.ids.calculator_input.text) - 1]

    def percent(self):
        prior = self.ids.calculator_input.text
        if prior[-1] != "e":
            prior = self.ids.calculator_input.text
            if prior[len(prior) - 2:len(prior)] == "/*" or prior[len(prior) - 2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior) - 2]
            else:
                if not (prior[-1] in ["*", "-", "+", "+/-", "%", "/"] or prior[len(prior) - 2:len(prior)] == "**"):
                    self.ids.calculator_input.text = str(float(eval(self.ids.calculator_input.text))/100)

    def plus_minus(self):
        if self.ids.calculator_input.text[-1] != "e":
            prior = self.ids.calculator_input.text
            if prior[len(prior)-2:len(prior)] == "/*" or prior[len(prior)-2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior)-2]
            else:
                if self.ids.calculator_input.text[-1] not in ["*", "-", "+", "+/-", "%", "/", "**"]:
                    self.ids.calculator_input.text = str(float(self.ids.calculator_input.text)*(-1))

    def dot(self):
        if self.ids.calculator_input.text[-1] != "e":
            prior = self.ids.calculator_input.text
            if prior[len(prior)-2:len(prior)] == "/*" or prior[len(prior)-2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior)-2]
            else:
                def splitting(sign):
                    nums_list = prior.split(sign)
                    if sign in prior and "." not in nums_list[-1]:
                        self.ids.calculator_input.text += "."

                    elif "." not in self.ids.calculator_input.text:
                        self.ids.calculator_input.text += "."
                splitting("+")
                splitting("-")
                splitting("*")
                splitting("/")

    def number_press(self, num):
        prior = self.ids.calculator_input.text
        if prior[len(prior) - 2:len(prior)] == "/*" or prior[len(prior) - 2:len(prior)] == "*/":
            self.ids.calculator_input.text = prior[0:len(prior) - 2]
        else:
            if prior == "0" or prior == "Impossible":
                self.ids.calculator_input.text = str(num)
            else:
                self.ids.calculator_input.text += str(num)

    def actions(self, action):
        prior = self.ids.calculator_input.text
        if prior[-1] != "e":
            if prior[len(prior)-2:len(prior)] == "/*" or prior[len(prior)-2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior)-2]
            else:
                if prior[-1] in ["-", "+", "+/-", "%", "/"] or prior[len(prior)-2:len(prior)] == "**":
                    if not (prior[-1] == "/" and prior[-2] == "*"):
                        prior = self.ids.calculator_input.text[0:len(prior)-1] + action

                else:
                    prior += action

                self.ids.calculator_input.text = prior

    def equals(self):
        prior = self.ids.calculator_input.text
        if prior[-1] != "e":
            if prior[len(prior)-2:len(prior)] == "/*" or prior[len(prior)-2:len(prior)] == "*/":
                self.ids.calculator_input.text = prior[0:len(prior)-2]
            else:
                if prior[len(prior) - 2:len(prior)] == "**":
                    self.ids.calculator_input.text = str(eval(prior[0:len(prior) - 2]))

                elif prior[-1] in ["*", "-", "+", "+/-", "%", "/"]:
                    self.ids.calculator_input.text = str(eval(prior[0:len(prior)-1]))
                else:
                    try:
                        answer = eval(self.ids.calculator_input.text)

                        if answer == int(answer):
                            self.ids.calculator_input.text = str(int(answer))
                        else:
                            self.ids.calculator_input.text = str(answer)

                    except ZeroDivisionError:
                        self.ids.calculator_input.text = "Impossible"


class Calculator(App):
    def build(self):
        if platform == "android" or platform == "ios":
            Window.maximize()
        else:
            Window.size = (620, 1024)
        return MyLayout()


if __name__ == '__main__':
    app = Calculator()
    app.run()
