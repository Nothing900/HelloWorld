from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
Config.set('graphics','resizable','0');



class Myapp(App):
        def build(self):
                return CodeInput(lexer=HtmlLexer())
                return Button(text="Hello!",
                              font_size=34,
                              on_press=self.btn_press,
                              background_color=[1,0,0,1])
        def btn_press(self,instance):
                print ("World!")
                instance.text="You are clicked me!"
                instance.background_color=[2.3,4,2,5]
                
        pass
if __name__=="__main__":
        Myapp().run()
