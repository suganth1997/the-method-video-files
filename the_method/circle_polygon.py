from math import sqrt, tan, cos
from manim import *

from numpy import poly

class PiWithPolygon(MovingCameraScene):
    def construct(self):

        r = 2

        n = 15

        circle = Circle(r)

        inside_polygon = []

        outside_polygon = []

        for i in range(4, n):
            inside_polygon.append(RegularPolygon(i, radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2))
            outside_polygon.append(RegularPolygon(i, radius=r/cos(PI/i), stroke_width=DEFAULT_STROKE_WIDTH/2))

        # inside_polygon = RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # outside_polygon = RegularPolygon(int(n.get_value()), radius=r/cos(PI/n.get_value()), stroke_width=DEFAULT_STROKE_WIDTH/2)

        # inside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)))

        # outside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r/cos(PI/int(n.get_value())), stroke_width=DEFAULT_STROKE_WIDTH/2)))
        
        self.play(Create(circle))

        self.play(Create(inside_polygon[0]))

        self.play(Create(outside_polygon[0]))

        # self.play(n.animate.set_value(10), run_time=4)

        for i in range(n - 5):
            self.play(ReplacementTransform(inside_polygon[i], inside_polygon[i + 1]), ReplacementTransform(outside_polygon[i], outside_polygon[i + 1]))

        self.wait(4)
