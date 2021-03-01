from manim import *
class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        circle.set_fill(PINK, opacity=0.5)
        square.set_fill(YELLOW, opacity=0.5)
        triangle.set_fill(RED, opacity=0.5)
        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)
        self.play(ShowCreation(circle))
        self.play(ShowCreation(square))
        self.play(ShowCreation(triangle))
        self.wait(1)
