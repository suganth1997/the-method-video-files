from math import sqrt, tan
from manim import *

class IntroScene(MovingCameraScene):
    def construct(self):
        archimedes = ImageMobject('Archimedes.jpg').scale(0.25).to_edge(RIGHT)

        archimedes_works = ImageMobject('works_of_archimedes.png').scale(0.5).to_corner(RIGHT+DOWN)

        archimedes_quote_1 = Text("Give me a lever long enough and a fulcrum to place it,", font_size=24).to_edge(UP).to_edge(LEFT)
        archimedes_quote_2 = Text("and I shall move the world.", font_size=24).next_to(archimedes_quote_1, DOWN).to_edge(LEFT)
        
        archimedes_name = Text("~ Archimedes", slant=ITALIC, font_size=20).next_to(archimedes_quote_2, DOWN).to_edge(RIGHT)

        fulcrum = Polygon(ORIGIN, (LEFT+DOWN)/2, (RIGHT+DOWN)/2, fill_opacity=1)

        lever = Line(3*LEFT, 3*RIGHT, color=BLUE)

        left_circle = Circle(0.3, color=BLUE, fill_opacity=1).move_to(3*LEFT)

        right_circle = Circle(0.15, color=BLUE, fill_opacity=1).move_to(3*RIGHT)

        center = Dot(ORIGIN, color=BLUE)

        lever_and_all = VGroup(lever, left_circle, right_circle)

        fulcrum_and_lever = VGroup(fulcrum, center, lever_and_all).shift(0.2*LEFT)

        lever_law = Text("Law of Levers", font_size=20).to_corner(LEFT+UP)

        cup = VGroup(Line(LEFT+UP, (LEFT+DOWN)), Line((LEFT+DOWN), (RIGHT+DOWN)), Line((RIGHT+DOWN), RIGHT+UP))

        water_level = Line(LEFT, RIGHT)

        water_level_ = DashedVMobject(Line(LEFT, RIGHT))

        circle_ball = Circle(0.25, fill_opacity=1).move_to(UP)

        buoyance_law = Text("Law of Buoyancy", font_size=20).to_edge(LEFT)
        
        eureka = Text("Eureka!", slant=ITALIC, font_size=20).next_to(cup, LEFT)

        geometry_text = Text("Works on Geometry", font_size=20).next_to(archimedes_works, LEFT).shift(UP)
        geometry_text.get_left()
        geometry_1 = Text("Bounds on Pi", font_size=16).next_to(geometry_text, DOWN)

        geometry_2 = Text("Volume of sphere", font_size=16).next_to(geometry_1, DOWN)

        geometry_3 = Text("...", font_size=16).next_to(geometry_2, DOWN)

        cup_water_setup = VGroup(cup, water_level, water_level_, circle_ball, eureka)

        self.play(Write(archimedes_quote_1), run_time=2)

        self.play(Write(archimedes_quote_2), run_time=2)

        self.wait(12)

        self.play(Write(archimedes_name), run_time=2)

        self.play(FadeIn(archimedes), run_time=5)

        self.wait(3)

        self.play(Unwrite(archimedes_quote_1), Unwrite(archimedes_quote_2), Unwrite(archimedes_name), run_time=10)

        self.play(archimedes.animate.to_corner(UP + RIGHT), run_time=4)

        self.wait(6)

        self.play(Create(fulcrum), Create(center), run_time=1)

        # self.play(Create(lever), Create(center), Create(left_circle), Create(right_circle))

        self.play(Create(lever_and_all), run_time=1)

        self.wait(3)

        self.play(lever_and_all.animate(run_time=1).rotate(PI/12, about_point=center.get_center()))

        self.play(lever_and_all.animate(run_time=1).shift(RIGHT + tan(PI/12)*UP))

        self.play(lever_and_all.animate(run_time=1).rotate(-PI/12, about_point=center.get_center()))

        self.play(Create(lever_law), fulcrum_and_lever.animate.shift((LEFT+UP)*2.25), run_time=1)

        self.wait(5)

        self.play(Create(cup), run_time=1)

        self.play(Create(water_level), Create(water_level_), Create(circle_ball), run_time=1)

        self.wait(2)

        self.play(circle_ball.animate.move_to(DOWN*3/4), run_time=1)

        self.play(water_level.animate.shift(UP*0.2), run_time=1)

        self.wait(2)

        self.play(Create(eureka), run_time=2)

        self.wait(10)

        self.play(Create(buoyance_law), cup_water_setup.animate.next_to(buoyance_law, DOWN*1.5 + 0.25*RIGHT), run_time=2)

        self.wait(8)

        self.play(FadeIn(archimedes_works), run_time=2)

        self.wait(8)

        self.play(Create(geometry_text), run_time=1)

        self.play(Create(geometry_1), run_time=1)

        self.play(Create(geometry_2), run_time=1)

        self.play(Create(geometry_3), run_time=1)

        self.wait(23)

        