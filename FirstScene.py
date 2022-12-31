from manim import *

#Set the output of the video to
#100% of the width of the screen.
config.media_width = "100%"

class FirstScene(Scene):
    def construct(self):
        text = Text("Hello world")
        self.play(Write(text))
        self.wait()
