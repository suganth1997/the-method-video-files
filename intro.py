from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan
from manim import *

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        name = Text("Zero of a function")
        self.play(Write(name).set_run_time(2.5))
        name_1 = Text("Zero of a function").move_to([0, 2, 0])
        self.play(ReplacementTransform(name, name_1))
        fx0 = MathTex("f(x)=0")
        self.play(Write(fx0.next_to(name, DOWN)).set_run_time(2.5))

        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).move_to([0, -1, 0])

        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        ).move_to([0, -1, 0])

        self.play(Create(l0))
        self.wait(2)

        parabola = lambda x, c, a : (-1.0/c)*(a*x**2 - 2)
        parabola_der = lambda x, c, a : (-2.0/c)*a*x
        parabola_zero = lambda a : sqrt(2.0/a)
        format_number = lambda x : "{:.4s}".format('{:0.4f}'.format(x))
        xValTrack = ValueTracker(0)

        fx00 = MathTex("f(" + format_number(xValTrack.get_value()) + ")=" + format_number(parabola(xValTrack.get_value(), 2.0, 1.0))).move_to([xValTrack.get_value(), 0, 0])

        # fx0.add_updater(lambda x: x.become(MathTex("f(" + str(xValTrack.get_value()) + ")=1").move_to([xValTrack.get_value(), 0, 0])))
        fx00.add_updater(lambda x: x.become(MathTex("f(" + format_number(xValTrack.get_value()) + ")=" + format_number(parabola(xValTrack.get_value(), 2.0, 1.0))).move_to([xValTrack.get_value(), 0, 0])))
        self.play(ReplacementTransform(fx0, fx00))
        # self.play(Transform(fx00, fx00.move_to([2, 0, 0])))
        # self.play(Create(fx00))

        self.play(xValTrack.animate(run_time=4).set_value(2.0))
        self.wait(2)
        self.play(xValTrack.animate(run_time=4).set_value(-2.0))
        self.wait(2)
        self.play(xValTrack.animate(run_time=4).set_value(sqrt(2.0)))
        self.wait(2)

        # fx001 = MathTex("f(" + format_number(xValTrack.get_value()) + ")=" + format_number(parabola(xValTrack.get_value()))).move_to([4, 3, 0])

        a = ValueTracker(1.0)
        b = ValueTracker(2.0)

        fx001 = MathTex("f(x)=\\frac{1}{" + format_number(b.get_value()) + "}(2-" + format_number(a.get_value()) + "x^2)").move_to([4, 3, 0])

        fx001.add_updater(lambda x : x.become(MathTex("f(x)=\\frac{1}{" + format_number(b.get_value()) + "}(2-" + format_number(a.get_value()) + "x^2)").move_to([4, 3, 0])))

        name_2 = name.copy().move_to([-4, 3, 0])

        self.play(ReplacementTransform(l0, axes), ReplacementTransform(fx00, fx001), Transform(name_1, name_2))

        parabola_graph = axes.get_graph(lambda x: parabola(x, b.get_value(), a.get_value()), color=BLUE, x_range=[-10, 10])
        parabola_graph.add_updater(lambda x : x.become(axes.get_graph(lambda x: parabola(x, b.get_value(), a.get_value()), color=BLUE, x_range=[-10, 10])))

        # point_on_curve = Dot([parabola(sqrt(2)), 0, 0])
        print(axes.coords_to_point(sqrt(2)))
        point_on_curve = Dot(axes.coords_to_point(parabola_zero(a.get_value())))
        point_on_curve_ = Dot(axes.coords_to_point(-parabola_zero(a.get_value())))

        point_on_curve.add_updater(lambda x : x.become(Dot(axes.coords_to_point(parabola_zero(a.get_value())))))
        point_on_curve_.add_updater(lambda x : x.become(Dot(axes.coords_to_point(-parabola_zero(a.get_value())))))
        # point_on_curve = axes.get_point_mobject([parabola(sqrt(2)), 0, 0])

        # point_on_curve.scale_in_place(10)

        # vgroup = VGroup(parabola_graph, point_on_curve)

        self.play(Create(parabola_graph).set_run_time(1.0))
        self.play(Create(point_on_curve), Create(point_on_curve_))
        self.play(b.animate(run_time=2.0).set_value(0.8))
        self.wait(2)
        self.play(b.animate(run_time=2.0).set_value(2.0))
        self.wait(2)
        # self.play(a.animate(run_time=2.0).set_value(4.0))
        self.play(a.animate(run_time=2.0).set_value(0.25))
        self.wait(2)
        self.play(a.animate(run_time=2.0).set_value(0.35))
        self.wait(2)

        x0 = 6.0
        x1 = x0 - parabola(x0, b.get_value(), a.get_value())/parabola_der(x0, b.get_value(), a.get_value())
        tangent_line = axes.get_line_graph([x0, x1], [parabola(x0, b.get_value(), a.get_value()), 0.0], vertex_dot_radius=0.01)
        self.play(Create(tangent_line))
        self.play(Create(axes.get_line_graph([x1, x1], [0.0, parabola(x1, b.get_value(), a.get_value())], vertex_dot_radius=0.01)))

        self.wait(1.5)

        x0 = x1
        x1 = x0 - parabola(x0, b.get_value(), a.get_value())/parabola_der(x0, b.get_value(), a.get_value())
        tangent_line = axes.get_line_graph([x0, x1], [parabola(x0, b.get_value(), a.get_value()), 0.0], vertex_dot_radius=0.01)
        self.play(Create(tangent_line))
        self.play(Create(axes.get_line_graph([x1, x1], [0.0, parabola(x1, b.get_value(), a.get_value())], vertex_dot_radius=0.01)))

        self.wait(3.0)

        x0 = -1.0
        x1 = x0 - parabola(x0, b.get_value(), a.get_value())/parabola_der(x0, b.get_value(), a.get_value())
        tangent_line = axes.get_line_graph([x0, x1], [parabola(x0, b.get_value(), a.get_value()), 0.0], vertex_dot_radius=0.01)
        self.play(Create(tangent_line))
        self.play(Create(axes.get_line_graph([x1, x1], [0.0, parabola(x1, b.get_value(), a.get_value())], vertex_dot_radius=0.01)))

        self.wait(1.5)

        x0 = x1
        x1 = x0 - parabola(x0, b.get_value(), a.get_value())/parabola_der(x0, b.get_value(), a.get_value())
        tangent_line = axes.get_line_graph([x0, x1], [parabola(x0, b.get_value(), a.get_value()), 0.0], vertex_dot_radius=0.01)
        self.play(Create(tangent_line))
        self.play(Create(axes.get_line_graph([x1, x1], [0.0, parabola(x1, b.get_value(), a.get_value())], vertex_dot_radius=0.01)))
        self.wait(3.0)
        # self.play(Transform(fx00, fx001))