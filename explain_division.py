from re import U
from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan, exp, pi, log
from manim import *
from numpy import number

class ExplainDivision(MovingCameraScene):
    def construct(self):
        question_1 = Text('How many steps will it take to reach the solution?').scale(0.8)

        
        question_1.move_to(LEFT).to_edge(UP)

        sub_question = Tex('To reach a given accuracy, say').next_to(question_1, DOWN)
        e_5 = MathTex('10^{-5}').next_to(sub_question, RIGHT)

        sub_group = VGroup(sub_question, e_5).to_edge(LEFT)

        self.play(Write(question_1))

        self.play(Create(sub_group))

        self.wait(1.0)

        numberLine = NumberLine([-5, 5], color=BLUE, include_numbers=True)

        numberLine_1 = NumberLine([-5, 5], color=BLUE, include_numbers=True, number_scale_value=0.25, stroke_width=0.5)

        self.play(Create(numberLine))

        self.play(self.camera.frame.animate.scale(0.125).move_to([1.5, 0, 0]), Transform(numberLine, numberLine_1))

        l_1 = Line([1, 0, 0], [1.5, 0, 0], stroke_width=0.5, color=YELLOW)

        l_2 = Line([2, 0, 0], [1.5, 0, 0], stroke_width=0.5, color=YELLOW)

        self.play(Create(l_1), Create(l_2))
