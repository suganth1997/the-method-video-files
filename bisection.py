from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan, exp, pi, log
from manim import *

class Bisection(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
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

        self.play(Create(axes).set_run_time(4.0))

        sin_graph = axes.get_graph(lambda x : sin(2*x), stroke_width=1)

        self.play(Create(sin_graph).set_run_time(4.0))

        new_axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            axis_config={"color" : GREEN,  "number_scale_value" : 0.5, "stroke_width" : 1},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False
        )

        self.play(ReplacementTransform(axes, new_axes), self.camera.frame.animate.scale(0.25).move_to(axes.coords_to_point(2, 0)))

        zero_1 = Dot(axes.coords_to_point(0, 0), radius=0.01)
        zero_2 = Dot(axes.coords_to_point(pi/2, 0), radius=0.01)
        zero_3 = Dot(axes.coords_to_point(pi, 0), radius=0.01)

        self.play(Create(zero_1), Create(zero_2), Create(zero_3))

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

        self.play(ReplacementTransform(new_axes, new_new_axes), self.camera.frame.animate.scale(0.5).move_to(axes.coords_to_point(1.5, 0)))

        line_1 = Line(axes.coords_to_point(1, -0.25), axes.coords_to_point(1, 0.25), stroke_width = 0.5).set_color(YELLOW)
        line_2 = Line(axes.coords_to_point(2, -0.25), axes.coords_to_point(2, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(Create(line_1), Create(line_2))

        mid_line = Line(axes.coords_to_point(1.5, -0.25), axes.coords_to_point(1.5, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(ReplacementTransform(line_1, mid_line), ReplacementTransform(line_2, mid_line))

        line_2 = Line(axes.coords_to_point(2, -0.25), axes.coords_to_point(2, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(Create(line_2))

        # line_3 = Line(axes.coords_to_point(2, -0.25), axes.coords_to_point(2, 0.25), stroke_width = 0.5).set_color(YELLOW)

        # self.play(Create(line_3))

        mid_line_1 = Line(axes.coords_to_point(1.75, -0.25), axes.coords_to_point(1.75, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(ReplacementTransform(line_2, mid_line_1), ReplacementTransform(mid_line, mid_line_1))

        mid_line = Line(axes.coords_to_point(1.5, -0.25), axes.coords_to_point(1.5, 0.25), stroke_width = 0.5).set_color(YELLOW)
        
        self.play(Create(mid_line))

        mid_line_2 = Line(axes.coords_to_point(1.625, -0.25), axes.coords_to_point(1.625, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(ReplacementTransform(mid_line, mid_line_2), ReplacementTransform(mid_line_1, mid_line_2))

        mid_line = Line(axes.coords_to_point(1.5, -0.25), axes.coords_to_point(1.5, 0.25), stroke_width = 0.5).set_color(YELLOW)
        
        self.play(Create(mid_line))

        mid_line_3 = Line(axes.coords_to_point(1.5675, -0.25), axes.coords_to_point(1.5675, 0.25), stroke_width = 0.5).set_color(YELLOW)

        self.play(ReplacementTransform(mid_line, mid_line_3), ReplacementTransform(mid_line_2, mid_line_3))

        self.play(self.camera.frame.animate.scale(4.0).move_to(axes.coords_to_point(0, 0)), Uncreate(mid_line_3))

        self.play(Uncreate(sin_graph), Uncreate(zero_1), Uncreate(zero_2), Uncreate(zero_3))


        