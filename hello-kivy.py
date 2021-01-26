import kivy
from kivy.app import App
from kivy.uix.label import Label

# Replace with your 
# Current version
kivy.require('1.11.1')

class MyFirstKivyApp(App):
    
    # Function that returns
    # rot widget
    def build(self):
        return Label(text ="Hello World !")


        # Label with text Hello world is returned
        # as a root widget


# Here our class is initialized
# and its run() method is called
# Initializes and starts
# our Kivy applications
MyFirstKivyApp().run()