import kivy
kivy.require('1.7.2')
# Load Essential modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
# Set desired graphic settings


from kivy.config import Config
Config.set('graphics','resizable', 0)

# Graphics fix
Window.clearcolor = (0,0,0,1.)

# Step 3: Introduce your classes – .
# For this tutorial we’ll start with a simple class that draws some text on the screen . 
# Create a Label instance with the text ‘Your first Kivy App!’). #
# Specify the position of the label using information from the Window instance for
# automatic positioning. 
# Label contains a property called width, which lets you center the label without 
# knowing the actual length of the text.  
#
# Remember to use the parent.add_widget(child) function to add the label to the root widget.
# 
#this is the main widget that contains the game
class GUI(Widget):
	def __init__(self,**kwargs):
		super(GUI, self).__init__(**kwargs)
		
		l = Label(text='Not your first Kivy App!')
		l.x = Window.width	/ 2 - l.width/2
		l.y = Window.height / 2
		self.add_widget(l)

# Step 4: Define your application class. 
# It will contain a build function that sets up the elements of the app.
# Inside the build function you’ll want to create an object from a class with a canvas,
# so that subsequent images and text can be drawn on the screen. In our case we use the class GUI.
#Class GUI extends Widget, and therefore contains a canvas.

class ClientApp(App):
	def build(self):

		# where root widget goes here
		# should be canvas
		app = GUI()
		return app

if __name__ == '__main__':
	ClientApp().run()