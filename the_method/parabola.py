from math import cos, sin, sqrt, tan, atan, pi
from click import style
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

        # f = lambda x: 1 - 4*x**2

        a = ValueTracker(4)

        f = lambda x: 1 - a.get_value()*x**2

        parabola_graph = axes.get_graph(lambda x: 1 - a.get_value()*x**2, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])
        line_parabola = axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])
        # area = axes.get_area(parabola_graph, [-sqrt(1.0/4.0), sqrt(1.0/4.0)], bounded=line_parabola)

        m = -2*a.get_value()*sqrt(1.0/a.get_value())
        m_ = abs(m)
        c = m_ * sqrt(1.0/4.0)

        def tangent(x):
            m = -2*a.get_value()*sqrt(1.0/a.get_value())
            m_ = abs(m)
            c = m_ * sqrt(1.0/a.get_value())

            return m*x + c, c

        tangent_line = axes.get_graph(lambda x: tangent(x)[0], x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01], color=YELLOW) # (sqrt(1.0/4.0), 0) --- (-sqrt(1.0/4.0), 2*(sqrt(1.0/4.0)*m)

        left_vertex_axis = axes.get_line_graph([-sqrt(1.0/a.get_value()), -sqrt(1.0/a.get_value())], [0.0, 2*tangent(0)[1]], add_vertex_dots=False)

        mid_axis = axes.get_line_graph([0.0, 0.0], [0.0, tangent(0)[1]], add_vertex_dots=False)

        A_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/4.0), 0]))

        A_text = Text('A').next_to(A_dot, (DOWN + LEFT)/2)

        B_dot = Dot(axes.coords_to_point(*[0, 1]))

        B_text = Text('B').next_to(B_dot, (UP + RIGHT)/2)

        C_dot = Dot(axes.coords_to_point(*[sqrt(1.0/4.0), 0]))

        C_text = Text('C').next_to(C_dot, (DOWN + RIGHT)/2)

        D_dot = Dot(axes.coords_to_point(*[0, 0]))

        D_text = Text('D').next_to(D_dot, DOWN)

        E_dot = Dot(axes.coords_to_point(*[0, 2 * f(0)]))

        E_text = Text('E').next_to(E_dot, (UP + RIGHT)/2)

        F_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/4.0), 4 * f(0)]))

        F_text = Text('F').next_to(F_dot, (UP + RIGHT)/2)


        b = ValueTracker(0.25)

        any_line_prl_axis = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False)

        O_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0]))

        O_text = Text('O').next_to(O_dot, DOWN)

        M_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]]))

        M_text = Text('M').next_to(M_dot, (UP + RIGHT)/2)

        P_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))

        P_text = Text('P').next_to(P_dot, (DOWN + RIGHT)/2)

        parabola_graph.add_updater(lambda x: x.become(axes.get_graph(lambda x: 1 - a.get_value()*x**2, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))
        line_parabola.add_updater(lambda x: x.become(axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))
        
        any_line_prl_axis.add_updater(lambda x: x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False)))

        O_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0]))))

        O_text.add_updater(lambda x: x.become(Text('O').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0])), DOWN)))

        M_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]]))))

        M_text.add_updater(lambda x: x.become(Text('M').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]])), (UP + RIGHT)/2)))

        P_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))))

        P_text.add_updater(lambda x: x.become(Text('P').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))])), (DOWN + RIGHT)/2)))

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

        self.play(Create(parabola_graph).set_run_time(2))
        self.play(Create(line_parabola).set_run_time(2))
        # self.play(Create(area).set_run_time(4))

        # self.wait(4)
        # self.play(self.camera.frame.animate.scale(2))

        # self.play(a.animate(run_time=4).set_value(8.0))
        # self.play(a.animate(run_time=4).set_value(2.0))
        # self.play(a.animate(run_time=4).set_value(4.0))

        self.play(self.camera.frame.animate.scale(3).move_to([0, 5, 0]))
        self.play(Create(tangent_line))
        self.play(Create(left_vertex_axis))
        self.play(Create(mid_axis))
        self.play(Create(any_line_prl_axis))

        self.play(Create(A_dot), Create(A_text), Create(C_dot), Create(C_text), Create(B_dot), Create(B_text), Create(D_dot), Create(D_text), Create(E_dot), Create(E_text), Create(F_dot), Create(F_text), Create(O_dot), Create(O_text), Create(M_dot), Create(M_text), Create(P_dot), Create(P_text))

        self.play(b.animate(run_time=4).set_value(0.75))

        self.play(b.animate(run_time=4).set_value(0.25))

        self.wait(4)