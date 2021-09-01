from re import U
from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan, exp, pi, log, log2
from manim import *
from numpy import number
from numpy.core.fromnumeric import sort

class BinarySearch(MovingCameraScene):
    def construct(self):
        question_1 = Text('Very similar to Binary search').scale(0.8)        
        question_1.to_edge(UP).to_edge(LEFT)

        self.play(Write(question_1))

        sorted_array = MathTex(*("2 ,\quad 5 ,\quad 9 ,\quad 13 ,\quad 21 ,\quad 25 ,\quad 31 ,\quad 35 ,\quad 39".split(" ")))

        self.play(Create(sorted_array))

        # for i in range(1):
        

        num_ind = list(range(0, len(sorted_array), 2))

        query_txt = MathTex("query").shift(2*UP).shift(2*RIGHT)

        self.play(Create(query_txt))

        A = 0
        B = len(num_ind) - 1

        sur_0 = SurroundingRectangle(sorted_array[num_ind[A]])

        sur_N = SurroundingRectangle(sorted_array[num_ind[B]])

        self.play(Create(sur_0), Create(sur_N))


        sur_N_2 = SurroundingRectangle(sorted_array[int(num_ind[int((A + B)/2)])])
        
        self.play(Create(sur_N_2))

        check_if = MathTex(">query").next_to(sur_N_2, UP)

        self.play(Write(check_if))

        # a = ApplyFunction(sorted_array[0].set_color, YELLOW)
        # b = ApplyFunction(sorted_array[1].set_color, YELLOW)

        self.play(ApplyMethod(sorted_array[0:int(len(sorted_array)/2)].set_color, RED))

        self.wait(2.0)

        self.play(ApplyMethod(sorted_array[0:int(len(sorted_array)/2)].set_color, WHITE))

        self.play(ApplyMethod(check_if.become, MathTex("<query").next_to(sur_N_2, UP)))

        self.play(ApplyMethod(sorted_array[int(len(sorted_array)/2)+1:len(sorted_array)].set_color, RED))

        self.wait(2.0)

        self.play(ApplyMethod(sorted_array[int(len(sorted_array)/2)+1:len(sorted_array)].set_color, WHITE))

        self.wait(2.0)

        self.play(ApplyMethod(query_txt.become, MathTex("query=13").shift(2*UP).shift(2*RIGHT)), Uncreate(check_if))

        self.wait(2.0)

        self.play(ReplacementTransform(sur_N, sur_N_2))

        sur_N = sur_N_2

        self.wait(1.0)

        B = int((A+B)/2)

        arr = [2, 5, 9, 13, 21, 25, 31, 35, 39]

        for i in range(2):

            sur_N_2 = SurroundingRectangle(sorted_array[num_ind[int((A + B)/2)]])

            self.play(Create(sur_N_2))

            self.wait(1.0)

            if arr[int((A+B)/2)] == 13:
                self.play(ReplacementTransform(sur_0, sur_N_2), ReplacementTransform(sur_N, sur_N_2))
                self.play(ApplyMethod(sorted_array[num_ind[int((A + B)/2)]].set_color, BLUE))
                self.wait(2.0)
                self.play(Uncreate(sur_N_2))
                break

            if arr[int((A+B)/2)] > 13:
                self.play(ReplacementTransform(sur_N, sur_N_2))
                sur_N = sur_N_2
                B = int((A+B)/2)

            else:
                self.play(ReplacementTransform(sur_0, sur_N_2))
                sur_0 = sur_N_2
                A = int((A+B)/2)

            self.wait(1.0)

        complexity = MathTex("log_2\ n").shift(2*UP).shift(2*LEFT)

        self.play(Write(complexity))

        self.play(ApplyMethod(complexity.become, MathTex("log_2\ 9 \simeq 3.17").shift(2*UP).shift(2*LEFT)))

        arr = [2, 50, 90, 130, 2100, 2500, 3100, 35000, 39000]

        # sorted_array = MathTex(*("2 ,\quad 5 ,\quad 9 ,\quad 13 ,\quad 21 ,\quad 25 ,\quad 31 ,\quad 35 ,\quad 39".split(" ")))

        self.play(ApplyMethod(sorted_array.become, MathTex(*(" ,\quad ".join([str(x) for x in arr]).split(" ")))))

        A = 0

        B = len(num_ind) - 1

        sur_0 = SurroundingRectangle(sorted_array[num_ind[A]])

        sur_N = SurroundingRectangle(sorted_array[num_ind[B]])

        self.play(Create(sur_0), Create(sur_N))


        for i in range(3):

            sur_N_2 = SurroundingRectangle(sorted_array[num_ind[int((A + B)/2)]])

            self.play(Create(sur_N_2))

            self.wait(1.0)

            if arr[int((A+B)/2)] == 130:
                self.play(ReplacementTransform(sur_0, sur_N_2), ReplacementTransform(sur_N, sur_N_2))
                self.play(ApplyMethod(sorted_array[num_ind[int((A + B)/2)]].set_color, BLUE))
                self.wait(2.0)
                self.play(Uncreate(sur_N_2))
                break

            if arr[int((A+B)/2)] > 130:
                self.play(ReplacementTransform(sur_N, sur_N_2))
                sur_N = sur_N_2
                B = int((A+B)/2)

            else:
                self.play(ReplacementTransform(sur_0, sur_N_2))
                sur_0 = sur_N_2
                A = int((A+B)/2)

            self.wait(1.0)


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
        ).shift(DOWN)

        numberLine = NumberLine([1, 2, 0.1], length=10, color=BLUE, include_numbers=True, number_scale_value=1, unit_size=10).shift(2*DOWN)

        self.play(Create(numberLine).set_run_time(1.0))

        def PlotBisection(f, A, B, n_steps):
                
                A = 1
                B = 2

                if f(A) < 0:
                    A, B = B, A    
            
                line_1 = Line(numberLine.n2p(A) - [0, 0.2, 0], numberLine.n2p(A) + [0, 0.2, 0], stroke_width = 4).set_color(YELLOW)
                line_2 = Line(numberLine.n2p(B) - [0, 0.2, 0], numberLine.n2p(B) + [0, 0.2, 0], stroke_width = 4).set_color(YELLOW)

                self.play(Create(line_1), Create(line_2))

                for i in range(n_steps):
                    C = (A + B)/2

                    mid_line = Line(numberLine.n2p(C) - [0, 0.2, 0], numberLine.n2p(C) + [0, 0.2, 0], stroke_width = 4).set_color(YELLOW)

                    self.play(Create(mid_line))

                    if f(C) > 0:
                        A = C
                        self.play(ReplacementTransform(line_1, mid_line))
                        line_1 = mid_line

                    else:
                        B = C
                        self.play(ReplacementTransform(line_2, mid_line))
                        line_2 = mid_line

                return line_1, line_2, mid_line, A, B

        
        f = lambda x : exp(-x) - exp(-1.114)

        line_1, line_2, midline, A, B = PlotBisection(f, 1, 2, 4)

        self.wait(2.0)

        numberLine_1 = NumberLine([1, 1.2, 0.01], length=10, color=BLUE, include_numbers=True, number_scale_value=0.5, unit_size=10).shift(2*DOWN)
        self.play(
            ApplyMethod(numberLine.become, numberLine_1),
            ApplyMethod(line_1.become, Line(numberLine_1.n2p(A) - [0, 0.2, 0], numberLine_1.n2p(A) + [0, 0.2, 0], stroke_width = 4).set_color(YELLOW)),
            ApplyMethod(line_2.become, Line(numberLine_1.n2p(B) - [0, 0.2, 0], numberLine_1.n2p(B) + [0, 0.2, 0], stroke_width = 4).set_color(YELLOW))
        )
        
        # self.play()
        # self.play()

        self.wait(2.0)

        arr = np.linspace(1, 2, 11)

        # sorted_array = MathTex(*("2 ,\quad 5 ,\quad 9 ,\quad 13 ,\quad 21 ,\quad 25 ,\quad 31 ,\quad 35 ,\quad 39".split(" ")))

        self.play(ApplyMethod(sorted_array.become, MathTex(*(" ,\quad ".join([str(round(x, 1)) for x in arr]).split(" ")))))

        self.wait(2.0)
        round
        # A = int((A+B)/2)

        # sur_N_2 = SurroundingRectangle(sorted_array[num_ind[int((A + B)/2)]])

        # self.play(Create(sur_N_2))

        # self.wait(1.0)

        # self.play(ReplacementTransform(sur_0, sur_N_2), ReplacementTransform(sur_N, sur_N_2))

        # self.play(ApplyMethod(sorted_array[num_ind[int((A + B)/2)]].set_color, BLUE))

        # # self.play(ApplyMethod(sorted_array[num_ind[int((A + B)/2)]].shift, UP))

        # self.wait(2.0)