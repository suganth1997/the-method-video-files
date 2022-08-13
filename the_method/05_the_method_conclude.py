from math import sqrt
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

        b = ValueTracker(0.25)

        f = lambda x: 1 - a.get_value()*x**2

        def tangent(x):
            m = -2*a.get_value()*sqrt(1.0/a.get_value())
            m_ = abs(m)
            c = m_ * sqrt(1.0/a.get_value())

            return m*x + c, c, m
        
        def HKC(x):
            m = -2*a.get_value()*sqrt(1.0/a.get_value())
            m_ = abs(m)
            c = m_ * sqrt(1.0/a.get_value())

            return (m/2)*x + (c/2)

        parabola_graph = axes.get_graph(lambda x: 1 - a.get_value()*x**2, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])
        line_parabola = axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])
        tangent_line = axes.get_graph(lambda x: tangent(x)[0], color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])
        
        area = axes.get_area(parabola_graph, [-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value())], bounded=line_parabola, dx_scaling=10)

        area_triangle = axes.get_area(tangent_line, [-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value())], bounded=line_parabola, dx_scaling=10)

        area_balanced = axes.get_area(parabola_graph, [-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value())], bounded=line_parabola, dx_scaling=10).move_to(axes.coords_to_point(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value())), 0.0]))

        m = -2*a.get_value()*sqrt(1.0/a.get_value())
        m_ = abs(m)
        c = m_ * sqrt(1.0/4.0)

        

        tangent_line = axes.get_graph(lambda x: tangent(x)[0], x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01], color=YELLOW) # (sqrt(1.0/4.0), 0) --- (-sqrt(1.0/4.0), 2*(sqrt(1.0/4.0)*m)

        left_vertex_axis = axes.get_line_graph([-sqrt(1.0/a.get_value()), -sqrt(1.0/a.get_value())], [0.0, 2*tangent(0)[1]], add_vertex_dots=False)

        mid_axis = axes.get_line_graph([0.0, 0.0], [0.0, tangent(0)[1]], add_vertex_dots=False)

        AB_line = axes.get_line_graph([-sqrt(1.0/a.get_value()), 0.0], [0.0, f(0.0)], add_vertex_dots=False)

        BC_line = axes.get_line_graph([0.0, sqrt(1.0/a.get_value())], [f(0.0), 0.0], add_vertex_dots=False)

        BK_line = axes.get_line_graph([-sqrt(1.0/a.get_value()), 0.0], [tangent(0)[1], f(0.0)], add_vertex_dots=False)

        HK_line = axes.get_line_graph([-sqrt(1.0/a.get_value()), -3*sqrt(1.0/a.get_value())], [HKC(-sqrt(1.0/a.get_value())), HKC(-3*sqrt(1.0/a.get_value()))], add_vertex_dots=False)

        # TG_line_ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)

        TG_line = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)

        PO_line = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)
        
        PO_line_ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)
        
        PO_line__ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)

        MO_line = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)

        MO_line_ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)

        # MO_line__ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)

        CA_line = axes.get_line_graph([-sqrt(1.0/4.0), sqrt(1.0/4.0)], [0.0, 0.0], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)
        
        AO_line = axes.get_line_graph([-sqrt(1.0/4.0), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, 0.0], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)

        CK_line = axes.get_line_graph([-sqrt(1.0/4.0), sqrt(1.0/4.0)], [2 * f(0), 0.0], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)
        
        KN_line = axes.get_line_graph([-sqrt(1.0/4.0), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [2 * f(0), (-2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1])/2], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)
        
        HK_line_ = axes.get_line_graph([-sqrt(1.0/4.0), -3*sqrt(1.0/a.get_value())], [2 * f(0), HKC(-3*sqrt(1.0/a.get_value()))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)

        
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

        K_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/4.0), 2 * f(0)]))

        K_text = Text('K').next_to(K_dot, (UP + LEFT)/2)

        H_dot = Dot(axes.coords_to_point(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value()))]))

        H_text = Text('H').next_to(H_dot, (UP + LEFT)/2)

        


        any_line_prl_axis = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False)

        O_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0]))

        O_text = Text('O').next_to(O_dot, DOWN)

        M_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]]))

        M_text = Text('M').next_to(M_dot, (UP + RIGHT)/2)

        N_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), (-2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1])/2]))

        N_text = Text('N').next_to(N_dot, (LEFT + DOWN)/2)

        P_dot = Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))

        P_text = Text('P').next_to(P_dot, (DOWN + RIGHT)/2)

        parabola_graph.add_updater(lambda x: x.become(axes.get_graph(lambda x: 1 - a.get_value()*x**2, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))

        line_parabola.add_updater(lambda x: x.become(axes.get_graph(lambda x: 0, color=YELLOW, x_range=[-sqrt(1.0/a.get_value()), sqrt(1.0/a.get_value()), 0.01])))
        
        any_line_prl_axis.add_updater(lambda x: x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False)))

        O_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0]))))

        O_text.add_updater(lambda x: x.become(Text('O').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), 0.0])), DOWN)))

        M_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]]))))

        M_text.add_updater(lambda x: x.become(Text('M').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]])), (UP + RIGHT)/2)))

        N_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), (-2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1])/2]))))

        N_text.add_updater(lambda x: x.become(Text('N').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), (-2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1])/2])), (UP + RIGHT)/2)))

        P_dot.add_updater(lambda x: x.become(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))))

        P_text.add_updater(lambda x: x.become(Text('P').next_to(Dot(axes.coords_to_point(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))])), (DOWN + RIGHT)/2)))

        TG_line.add_updater(lambda x: x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2).move_to(axes.coords_to_point(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value())), 0.0]))))

        PO_line.add_updater(lambda x: x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2)))

        MO_line.add_updater(lambda x: x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2)))

        # parabola_diagram_group = VGroup()

        quadrature_text = Text("Quadrature of Parabola", font_size = 80).shift(20*LEFT + 15*UP)
        
        the_method_text = Text("The Method", font_size = 80).shift(25*LEFT + 15*UP)

        MO_PO_text = MathTex("\\frac{MO}{PO} = ", font_size = 58).shift(22*LEFT + 8*UP)

        CA_AO_text = MathTex("\\frac{CA}{AO}", font_size = 58).next_to(MO_PO_text, RIGHT)

        CK_KN_text = MathTex("\\frac{CK}{KN}", font_size = 58).next_to(MO_PO_text, RIGHT)
        
        HK_KN_text = MathTex("\\frac{HK}{KN}", font_size = 58).next_to(MO_PO_text, RIGHT).shift(4*DOWN)

        ratio_relation = VGroup(MO_PO_text, CK_KN_text)
        
        fulcrum_lever_text = MathTex("MO\\times KN = OP\\times HK", font_size = 58).next_to(MO_PO_text, 4*DOWN)

        area_fulcrum_text_final = MathTex("\\text{Area of Parabola} = \\frac{1}{3}\\text{Area of Triangle}", font_size = 58).next_to(fulcrum_lever_text, 4*DOWN)

        self.play(Write(the_method_text), Create(parabola_graph), Create(line_parabola), self.camera.frame.animate.scale(3).move_to([-8, 6, 0]), Create(tangent_line), Create(left_vertex_axis), Create(mid_axis), Create(any_line_prl_axis), Create(AB_line), Create(BC_line), Create(BK_line), Create(A_dot), Create(A_text), Create(C_dot), Create(C_text), Create(B_dot), Create(B_text), Create(D_dot), Create(D_text), Create(E_dot), Create(E_text), Create(F_dot), Create(F_text), Create(O_dot), Create(O_text), Create(M_dot), Create(M_text), Create(P_dot), Create(P_text), Create(N_dot), Create(N_text), Create(K_dot), Create(K_text), Create(HK_line), Create(H_dot), Create(H_text))

        self.play(b.animate(run_time=2).set_value(0.75))

        self.play(Write(ratio_relation))

        self.play(b.animate(run_time=4).set_value(0.25))

        self.wait(2)
        
        self.play(Write(fulcrum_lever_text))

        self.wait(2)

        self.play(Create(area))

        self.wait(2)

        self.play(area.animate.move_to(H_dot.get_center()))

        self.wait(2)

        self.play(Create(area_triangle))

        self.wait(2)

        self.play(Write(area_fulcrum_text_final))

        self.wait(4)

        self.wait(55)
        