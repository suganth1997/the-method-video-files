from re import U
from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan, exp, pi, log
from manim import *
from numpy import number

class HowManySteps(MovingCameraScene):
    def construct(self):
        question = Text('How many steps will it take to reach the solution?').scale(0.8)
        self.play(Write(question))

        question_1 = Text('How many steps will it take to reach the solution?').scale(0.8)
        question_1.move_to(LEFT).to_edge(UP)
        self.play(Transform(question, question_1))
        

        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            axis_config={"color": GREEN}, # "number_scale_value":0.5
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False
        )

        self.play(Create(axes).set_run_time(1.0))

        a = ValueTracker(0.1)

        ex_graph = axes.get_graph(lambda x : exp(-x) - a.get_value(), stroke_width=1)

        ex_group = VGroup(ex_graph, Dot(axes.coords_to_point(-log(a.get_value()), 0), radius=0.015))

        ex_group.add_updater(lambda x : x.become(VGroup(axes.get_graph(lambda x : exp(-x) - a.get_value(), stroke_width=1), Dot(axes.coords_to_point(-log(a.get_value()), 0), radius=0.015))))

        new_new_axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            axis_config={"color" : GREEN,  "number_scale_value" : 0.25, "stroke_width" : 0.25},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 1),
                # "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False
        )
        
        self.play(ReplacementTransform(axes, new_new_axes), Create(ex_group), self.camera.frame.animate.scale(0.3).move_to(axes.coords_to_point(1.5, 0)))

        self.play(a.animate(run_time=2.0).set_value(0.4))

        def PlotBisection(f, A, B, n_steps):
            
            A = 1
            B = 2

            if f(A) < 0:
                A, B = B, A    
        
            line_1 = Line(axes.coords_to_point(A, -0.25), axes.coords_to_point(A, 0.25), stroke_width = 0.5).set_color(YELLOW)
            line_2 = Line(axes.coords_to_point(B, -0.25), axes.coords_to_point(B, 0.25), stroke_width = 0.5).set_color(YELLOW)

            self.play(Create(line_1), Create(line_2))

            for i in range(n_steps):
                C = (A + B)/2

                mid_line = Line(axes.coords_to_point(C, -0.25), axes.coords_to_point(C, 0.25), stroke_width = 0.5).set_color(YELLOW)

                self.play(Create(mid_line))

                if f(C) > 0:
                    A = C
                    self.play(ReplacementTransform(line_1, mid_line))
                    line_1 = mid_line

                else:
                    B = C
                    self.play(ReplacementTransform(line_2, mid_line))
                    line_2 = mid_line

            return line_1, line_2, mid_line

        self.play(a.animate(run_time=2.0).set_value(exp(-1.56)))

        ########################################################################################################################################

        f = lambda x : exp(-x) - a.get_value()

        line_1, line_2, mid_line = PlotBisection(f, 1, 2, 4)

        self.play(Uncreate(line_1), Uncreate(line_2))

        self.play(a.animate(run_time=1.0).set_value(exp(-1.23)))

        line_1, line_2, mid_line = PlotBisection(f, 1, 2, 4)

        self.play(Uncreate(line_1), Uncreate(line_2), Uncreate(ex_group))


        a.set_value(1.0)

        ex_graph = new_new_axes.get_graph(lambda x : x**2 - a.get_value(), stroke_width=1)

        ex_group = VGroup(ex_graph, Dot(new_new_axes.coords_to_point(-log(a.get_value()), 0), radius=0.015))

        ex_group.add_updater(lambda x : x.become(VGroup(new_new_axes.get_graph(lambda x : x**2 - a.get_value(), stroke_width=1), Dot(new_new_axes.coords_to_point(sqrt(a.get_value()), 0), radius=0.015))))

        # self.play(Create(ex_graph))

        self.play(Create(ex_group))

        self.play(a.animate(run_time=1.0).set_value(1.34**2))

        f = lambda x : x**2 - a.get_value()

        line_1, line_2, mid_line = PlotBisection(f, 1, 2, 4)

        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            axis_config={"color": GREEN}, # "number_scale_value":0.5
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False
        )

        self.play(Uncreate(line_1), Uncreate(line_2), Uncreate(ex_group), Uncreate(new_new_axes), self.camera.frame.animate.scale(1.0/0.3).move_to(axes.coords_to_point(0, 0)))

        # question = Text('How many steps will it take to reach the solution?').scale(0.5)

        sub_question = Tex('To reach a given accuracy, say').next_to(question_1, DOWN)
        e_5 = MathTex('10^{-5}').next_to(sub_question, RIGHT)

        sub_group = VGroup(sub_question, e_5).to_edge(LEFT)

        self.play(Create(sub_group))

        self.wait(1.0)

        numberLine = NumberLine([-5, 5], color=BLUE, include_numbers=True)

        self.play(Create(numberLine))
        
        # mid_line = Line(axes.coords_to_point(1.25, -0.25), axes.coords_to_point(1.25, 0.25), stroke_width = 0.5).set_color(YELLOW)

        # self.play(Create(mid_line))

        # self.play(ReplacementTransform(line_2, mid_line))

        # line_2 = mid_line

        # mid_line = Line(axes.coords_to_point(1.125, -0.25), axes.coords_to_point(1.125, 0.25), stroke_width = 0.5).set_color(YELLOW)

        # self.play(Create(mid_line))

        # self.play(ReplacementTransform(line_1, mid_line))

        




