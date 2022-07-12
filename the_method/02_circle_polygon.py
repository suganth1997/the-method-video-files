from math import sqrt, tan, cos
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

        circle = Circle(r)

        inside_polygon = []

        outside_polygon = []

        for i in range(4, n):
            inside_polygon.append(RegularPolygon(i, radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2, start_angle=PI/2))
            outside_polygon.append(RegularPolygon(i, radius=r/cos(PI/i), stroke_width=DEFAULT_STROKE_WIDTH/2, start_angle=PI/2))

        # inside_polygon = RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)

        # outside_polygon = RegularPolygon(int(n.get_value()), radius=r/cos(PI/n.get_value()), stroke_width=DEFAULT_STROKE_WIDTH/2)

        # inside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r, stroke_width=DEFAULT_STROKE_WIDTH/2)))

        # outside_polygon.add_updater(lambda x: x.become(RegularPolygon(int(n.get_value()), radius=r/cos(PI/int(n.get_value())), stroke_width=DEFAULT_STROKE_WIDTH/2)))
        
        self.play(Create(circle))

        self.play(Create(inside_polygon[0]))

        self.play(Create(outside_polygon[0]))

        # self.activate_zooming(animate=False)

        # self.play(self.zoomed_camera.frame.animate.scale(0.75))

        # self.play(self.zoomed_camera.frame.animate.shift(2 * RIGHT))

        # self.play(n.animate.set_value(10), run_time=4)

        n_list = n - 5
        for i in range(n_list):
            self.play(ReplacementTransform(inside_polygon[i], inside_polygon[i + 1]), ReplacementTransform(outside_polygon[i], outside_polygon[i + 1]), circle.animate.set(stroke_width=DEFAULT_STROKE_WIDTH/2  + ((n_list - i - 1)/n_list)*DEFAULT_STROKE_WIDTH/2))

        self.wait(2)

        self.play(Uncreate(circle), Uncreate(inside_polygon[n_list]), Uncreate(outside_polygon[n_list]))

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

        m_base = -1
        c_base = 0.5

        m_base = 0.0
        c_base = 0.0

        x1_ = (-m_base - sqrt((m_base**2) - (4*a.get_value()*(c_base - 1))))/(2*a.get_value())
        x2_ = (-m_base + sqrt((m_base**2) - (4*a.get_value()*(c_base - 1))))/(2*a.get_value())

        parabola_graph = axes.get_graph(lambda x: f(x), color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)

        areas = []

        triangle_lines = [[{'m':m_base, 'c':c_base, 'x1':x1_, 'x2':x2_}]]

        triangle_lines_obj = [[axes.get_graph(lambda x: triangle_lines[0][0]['m']*x + triangle_lines[0][0]['c'], color=YELLOW, x_range=[x1_, x2_, 0.01], stroke_width=DEFAULT_STROKE_WIDTH/2)]]

        for i_div in range(divs):
            triangle_lines_now = []
            triangle_lines_now_obj = []
            areas_now = VGroup()
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

                areas_now += area_1 + area_2

            triangle_lines.append(triangle_lines_now)
            triangle_lines_obj.append(triangle_lines_now_obj)

            areas.append(areas_now)

        
        self.play(Create(parabola_graph))

        for triangle_line in triangle_lines_obj:
            triangle_create = []
            for line in triangle_line:
                triangle_create.append(Create(line))

            self.play(*triangle_create)

        
        for area in areas:
            self.play(Create(area))

        self.wait(2)