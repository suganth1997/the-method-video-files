from math import sqrt, tan
from manim import *

class IntroScene(MovingCameraScene):
    def construct(self):
        archimedes = ImageMobject('Archimedes.jpg').scale(0.25).to_edge(RIGHT)

        archimedes_works = ImageMobject('works_of_archimedes.png').scale(0.5).to_corner(RIGHT+DOWN)

        archimedes_quote_1 = Text("Mathematics reveals its secrets only to those who approach it with pure love,", font_size=20).to_edge(UP).to_edge(LEFT)
        archimedes_quote_2 = Text("for its own beauty.", font_size=20).next_to(archimedes_quote_1, DOWN).to_edge(LEFT)
        
        archimedes_name = Text("~ Archimedes", slant=ITALIC, font_size=18).next_to(archimedes_quote_2, DOWN).to_edge(RIGHT)

        self.play(Write(archimedes_quote_1))

        self.play(Write(archimedes_quote_2))

        self.play(Write(archimedes_name))

        self.play(FadeIn(archimedes))

        self.wait(2)

        self.play(Unwrite(archimedes_quote_1), Unwrite(archimedes_quote_2), Unwrite(archimedes_name))

        self.play(archimedes.animate.to_corner(UP + RIGHT))

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

        self.play(Create(fulcrum), Create(center))

        # self.play(Create(lever), Create(center), Create(left_circle), Create(right_circle))

        self.play(Create(lever_and_all))

        self.play(lever_and_all.animate.rotate(PI/12, about_point=center.get_center()))

        self.play(lever_and_all.animate.shift(RIGHT + tan(PI/12)*UP))

        self.play(lever_and_all.animate.rotate(-PI/12, about_point=center.get_center()))

        self.play(Create(lever_law), fulcrum_and_lever.animate.shift((LEFT+UP)*2.25))

        self.play(Create(cup))

        self.play(Create(water_level), Create(water_level_), Create(circle_ball))

        self.play(circle_ball.animate.move_to(DOWN*3/4))

        self.play(water_level.animate.shift(UP*0.2))

        self.play(Create(eureka))

        self.play(Create(buoyance_law), cup_water_setup.animate.next_to(buoyance_law, DOWN*1.5 + 0.25*RIGHT))

        self.play(FadeIn(archimedes_works))

        self.play(Create(geometry_text))

        self.play(Create(geometry_1))

        self.play(Create(geometry_2))

        self.play(Create(geometry_3))

        self.wait(2)
        