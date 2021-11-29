from typing_extensions import runtime
from jedi.inference.context import ValueContext
from manim import *
from numpy import angle
from math import sin, cos

import pickle
from numpy.core.defchararray import center

with open("Cn.dat", "rb") as fp:
    Cn = pickle.load(fp)

class PointMovingOnShapes(Scene):
    def construct(self):
        master_angle = ValueTracker(0)
        
        # lengths = np.array([3, 2, 1, 2])/2
        # phis = np.array([0, 0, 0, 0])

        lengths = [np.abs(2*x) for _, x in Cn]
        phis = [angle(x) for _, x in Cn]

        n_ind = [i for i, _ in Cn]

        rel_origin_main = [ORIGIN]
        def get_lines_and_circles():
            lines = []
            circles = []

            rel_origin = ORIGIN
            for n, l, phi in zip(n_ind, lengths, phis):
                circles.append(Circle(radius = l, stroke_opacity = 0.5, stroke_width = DEFAULT_STROKE_WIDTH/2).move_to(rel_origin))
                master_angle_value = n * master_angle.get_value()
                right = rel_origin + [l*cos(master_angle_value + phi), l*sin(master_angle_value + phi), 0]
                lines.append(Line(rel_origin, right, stroke_opacity = 0.5, stroke_width = DEFAULT_STROKE_WIDTH/2))
                rel_origin = right

            rel_origin_main[0] = rel_origin

            return lines + circles

        full_group = VGroup(*get_lines_and_circles())
        self.add(full_group)

        full_group.add_updater(lambda x: x.become(VGroup(*get_lines_and_circles())))

        trace = TracedPath(lambda : rel_origin_main[0])
        self.add(trace)
        self.play(master_angle.animate(run_time = 8).set_value(2*PI - 0.0001))

        self.wait(2)

        # dot = Dot()
        # dot2 = dot.copy().shift(RIGHT)
        # dot_1 = Dot()
        # self.add(dot, dot_1)

        # line = Line([3, 0, 0], [5, 0, 0])
        # line_1 = Line([0, 0, 0], [-3, 0, 0])

        # circle_1 = Arc(radius=3, angle = TAU / 2, color=BLUE).shift(3*LEFT)
        # self.add(line, line_1, circle_1)

        # self.play(GrowFromCenter(circle))
        # self.play(Transform(dot, dot2))
        # self.play(MoveAlongPath(dot, circle), MoveAlongPath(circle, circle_1), MoveAlongPath(dot_1, circle_1), run_time=2, rate_func=linear)
        # self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        # self.wait()
