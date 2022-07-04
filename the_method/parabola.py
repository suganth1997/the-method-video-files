from math import cos, sin, sqrt, tan, atan, pi
from manim import *

class ParabolaPlot(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()

        axes = Axes(
            x_range=[-0.5, 0.5, 0.1],
            y_range=[0, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            # x_axis_config={
            #     "numbers_to_include": np.arange(-1, 1, 0.1),
            #     "numbers_with_elongated_ticks": np.arange(-1, 1, 0.5),
            # },
            tips=False,
        )
        # axes_labels = axes.get_axis_labels()

        parabola_graph = axes.get_graph(lambda x: 1 - 4*x**2, color=YELLOW, x_range=[-sqrt(1.0/4.0), sqrt(1.0/4.0), 0.01])
        line_parabola = axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/4.0), sqrt(1.0/4.0), 0.01])
        # area = axes.get_area(parabola_graph, [-sqrt(1.0/4.0), sqrt(1.0/4.0)], bounded=line_parabola)

        m = -2*4.0**2
        m_ = abs(tan(pi - atan(m)))
        c = m_ * 2 * sqrt(1.0/4.0)
        tangent_line = axes.get_graph(lambda x: m*x + c) # (sqrt(1.0/4.0), 0) --- (-sqrt(1.0/4.0), 2*(sqrt(1.0/4.0)*m)

        a = ValueTracker(4)

        parabola_graph.add_updater(lambda x: x.become(axes.get_graph(lambda x: 1 - a.get_value()*x**2, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))
        line_parabola.add_updater(lambda x: x.become(axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))
        
        # area.add_updater(lambda x: x.become(axes.get_area(parabola_graph, [-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value())], bounded=line_parabola)))

        # x_vals = np.linspace(-0.5, 0.5, 100)
        # y_vals = 5*(x_vals)**2 - 0.75

        # c_vals = x_vals + 1j * y_vals
        # c_vals = (cos(pi/4) + 1j * sin(pi/4)) * c_vals

        # x_vals = np.real(c_vals)
        # y_vals = np.imag(c_vals)

        # idx = x_vals > -1.0

        # x_vals = x_vals[idx]
        # y_vals = y_vals[idx]

        # graph = axes.get_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False)

        # cos_graph = axes.get_graph(lambda x: np.cos(x), color=RED)
        # self.add(axes)
        # self.play(Create(graph).set_run_time(4))

        self.play(Create(parabola_graph).set_run_time(4))
        self.play(Create(line_parabola).set_run_time(2))
        # self.play(Create(area).set_run_time(4))

        self.wait(4)
        self.play(self.camera.frame.animate.scale(2))

        self.play(a.animate(run_time=4).set_value(8.0))
        self.play(a.animate(run_time=4).set_value(2.0))
        self.play(a.animate(run_time=4).set_value(4.0))

        self.play(Create(tangent_line))
        self.wait(4)