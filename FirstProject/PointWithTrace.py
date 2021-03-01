from manim import *
class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            updated_path = path.copy()
            updated_path.add_points_as_corners([dot.get_center()])
            path.become(updated_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=-PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()
