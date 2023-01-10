from manim import *

class MoreAnimations(Scene):
    def construct(self):
        text = Text("Hello world")
        self.play(Write(text))
        self.wait()
        self.play(Rotate(text,PI/2))
        self.wait()
        self.play(Indicate(text))
        self.wait()
        self.play(FocusOn(text))
        self.wait()
        self.play(ShowCreationThenDestructionAround(text))
        self.wait()
        self.play(FadeOut(text))
        self.wait()
