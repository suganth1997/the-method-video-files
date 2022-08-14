from math import sqrt, tan, cos
from multiprocessing.sharedctypes import Value
from manim import *

from numpy import poly

class PiWithPolygon(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            # zoomed_display_height=1,
            # zoomed_display_width=3,
            # image_frame_stroke_width=20,
            # zoomed_camera_config={
            #     "default_frame_stroke_width": 3,
            # },
            **kwargs
        )

    def construct(self):

        r = 2

        n = 15

        circle = Circle(r).shift(4*RIGHT)

        inside_polygon = []

        outside_polygon = []

        n_side_texts = []

        inner_polygon_text = Text('Perimeter of circle > Perimeter of inner polygon', font_size=20).shift(3*LEFT + UP)

        inner_polygon_perimeter = MathTex('2\pi r > 2nr\ sin\\left(\\frac{180}{n}\\right)', font_size=24).next_to(inner_polygon_text, DOWN)

        outer_polygon_text = Text('Perimeter of circle < Perimeter of outer polygon', font_size=20).next_to(inner_polygon_perimeter, 2*DOWN)

        outer_polygon_perimeter = MathTex('2\pi r < 2nr\ tan\\left(\\frac{180}{n}\\right)', font_size=24).next_to(outer_polygon_text, DOWN)

        pi_perimeter_bounds = MathTex('n\ sin\\left(\\frac{180}{n}\\right) < \pi < n\ tan\\left(\\frac{180}{n}\\right)', font_size=24).next_to(outer_polygon_perimeter, DOWN)

        for i in range(4, n):
            n_side_texts.append(MathTex('n = ' + str(i)).to_corner(UP+RIGHT))
            inside_polygon.append(RegularPolygon(i, radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2, start_angle=PI/2).shift(4*RIGHT))
            outside_polygon.append(RegularPolygon(i, radius=r/cos(PI/i), stroke_width=DEFAULT_STROKE_WIDTH/2, start_angle=PI/2).shift(4*RIGHT))

        # inside_polygon = RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # outside_polygon = RegularPolygon(int(n.get_value()), radius=r/cos(PI/n.get_value()), stroke_width=DEFAULT_STROKE_WIDTH/2)

        # inside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)))

        # outside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r/cos(PI/int(n.get_value())), stroke_width=DEFAULT_STROKE_WIDTH/2)))
        
        self.wait(7)

        self.play(Create(circle))

        self.wait(10)
        
        self.play(Create(inside_polygon[0]), run_time=2)

        self.play(Create(outside_polygon[0]), run_time=2)

        # self.activate_zooming(animate=False)

        # self.play(self.zoomed_camera.frame.animate.scale(0.75))

        # self.play(self.zoomed_camera.frame.animate.shift(2 * RIGHT))

        # self.play(n.animate.set_value(10), run_time=4)

        n_list = n - 5
        for i in range(1):
            self.play(Create(n_side_texts[0]))
            self.play(ReplacementTransform(inside_polygon[i], inside_polygon[i + 1]), ReplacementTransform(outside_polygon[i], outside_polygon[i + 1]), circle.animate.set(stroke_width=DEFAULT_STROKE_WIDTH/2  + ((n_list - i - 1)/n_list)*DEFAULT_STROKE_WIDTH/2), ReplacementTransform(n_side_texts[i], n_side_texts[i + 1]))

        self.play(Write(inner_polygon_text))

        self.play(Write(outer_polygon_text))

        self.play(Write(inner_polygon_perimeter))

        self.play(Write(outer_polygon_perimeter))

        self.wait(8)

        self.play(Write(pi_perimeter_bounds), run_time=2)

        self.wait(3)

        for i in range(1, n_list):
            self.play(ReplacementTransform(inside_polygon[i], inside_polygon[i + 1]), ReplacementTransform(outside_polygon[i], outside_polygon[i + 1]), circle.animate.set(stroke_width=DEFAULT_STROKE_WIDTH/2  + ((n_list - i - 1)/n_list)*DEFAULT_STROKE_WIDTH/2), ReplacementTransform(n_side_texts[i], n_side_texts[i + 1]))

        self.wait(10)

        self.play(Uncreate(circle), Uncreate(inside_polygon[n_list]), Uncreate(outside_polygon[n_list]))

        self.play(Unwrite(inner_polygon_text), Unwrite(inner_polygon_perimeter), Unwrite(outer_polygon_text), Unwrite(outer_polygon_perimeter), Unwrite(pi_perimeter_bounds), Uncreate(n_side_texts[n_list]))

        self.wait(2)

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

        start_base = [{'m':0.0, 'c':0.0}]

        divs = 3

        # m_base = -1
        # c_base = 0.5

        m_base = ValueTracker(0.0)
        c_base = ValueTracker(0.0)

        x1_ = (-m_base.get_value() - sqrt((m_base.get_value()**2) - (4*a.get_value()*(c_base.get_value() - 1))))/(2*a.get_value())
        
        x2_ = (-m_base.get_value() + sqrt((m_base.get_value()**2) - (4*a.get_value()*(c_base.get_value() - 1))))/(2*a.get_value())

        parabola_graph = axes.get_graph(lambda x: f(x), color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)

        def get_parabola_triangles():
            areas = []

            x1_ = (-m_base.get_value() - sqrt((m_base.get_value()**2) - (4*a.get_value()*(c_base.get_value() - 1))))/(2*a.get_value())
            x2_ = (-m_base.get_value() + sqrt((m_base.get_value()**2) - (4*a.get_value()*(c_base.get_value() - 1))))/(2*a.get_value())


            triangle_lines = [[{'m':m_base.get_value(), 'c':c_base.get_value(), 'x1':x1_, 'x2':x2_}]]

            triangle_lines_obj = [[axes.get_graph(lambda x: triangle_lines[0][0]['m']*x + triangle_lines[0][0]['c'], color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)]]

            for i_div in range(divs):
                triangle_lines_now = []
                triangle_lines_now_obj = []
                areas_now = []
                for i_base, bases in enumerate(triangle_lines[i_div]):
                    x1 = bases['x1']
                    y1 = f(x1)

                    x3 = -bases['m']/(2*a.get_value())
                    y3 = f(x3)

                    m1 = (y3 - y1) / (x3 - x1)
                    c1 = y1 - m1 * x1

                    triangle_lines_now.append({'m':m1, 'c':c1, 'x1':x1, 'x2':x3})
                    triangle_lines_now_obj.append(axes.get_graph(lambda x: m1*x+c1, color=YELLOW, x_range=[x1, x3, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/(i_div + 2)))
                    
                    x2 = bases['x2']
                    y2 = f(x2)

                    m2 = (y3 - y2) / (x3 - x2)
                    c2 = y2 - m2 * x2

                    triangle_lines_now.append({'m':m2, 'c':c2, 'x1':x3, 'x2':x2})
                    triangle_lines_now_obj.append(axes.get_graph(lambda x: m2*x+c2, color=YELLOW, x_range=[x3, x2, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/(i_div + 2)))

                    print(i_div, i_base, triangle_lines[i_div][i_base])

                    m_ = triangle_lines[i_div][i_base]['m']
                    c_ = triangle_lines[i_div][i_base]['c']

                    area_1 = axes.get_area(triangle_lines_now_obj[0], [x1, x3], bounded=axes.get_graph(lambda x: m_*x+c_, color=YELLOW, x_range=[x1, x3, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/(i_div + 2)), dx_scaling=5, color=GREEN)

                    area_2 = axes.get_area(triangle_lines_now_obj[1], [x3, x2], bounded=axes.get_graph(lambda x: m_*x+c_, color=YELLOW, x_range=[x1, x3, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/(i_div + 2)), dx_scaling=5, color=GREEN)

                    areas_now.append(area_1 + area_2)

                triangle_lines.append(triangle_lines_now)
                triangle_lines_obj.append(triangle_lines_now_obj)

                areas.append(areas_now)

            return triangle_lines_obj, areas, triangle_lines

        triangle_lines_obj, areas, triangle_lines = get_parabola_triangles()

        # print(triangle_lines_obj)
        
        self.play(Create(parabola_graph))

        self.play(Create(triangle_lines_obj[0][0]))

        # parabola_graph_segment_group = VGroup(parabola_graph, triangle_lines_obj[0][0])

        def parabola_graph_updater(x):
            parabola_graph = axes.get_graph(lambda x: f(x), color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)

            triangle_lines_obj, areas, triangle_lines = get_parabola_triangles()

            parabola_graph_segment = VGroup(parabola_graph, triangle_lines_obj[0][0])

            x.become(parabola_graph)

        def parabola_graph_line_updater(x):
            parabola_graph = axes.get_graph(lambda x: f(x), color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)

            triangle_lines_obj, areas, triangle_lines = get_parabola_triangles()

            parabola_graph_segment = VGroup(parabola_graph, triangle_lines_obj[0][0])

            x.become(triangle_lines_obj[0][0])

        parabola_graph.add_updater(parabola_graph_updater)
        triangle_lines_obj[0][0].add_updater(parabola_graph_line_updater)

        self.play(m_base.animate(run_time=4).set_value(0.25))

        self.wait(12)

        self.play(m_base.animate(run_time=4).set_value(0.0))

        parabola_graph.remove_updater(parabola_graph_updater)
        triangle_lines_obj[0][0].remove_updater(parabola_graph_line_updater)

        return
        for triangle_line in triangle_lines_obj[1:2]:
            triangle_create = []
            for line in triangle_line:
                triangle_create.append(Create(line))

            self.play(*triangle_create)

        x_A = triangle_lines[0][0]['x1']
        A_dot = Dot(axes.coords_to_point(*[x_A, f(x_A)]), radius=DEFAULT_DOT_RADIUS*2/3)
        A_text = Text("A", font_size=20).next_to(A_dot, LEFT/2)

        x_B = triangle_lines[0][0]['x2']
        B_dot = Dot(axes.coords_to_point(*[x_B, f(x_B)]), radius=DEFAULT_DOT_RADIUS*2/3)
        B_text = Text("B", font_size=20).next_to(B_dot, RIGHT/2)

        x_C = triangle_lines[1][0]['x2']
        C_dot = Dot(axes.coords_to_point(*[x_C, f(x_C)]), radius=DEFAULT_DOT_RADIUS*2/3)
        C_text = Text("C", font_size=20).next_to(C_dot, UP/2)

        self.play(Create(A_dot), Create(B_dot), Create(C_dot))
        
        self.play(Write(A_text), Write(B_text), Write(C_text))

        self.wait(15)

        x_D = triangle_lines[2][0]['x2']
        D_dot = Dot(axes.coords_to_point(*[x_D, f(x_D)]), radius=DEFAULT_DOT_RADIUS*2/3)
        D_text = Text("D", font_size=20).next_to(D_dot, (LEFT + UP)/2)

        x_E = triangle_lines[2][2]['x2']
        E_dot = Dot(axes.coords_to_point(*[x_E, f(x_E)]), radius=DEFAULT_DOT_RADIUS*2/3)
        E_text = Text("E", font_size=20).next_to(E_dot, (RIGHT + UP)/2)

        # for area in areas:
        #     self.play(Create(area))

        triangle_ABC = MathTex("\Delta ABC").shift(2*UP + 4*LEFT)

        triangle_ADC = MathTex("= \\frac{1}{8}\Delta ADC").next_to(triangle_ABC, RIGHT)

        area_of_parabola = MathTex("\\text{Area of Parabola}", font_size=24).shift(2*UP + 4*LEFT)

        area_series = MathTex("= \Delta ABC + 2\\times\\frac{1}{8}\Delta ABC + 4\\times\\frac{1}{8^2}\Delta ABC+...", font_size = 24).next_to(area_of_parabola, RIGHT)

        area_series_1 = MathTex("= \\left(1 + \\frac{1}{4} + \\frac{1}{16} + ...\\right)\Delta ABC", font_size = 24).next_to(area_of_parabola, RIGHT)

        area_series_2 = MathTex("= \\left(1 + \\frac{1}{4}\left(1 + \\frac{1}{4} + ...\\right)\\right)\Delta ABC", font_size = 24).next_to(area_of_parabola, RIGHT)
        
        area_series_3 = MathTex("= \Delta ABC + \\frac{1}{4}\left(1 + \\frac{1}{4} + ...\\right)\Delta ABC", font_size = 24).next_to(area_of_parabola, RIGHT)
        
        area_series_4 = MathTex("= \Delta ABC + \\frac{1}{4}\\text{Area of Parabola}", font_size = 24).next_to(area_of_parabola, RIGHT)
        
        area_series_5 = MathTex("= \\frac{4}{3}\Delta ABC", font_size = 24).next_to(area_of_parabola, RIGHT)

        for triangle_line in triangle_lines_obj[2:]:
            triangle_create = []
            for line in triangle_line:
                triangle_create.append(Create(line))

            self.play(*triangle_create, run_time = 2)

        self.play(Create(D_dot), Create(E_dot))
        
        self.play(Write(D_text), Write(E_text))
        
        self.play(Create(areas[0][0]))

        self.play(areas[0][0].animate(run_time=0.75).set_opacity(1.0))

        self.play(areas[0][0].animate(run_time=0.75).set_opacity(0.3), Write(triangle_ABC))

        self.play(Create(areas[1][0]))

        self.play(areas[1][0].animate(run_time=0.75).set_opacity(1.0))

        self.play(areas[1][0].animate(run_time=0.75).set_opacity(0.3), Write(triangle_ADC))

        self.wait(5)

        self.play(Create(areas[1][1]))

        self.play(Unwrite(triangle_ABC), Unwrite(triangle_ADC))

        self.play(Write(area_of_parabola))

        self.play(Write(area_series), Create(areas[2][0]), Create(areas[2][1]), Create(areas[2][2]), Create(areas[2][3]))

        self.wait(5)

        self.play(ReplacementTransform(area_series, area_series_1))

        self.wait(2)

        self.play(ReplacementTransform(area_series_1, area_series_2))

        self.wait(2)

        self.play(ReplacementTransform(area_series_2, area_series_3))
        
        self.wait(2)

        self.play(ReplacementTransform(area_series_3, area_series_4))

        self.wait(2)

        self.play(ReplacementTransform(area_series_4, area_series_5))

        # parabola_triangles_group_list = [x for xs in triangle_lines_obj for x in xs]

        # print(parabola_triangles_group_list)

        # parabola_triangles_group = Group(*parabola_triangles_group_list)
        
        # def parabola_updater(x):

        #     triangle_lines_obj, areas = get_parabola_triangles()
            
        #     parabola_triangles_group_list = [x for xs in triangle_lines_obj for x in xs]

        #     parabola_triangles_group = Group(*parabola_triangles_group_list)

        #     x.become(parabola_triangles_group_list)

        # parabola_triangles_group.add_updater(parabola_updater)

        self.wait(7)

        # self.play(c_base.animate.set_value(0.5))
