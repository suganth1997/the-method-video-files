from typing_extensions import runtime
from manim import *

# class amp(Scene):
#     def construct(self):
#         A = ValueTracker(1)
#         graph = FunctionGraph(lambda x: np.arctan(A.get_value()* np.sin(x)))
#         graph.add_updater(lambda func : func.become(FunctionGraph(lambda x: np.arctan(A.get_value()* np.sin(x)))))
#         self.play(Write(graph))
#         self.play(A.animate.set_value(1000),run_time=10)

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.get_graph(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.get_graph(lambda x: np.cos(x), color=RED)
        
        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=RED,
        )

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph)
        labels = VGroup(axes_labels, sin_label)

        # b = 0.5
        # parabola_graph = axes.get_graph(lambda x: 0.5*np.exp(b*x) - 1, color=RED)

        # b = 0.25
        # parabola_graph_1 = axes.get_graph(lambda x: 0.5*np.exp(b*x) - 1, color=RED)

        # b = 0.4
        # parabola_graph_2 = axes.get_graph(lambda x: 0.5*np.exp(b*x) - 1, color=RED)

        # def test_func(x):
        #     x.become(axes.get_graph(lambda x: 0.5*np.exp(b.get_value()*x) - 1, color=RED))

        b = ValueTracker(0.25)
        
        parabola_graph = axes.get_graph(lambda x: 0.5*np.exp(b.get_value()*x) - 1, color=RED)
        parabola_graph.add_updater(lambda x: x.become(axes.get_graph(lambda x: 0.5*np.exp(b.get_value()*x) - 1, color=RED)))
        
        sin_label = axes.get_graph_label(
            parabola_graph, "\\frac{1}{2}e^{" + str(b.get_value()) + "x}-1", x_val=-10, direction=UP / 2
        )

        sin_label.add_updater(lambda x: x.become(axes.get_graph_label(
            parabola_graph, "\\frac{1}{2}e^{" + str(round(b.get_value(), 2)) + "x}-1", x_val=-10, direction=UP / 2
        )))

        self.play(FadeIn(axes))
        self.play(Create(parabola_graph).set_run_time(2.5))
        # self.play(parabola_graph)
        # self.add(axes, parabola_graph)
        self.play(Create(sin_label))
        # self.add(b)
        # b.add_updater(lambda x, dt: x.increment_value(0.01))
        # self.wait(2)
        # for dt in np.linspace(0, 0.25, 26):
        #     self.play(b.animate().increment_value(dt))
        self.play(b.animate(run_time=4).set_value(0.5))
        self.play(b.animate(run_time=4).set_value(0.1))
        # self.play(Transform(parabola_graph, parabola_graph_1).set_run_time(2.5))
        # self.play(Transform(parabola_graph, parabola_graph_2).set_run_time(2.5))