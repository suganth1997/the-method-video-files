from cv2 import rectangle
from manim import *

class TheMethodIntro(Scene):
    def construct(self):

        the_method = Text("The Method").to_edge(UP)

        circle = Circle(1, stroke_width=DEFAULT_STROKE_WIDTH/2)

        circle_filled = Circle(1, stroke_width=DEFAULT_STROKE_WIDTH/2).set_fill(WHITE, opacity=0.5)

        circle_back = Circle(1, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # rectangle_line_1 = Line(LEFT+UP, LEFT+DOWN, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # rectangle_line_2 = Line(RIGHT+UP, RIGHT+DOWN, stroke_width=DEFAULT_STROKE_WIDTH/2)

        rectangle = Rectangle(width=2, stroke_width=DEFAULT_STROKE_WIDTH/2)

        rectangle_filled = Rectangle(width=2, stroke_width=DEFAULT_STROKE_WIDTH/2).set_fill(WHITE, opacity=0.5)

        rectangle_back = Rectangle(width=2, stroke_width=DEFAULT_STROKE_WIDTH/2)

        outer_rectangle = Rectangle(stroke_width=DEFAULT_STROKE_WIDTH/2)

        diameter = Line(LEFT, RIGHT, stroke_width=DEFAULT_STROKE_WIDTH/2)

        triangle_1 = Polygon(UP, LEFT, RIGHT, stroke_width=DEFAULT_STROKE_WIDTH/2)

        triangle_1_filled = Polygon(UP, LEFT, RIGHT, stroke_width=DEFAULT_STROKE_WIDTH/2).set_fill(WHITE, opacity=0.5)

        triangle_1_back = Polygon(UP, LEFT, RIGHT, stroke_width=DEFAULT_STROKE_WIDTH/2)

        triangle_2 = Polygon(UP, 2*LEFT + DOWN, 2*RIGHT + DOWN, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # cone_1 = Line(UP, 2*LEFT+DOWN, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # cone_2 = Line(UP, 2*RIGHT+DOWN, stroke_width=DEFAULT_STROKE_WIDTH/2)

        self.play(Write(the_method))

        self.play(Create(circle))

        self.play(Create(outer_rectangle))

        self.play(Create(rectangle))

        self.play(Create(diameter))

        self.play(Create(triangle_1), Create(triangle_2))

        self.play(ReplacementTransform(rectangle, rectangle_filled))

        self.play(ReplacementTransform(rectangle_filled, rectangle_back))

        self.play(ReplacementTransform(circle, circle_filled))

        self.play(ReplacementTransform(circle_filled, circle_back))

        self.play(ReplacementTransform(triangle_1, triangle_1_filled))

        self.play(ReplacementTransform(triangle_1_filled, triangle_1_back))

        self.wait(2)

        self.play(Uncreate(circle_back), Uncreate(outer_rectangle), Uncreate(rectangle_back), Uncreate(diameter), Uncreate(triangle_1_back), Uncreate(triangle_2))

        self.wait(2)

        