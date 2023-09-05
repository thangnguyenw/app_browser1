import os
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

Builder.load_file('layout.kv')


# class MyFunctions:
#     os.system()hàm để thực thi lệnh python samples.py.
#     @staticmethod
#     def samples(self):
#         filename = 'samples.py'
#         os.system('python ' + filename)

#     @staticmethod
#     def testcode(self):
#         filename = 'thucode.py'
#         os.system('python ' + filename)

#     @staticmethod
#     def delete(self):
#         filename = 'delete.py'
#         os.system('python ' + filename)


class MyGridLayout(Widget):
    # text = ObjectProperty(None)

    def press(self, button_text):
        print('hello', button_text)

    def show_popup(self, button_text):
        print(button_text)
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text=button_text))
        content.add_widget(Button(text='Close Popup', on_press=self.dismiss_popup))
        self.popup = Popup(title='My Popup', content=content, size_hint=(None, None), size=(200, 200))
        self.popup.open()

    def dismiss_popup(self, instance):
        self.popup.dismiss()


class MyApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
