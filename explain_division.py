from re import U
from typing_extensions import runtime
from math import sqrt, cos, sin, tan, atan, exp, pi, log, log2
from manim import *
from numpy import number

class ExplainDivision(MovingCameraScene):
    def construct(self):
        question_1 = Text('How many steps will it take to reach the solution?').scale(0.8)

        
        question_1.to_edge(UP).to_edge(LEFT)

        sub_question = Tex('To reach a given accuracy, say').next_to(question_1, DOWN)
        e_5 = MathTex('10^{-3}').next_to(sub_question)

        sub_group = VGroup(sub_question, e_5).to_edge(LEFT)

        self.play(Write(question_1))

        self.play(Create(sub_group))

        self.wait(1.0)

        f = lambda x : exp(-x) - exp(-1.114)

        numberLine = NumberLine([-5, 5], color=BLUE, include_numbers=True)

        format_number = lambda x : "{:.4s}".format('{:0.4f}'.format(x))

        # xValTrack = ValueTracker(0)

        # fx00 = MathTex("f(" + format_number(xValTrack.get_value()) + ")=" + format_number(f(xValTrack.get_value()))).move_to([xValTrack.get_value(), 0, 0])

        # # fx0.add_updater(lambda x: x.become(MathTex("f(" + str(xValTrack.get_value()) + ")=1").move_to([xValTrack.get_value(), 0, 0])))
        # fx00.add_updater(lambda x: x.become(MathTex("f(" + format_number(xValTrack.get_value()) + ")=" + format_number(f(xValTrack.get_value()))).move_to([xValTrack.get_value(), 0, 0])))
        # self.play(Create(fx00))
        # # self.play(Transform(fx00, fx00.move_to([2, 0, 0])))
        # # self.play(Create(fx00))

        # self.play(xValTrack.animate(run_time=4).set_value(2.0))
        # self.wait(2)

        fx0 = MathTex("f(x) = e^{-x} - e^{-1.114}").move_to([4, 1.75, 0])

        n_steps_str = Tex("N = ", str(0)).align_on_border(LEFT).shift(DOWN/2)
        b_a_eq = MathTex("b-a=").next_to(n_steps_str).shift(RIGHT)
        accuracy_value = DecimalNumber(1.0, num_decimal_places=4).next_to(b_a_eq)

        accuracy_line = VGroup(n_steps_str, b_a_eq, accuracy_value)

        mainNumberLine = NumberLine([1, 2, 0.25], length=10, color=BLUE, include_numbers=True, number_scale_value=1, unit_size=10).move_to([0, 0.75, 0])

        numberLine_prev = NumberLine([1, 2, 0.5], length=10, color=YELLOW, include_numbers=True, number_scale_value=1, unit_size=10).move_to([0, -2, 0])

        A = 1.0

        B = 2.0

        text_a = MathTex("a").move_to(numberLine_prev.n2p(A) + [0, 0.5, 0])
        text_b = MathTex("b").move_to(numberLine_prev.n2p(B) + [0, 0.5, 0])
        numberLine_prev_group = VGroup(text_a, text_b, numberLine_prev)
        

        line_1 = Line(mainNumberLine.n2p(A) - [0, 0.2, 0], mainNumberLine.n2p(A) + [0, 0.2, 0], color=YELLOW)

        line_2 = Line(mainNumberLine.n2p(B) - [0, 0.2, 0], mainNumberLine.n2p(B) + [0, 0.2, 0], color=YELLOW)

        self.play(Create(numberLine), Create(fx0))
        
        self.play(ReplacementTransform(numberLine, mainNumberLine))

        self.play(Write(accuracy_line))

        self.play(Create(numberLine_prev_group), Create(line_1), Create(line_2))
        
        N_acc_1_2 = MathTex("\\frac{1}{2^{" + str(4) + "}}").next_to(accuracy_value).to_edge(RIGHT)

        for i in range(12):
            C = (A + B) / 2

            mid_line = Line(mainNumberLine.n2p(C) - [0, 0.2, 0], mainNumberLine.n2p(C) + [0, 0.2, 0], color=YELLOW, stroke_width = 2.0 + 4*abs(C - 1.114))

            self.play(Create(mid_line))

            if f(C) > 0:
                A = C

                number_line_next = NumberLine([A, B, abs(A - B)/2], length=10, color=YELLOW, include_numbers=True, number_scale_value=1, unit_size=10).move_to([0, -2, 0])
                text_a = MathTex("a").move_to(number_line_next.n2p(A) + [0, 0.5, 0])
                text_b = MathTex("b").move_to(number_line_next.n2p(B) + [0, 0.5, 0])
                number_line_next_group = VGroup(text_a, text_b, number_line_next)

                n_steps_str = Tex("N = ", str(i + 1)).align_on_border(LEFT).shift(DOWN/2)
                b_a_eq = MathTex("b-a=").next_to(n_steps_str).shift(RIGHT)
                accuracy_value = DecimalNumber(B - A, num_decimal_places=4).next_to(b_a_eq)

                self.play(
                    ReplacementTransform(line_1, mid_line), 
                    ReplacementTransform(numberLine_prev_group, number_line_next_group),
                    ApplyMethod(accuracy_line.become, VGroup(
                        n_steps_str,
                        b_a_eq,
                        accuracy_value
                    )),
                    # ApplyMethod(n_steps_str.become, Tex("Number of steps = " + str(i + 1) + ", b - a = ").align_on_border(LEFT).shift(DOWN/2)),
                    # ApplyMethod(accuracy_value.become, DecimalNumber(B - A, num_decimal_places=4).next_to(Tex("Number of steps = " + str(i + 1) + ", b - a = ").align_on_border(LEFT).shift(DOWN/2)))
                )

                numberLine_prev_group = number_line_next_group

                line_1 = mid_line

            else:
                B = C
                
                number_line_next = NumberLine([A, B, abs(A - B)/2], length=10, color=YELLOW, include_numbers=True, number_scale_value=1, unit_size=10).move_to([0, -2, 0])
                text_a = MathTex("a").move_to(number_line_next.n2p(A) + [0, 0.5, 0])
                text_b = MathTex("b").move_to(number_line_next.n2p(B) + [0, 0.5, 0])
                number_line_next_group = VGroup(text_a, text_b, number_line_next)

                n_steps_str = Tex("N = ", str(i + 1)).align_on_border(LEFT).shift(DOWN/2)
                b_a_eq = MathTex("b-a=").next_to(n_steps_str).shift(RIGHT)
                accuracy_value = DecimalNumber(B - A, num_decimal_places=4).next_to(b_a_eq)

                self.play(
                    ReplacementTransform(line_2, mid_line), 
                    ReplacementTransform(numberLine_prev_group, number_line_next_group),
                    ApplyMethod(accuracy_line.become, VGroup(
                        n_steps_str,
                        b_a_eq,
                        accuracy_value
                    )),
                    # ApplyMethod(n_steps_str.become, Tex("Number of steps = " + str(i + 1) + ", b - a = ").align_on_border(LEFT).shift(DOWN/2)),
                    # ApplyMethod(accuracy_value.become, DecimalNumber(B - A, num_decimal_places=4).next_to(Tex("Number of steps = " + str(i + 1) + ", b - a = ").align_on_border(LEFT).shift(DOWN/2)))
                )

                numberLine_prev_group = number_line_next_group

                line_2 = mid_line

            # N_acc_1_2 = MathTex("\\frac{1}{2^{" + str(i + 1) + "}}").next_to(accuracy_value).shift(RIGHT)

            # if i > 3:
            #     self.play(ApplyMethod(N_acc_1_2.become, MathTex("\\frac{1}{2^{" + str(i + 1) + "}}").next_to(accuracy_value).to_edge(RIGHT)))

            if i == 3:
                surround_accuracy = SurroundingRectangle(accuracy_value)
                self.play(Create(surround_accuracy))
                less_than_0_1 = MathTex("\leq 0.1").next_to(surround_accuracy)
                self.play(Write(less_than_0_1))
                surround_n_steps = SurroundingRectangle(n_steps_str[1])
                self.play(Create(surround_n_steps))

                self.play(ApplyMethod(sub_group.become, Tex("How close are we to the solution?").next_to(question_1, DOWN).to_edge(LEFT)))

                interval_len = MathTex("2 - 1 = 1").next_to(less_than_0_1).shift(RIGHT)
                self.play(Create(interval_len))

                for j in range(4):
                    self.play(ApplyMethod(interval_len.become, MathTex("\\frac{1}{2^{" + str(j + 1) + "}}").next_to(less_than_0_1).shift(RIGHT)))

                self.play(ApplyMethod(interval_len.become, MathTex("\\frac{1}{2^{" + str(j + 1) + "}}\\leq 0.1").next_to(less_than_0_1).shift(RIGHT)))
                self.play(ApplyMethod(interval_len.become, MathTex("\\frac{1}{2^{N}}\\leq 0.1").next_to(less_than_0_1).shift(RIGHT)))
                self.play(ApplyMethod(interval_len.become, MathTex("2^{N}\\geq\\frac{1}{0.1}").next_to(less_than_0_1).shift(RIGHT)))

                log_simeq = MathTex("N\\geq log_2(\\frac{1}{0.1}) \simeq ").next_to(less_than_0_1).shift(RIGHT)
                self.play(ApplyMethod(interval_len.become, VGroup(log_simeq, DecimalNumber(log2(10)).next_to(log_simeq))))

                self.wait(2.0)

                log_simeq = MathTex("N\\geq log_2(\\frac{1}{0.01}) \simeq ").next_to(less_than_0_1).shift(RIGHT)
                self.play(ApplyMethod(interval_len.become, VGroup(log_simeq, DecimalNumber(log2(100)).next_to(log_simeq))))

                self.wait(2.0)

                self.play(
                    Uncreate(surround_accuracy), 
                    Uncreate(less_than_0_1), 
                    Uncreate(surround_n_steps), 
                    # Uncreate(interval_len),
                    # ReplacementTransform(interval_len, N_acc_1_2)
                )

                N_acc_1_2 = interval_len

                # return

            if i == 6:
                surround_accuracy = SurroundingRectangle(accuracy_value)
                self.play(Create(surround_accuracy))
                less_than_0_1 = MathTex("\leq 0.01").next_to(surround_accuracy)
                self.play(Write(less_than_0_1))
                surround_n_steps = SurroundingRectangle(n_steps_str[1])
                self.play(Create(surround_n_steps))

                # self.play(ApplyMethod(N_acc_1_2.become, MathTex("N\\geq log_2(\\frac{1}{0.01})").next_to(less_than_0_1).shift(RIGHT)))

                self.wait(2.0)

                log_simeq = MathTex("N\\geq log_2(\\frac{1}{0.001}) \simeq ").next_to(less_than_0_1)
                self.play(ApplyMethod(N_acc_1_2.become, VGroup(log_simeq, DecimalNumber(log2(1000)).next_to(log_simeq))))

                self.wait(2.0)

                self.play(Uncreate(surround_accuracy), Uncreate(less_than_0_1), Uncreate(surround_n_steps))

            if i == 9:
                surround_accuracy = SurroundingRectangle(accuracy_value)
                self.play(Create(surround_accuracy))
                less_than_0_1 = MathTex("\leq 0.001").next_to(surround_accuracy)
                self.play(Write(less_than_0_1))
                surround_n_steps = SurroundingRectangle(n_steps_str[1])
                self.play(Create(surround_n_steps))
                
                self.wait(2.0)

                log_simeq = MathTex("N\\geq log_2(\\frac{1}{0.001}) \simeq ").next_to(less_than_0_1)
                self.play(ApplyMethod(N_acc_1_2.become, VGroup(log_simeq, DecimalNumber(log2(1000)).next_to(log_simeq))))

                self.wait(2.0)

                self.play(Uncreate(surround_accuracy), Uncreate(less_than_0_1), Uncreate(surround_n_steps))

        self.wait(2.0)

        self.play(ApplyMethod(sub_group.become, Tex("Doesn't matter which function or where the zero is in [a, b]").next_to(question_1, DOWN).to_edge(LEFT)))

        #########################################
        # CHANGE INTERVAL AND RUN THE ANIMATION,#
        # DEMONSTRATE N STEPS,                  #
        # DERIVE THE FORMULA                    #
        # #######################################


        self.wait(2.0)
        # B = C

        # C = (A + B) / 2

        # mid_line = Line(mainNumberLine.n2p(C) - [0, 0.2, 0], mainNumberLine.n2p(C) + [0, 0.2, 0], color=YELLOW)

        # self.play(Create(mid_line))

        # self.wait(1.0)