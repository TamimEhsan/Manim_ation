from manim import *
from plotterForManin import *
class BisectionMethod(GraphScene,MovingCameraScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-10,
            x_max=10.3,
            num_graph_anchor_points=100,
            y_min=-20,
            y_max=20,
            graph_origin=ORIGIN,
            axes_color=GREEN,
            x_labeled_nums=range(-10, 10, 1),
            **kwargs
        )
        self.function_color = RED
        MovingCameraScene.setup(self)



    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph( self.func_to_graph , x_min = -10, x_max = 70)
        graph_label = self.get_graph_label(func_graph, label="\lgroup \\frac{x+5}{5} \\rgroup ^{3}-10")
        self.play(ShowCreation(func_graph))
        self.add(graph_label)
        [data,datal,datar] = find_Root_By_Bisection_Method(-8, 6, 20)
        dotl = Dot(self.coords_to_point(datal[0][0], datal[0][1]),color=YELLOW)
        dotr = Dot(self.coords_to_point(datar[0][0], datar[0][1]),color=YELLOW)
        dot = Dot(self.coords_to_point(data[0][0], data[0][1]), color=RED)
        self.add(dotl,dotr,dot)
        print(len(data))
        for i in range(len(data)):
            self.play(
                ApplyMethod(dotl.move_to, self.coords_to_point(datal[i][0], datal[i][1])),
                ApplyMethod(dotr.move_to, self.coords_to_point(datar[i][0], datar[i][1])),
            )
            self.play(ApplyMethod(dot.move_to,self.coords_to_point(data[i][0], data[i][1])))
            if i%3 == 2:
                self.play(
                    ApplyMethod(self.camera_frame.move_to, self.coords_to_point(data[i][0], data[i][1]))

                )
                self.play(ApplyMethod(self.camera_frame.scale, .7))
        self.wait(2)


    def func_to_graph(self, x):
        return ((0.3*(x+5))**3-10)

# manim manimation.py BisectionMethod -pql  // file name function name