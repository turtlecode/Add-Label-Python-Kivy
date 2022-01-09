import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        string = input("Enter :")
        lbl = Label(text = string,
                    font_size = "80 sp",
                    color = "#D9DC22")
        return lbl

label = MyLabelApp()
label.run()