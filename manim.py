# Import manim library
from manim import *

class SceneName(Scene):
    """
    By convention, the structure of your animation
    is defined in the construct method, but later
    we will learn how to do it in different ways.
    """
    def construct(self):
        # Create a text using Text class
        text = Text("Hello world")

        # Text animation
        self.play(Write(text))

        # Pause
        self.wait()
