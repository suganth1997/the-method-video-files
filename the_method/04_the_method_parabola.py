from math import cos, sin, sqrt, tan, atan, pi
from random import triangular
from typing_extensions import runtime
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

        quadrature_text = Text("Quadrature of Parabola", font_size = 80).shift(20*LEFT + 15*UP)
        
        the_method_text = Text("The Method", font_size = 80).shift(25*LEFT + 15*UP)

        MO_PO_text = MathTex("\\frac{MO}{PO} = ", font_size = 58).shift(15*LEFT + 8*UP)

        CA_AO_text = MathTex("\\frac{CA}{AO}", font_size = 58).next_to(MO_PO_text, RIGHT)

        CK_KN_text = MathTex("\\frac{CK}{KN}", font_size = 58).next_to(MO_PO_text, RIGHT)
        
        HK_KN_text = MathTex("\\frac{HK}{KN}", font_size = 58).next_to(MO_PO_text, RIGHT).shift(4*DOWN)

        ratio_relation = VGroup(MO_PO_text, CK_KN_text)
        
        fulcrum_lever_text = MathTex("MO\\times KN = OP\\times HK", font_size = 58).shift(15*LEFT + 4*UP)

        lever_ = Line(7*LEFT, 8*RIGHT).next_to(fulcrum_lever_text, 6*DOWN).shift(4*LEFT)
        
        # fulcrum_lever_illus

        lever_center = [-18, 2.3, 0] # lever_.get_center()
        lever_left_coord = lever_.get_left()
        lever_right_coord = lever_.get_right()

        print(lever_center)

        # dist = lambda x1, x2: sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

        # HK_length = dist(axes.c2p(*[-sqrt(1.0/a.get_value()), HKC(-sqrt(1.0/a.get_value()))]), axes.c2p(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value()))]))

        # [-sqrt(1.0/4.0), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [2 * f(0), (-2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1])/2]

        # KN_length = dist(axes.c2p(*[-sqrt(1.0/a.get_value()), HKC(-sqrt(1.0/a.get_value()))]), axes.c2p(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), HKC(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))

        # print(-sqrt(1.0/a.get_value()), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))

        # print("KN_length = ", KN_length, ", HK_length = ", HK_length)

        # lever_left_coord = lever_center - np.array([HK_length, 0, 0])/1.75

        # lever_right_coord = lever_center + np.array([KN_length, 0, 0])/1.75

        dist = lambda x1, x2: sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

        HK_length = dist(axes.c2p(*[-sqrt(1.0/a.get_value()), HKC(-sqrt(1.0/a.get_value()))]), axes.c2p(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value()))]))

        def get_left_and_right_coord():
            HK_length = dist(axes.c2p(*[-sqrt(1.0/a.get_value()), HKC(-sqrt(1.0/a.get_value()))]), axes.c2p(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value()))]))

            KN_length = dist(axes.c2p(*[-sqrt(1.0/a.get_value()), HKC(-sqrt(1.0/a.get_value()))]), axes.c2p(*[-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), HKC(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))]))

            lever_left_coord = lever_center - np.array([HK_length, 0, 0]) # /1.75

            lever_right_coord = lever_center + np.array([KN_length, 0, 0]) # /1.75

            return lever_left_coord, lever_right_coord

        lever_left_coord, lever_right_coord = get_left_and_right_coord()

        def lever_updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            x.become(Line(lever_left_coord, lever_right_coord))

        # lever_right_coord[0] = lever_center[0] + (lever_center[0] - lever_left_coord[0])/2
        # lever_right_coord[1] = lever_center[1] + (lever_center[1] - lever_left_coord[1])/2
        # lever_right_coord[2] = lever_center[2] + (lever_center[2] - lever_left_coord[2])/2

        lever_ = Line(lever_left_coord, lever_right_coord)
        lever_left = Line(lever_left_coord, lever_center)
        lever_right = Line(lever_center, lever_right_coord)

        lever_.add_updater(lever_updater)

        f_l_center_dot = Dot(lever_center, radius=2*DEFAULT_DOT_RADIUS)
        f_l_left_dot = Dot(lever_left_coord, radius=2*DEFAULT_DOT_RADIUS)
        f_l_right_dot = Dot(lever_right_coord, radius=2*DEFAULT_DOT_RADIUS)

        def f_l_right_dot_updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            x.become(Dot(lever_right_coord, radius=2*DEFAULT_DOT_RADIUS))

        f_l_right_dot.add_updater(f_l_right_dot_updater)

        l_H = Text("H", font_size=48).next_to(f_l_left_dot, RIGHT + UP)
        l_K = Text("K", font_size=48).next_to(f_l_center_dot, UP)
        l_N = Text("N", font_size=48).next_to(f_l_right_dot, LEFT + UP)

        def l_N_updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            f_l_right_dot = Dot(lever_right_coord, radius=2*DEFAULT_DOT_RADIUS)
            x.become(Text("N", font_size=48).next_to(f_l_right_dot, LEFT + UP))

        l_N.add_updater(l_N_updater)

        lever_all = VGroup(lever_, f_l_left_dot, f_l_right_dot)

        fulcrum = Polygon(lever_center, lever_center + (2*LEFT+2*DOWN)/2, lever_center + (2*RIGHT+2*DOWN)/2, fill_opacity=1)

        fulcrum_all = VGroup(fulcrum, f_l_center_dot)

        TG_line_ = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2).move_to(lever_left_coord)

        def TG_line__updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, f(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())))], add_vertex_dots=False, line_color=BLUE, stroke_width=DEFAULT_STROKE_WIDTH*2).move_to(lever_left_coord))

        TG_line_.add_updater(TG_line__updater)

        MO_line_f = axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2).move_to(lever_right_coord)

        def MO_line_f_updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            x.become(axes.get_line_graph([-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value())), -sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))], [0.0, -2*a.get_value()*sqrt(1.0/a.get_value())*(-sqrt(1.0/a.get_value()) + b.get_value()*(2*sqrt(1.0/a.get_value()))) + tangent(0)[1]], add_vertex_dots=False, line_color=RED, stroke_width=DEFAULT_STROKE_WIDTH*2).move_to(lever_right_coord))

        MO_line_f.add_updater(MO_line_f_updater)

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
        self.play(Create(AB_line), Create(BC_line))
        self.play(Create(BK_line))

        self.play(Create(A_dot), Create(A_text), Create(C_dot), Create(C_text), Create(B_dot), Create(B_text), Create(D_dot), Create(D_text), Create(E_dot), Create(E_text), Create(F_dot), Create(F_text), Create(O_dot), Create(O_text), Create(M_dot), Create(M_text), Create(P_dot), Create(P_text), Create(N_dot), Create(N_text), Create(K_dot), Create(K_text))

        self.play(b.animate(run_time=4).set_value(0.75))

        self.play(b.animate(run_time=4).set_value(0.25))

        # self.wait(4)

        self.play(self.camera.frame.animate.move_to([-8, 6, 0]))

        self.play(Write(quadrature_text))

        self.play(FadeIn(MO_line))
        
        self.play(FadeOut(MO_line))

        self.play(FadeIn(PO_line))

        self.play(FadeOut(PO_line))

        self.play(Write(MO_PO_text))

        self.play(FadeIn(CA_line))
        
        self.play(FadeOut(CA_line))

        self.play(FadeIn(AO_line))

        self.play(FadeOut(AO_line))

        self.play(Write(CA_AO_text))

        self.play(FadeIn(CK_line))
        
        self.play(FadeOut(CK_line))

        self.play(FadeIn(KN_line))

        self.play(FadeOut(KN_line))

        self.play(Unwrite(CA_AO_text))

        self.play(Write(CK_KN_text))

        self.play(Unwrite(quadrature_text))
        
        self.play(Write(the_method_text))

        self.play(ratio_relation.animate.shift(4*DOWN))

        self.play(Create(HK_line), Create(H_dot), Create(H_text))

        self.play(FadeIn(HK_line_))

        self.play(FadeOut(HK_line_))

        self.play(Unwrite(CK_KN_text))

        self.play(Write(HK_KN_text))

        self.play(Unwrite(MO_PO_text), Unwrite(HK_KN_text))

        self.play(Write(fulcrum_lever_text))

        self.wait(2)

        # TODO: animate fulcrum and lever with line lengths, and conclude with archimedes quote
        
        # self.play(Create(TG_line_))

        # self.play(TG_line_.animate.move_to(axes.coords_to_point(*[-3*sqrt(1.0/a.get_value()), HKC(-3*sqrt(1.0/a.get_value())), 0.0])))

        # self.add(TG_line)

        # self.play(Uncreate(TG_line_))

        self.play(Create(PO_line))

        self.play(b.animate(run_time=4).set_value(0.0))

        self.play(b.animate(run_time=2).set_value(1.0))

        self.play(b.animate(run_time=2).set_value(0.25))

        self.play(fulcrum_lever_text.animate.shift(8*UP + 7*LEFT))

        self.play(Create(lever_all), self.camera.frame.animate.move_to([-15, 6, 0]), fulcrum_lever_text.animate.shift(7*LEFT), the_method_text.animate.shift(7*LEFT))

        self.play(Create(fulcrum_all))

        self.play(Write(l_H), Write(l_K), Write(l_N))

        self.play(Create(PO_line_), Create(PO_line__))

        self.play(ReplacementTransform(PO_line_, TG_line))

        self.play(ReplacementTransform(PO_line__, TG_line_))

        self.play(Create(MO_line_), Create(MO_line))

        self.play(ReplacementTransform(MO_line_, MO_line_f))

        self.play(b.animate(run_time=6).set_value(0.75))

        self.play(b.animate(run_time=2).set_value(1.0))

        self.play(b.animate(run_time=6).set_value(0.0))

        self.play(b.animate(run_time=2).set_value(0.25))

        self.wait(4)

        self.play(Create(area), run_time=4)

        # self.play(area.animate.scale(1.0/1.75), run_time=2)

        self.play(area.animate.move_to(lever_left_coord), run_time=2)

        self.play(Create(area_triangle))

        # self.play(area_triangle.animate.scale(1.0/1.75), run_time=2)

        tr_l = area_triangle.get_left()
        tr_center = area_triangle.get_center()

        AF_length = np.linalg.norm(A_dot.get_center() - F_dot.get_center())
        AC_length = np.linalg.norm(A_dot.get_center() - C_dot.get_center())
        KC_length = np.linalg.norm(K_dot.get_center() - C_dot.get_center())

        AF_length *= AC_length/KC_length

        triangle_vis_eq = Polygon(lever_center + AF_length*UP/2, lever_center - AF_length*UP/2, lever_center + KC_length*RIGHT, fill_color=BLUE, fill_opacity=0.5)

        self.play(area_triangle.animate.move_to(lever_center + (tr_center - tr_l) + 2*UP), run_time=2)

        self.play(b.animate(run_time=2).set_value(0.0))

        lever_left_coord, lever_right_coord = get_left_and_right_coord()

        MO_line_f_ = Line(lever_right_coord - AF_length*UP/2, lever_right_coord + AF_length*UP/2)

        def MO_line_f__updater(x):
            lever_left_coord, lever_right_coord = get_left_and_right_coord()
            b_f = 1 - b.get_value()
            AC_b_f = b_f*KC_length
            AF_b_f = AC_b_f * AF_length / (KC_length * 2)
            x.become(Line(lever_right_coord - AF_b_f*UP, lever_right_coord + AF_b_f*UP))

        MO_line_f_.add_updater(MO_line_f__updater)

        self.play(ReplacementTransform(area_triangle, triangle_vis_eq), ReplacementTransform(MO_line_f, MO_line_f_))

        self.play(b.animate(run_time=2).set_value(1.0))

        # self.play(self.camera.frame.animate.move_to([-15, 6, 0]), fulcrum_lever_text.animate.shift(7*LEFT), the_method_text.animate.shift(7*LEFT))

        # self.play(area_triangle.animate.stretch_in_place(1.0/1.75, 0))
        
        self.wait(4)
