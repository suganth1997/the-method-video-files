from math import sqrt, tan
from tkinter import Image
from cv2 import circle
from manim import *

class IntroScene(MovingCameraScene):
    def construct(self):
        archimedes = ImageMobject('Archimedes.jpg').scale(0.25).to_edge(RIGHT)

        archimedes_works = ImageMobject('works_of_archimedes.png').scale(0.5).shift(2*RIGHT)

        archimedes_quote_1 = Text("Mathematics reveals its secrets only to those who approach it with pure love,", font_size=20).to_edge(UP).to_edge(LEFT)
        archimedes_quote_2 = Text("for its own beauty.", font_size=20).next_to(archimedes_quote_1, DOWN).to_edge(LEFT)
        
        archimedes_name = Text("~ Archimedes", slant=ITALIC, font_size=18).next_to(archimedes_quote_2, DOWN).to_edge(RIGHT)

        self.play(Create(archimedes_quote_1))

        self.play(Create(archimedes_quote_2))

        self.play(Create(archimedes_name))

        self.play(FadeIn(archimedes))

        self.wait(2)

        self.play(Uncreate(archimedes_quote_1), Uncreate(archimedes_quote_2), Uncreate(archimedes_name))

        self.play(archimedes.animate.to_corner(UP + RIGHT))

        fulcrum = Polygon(ORIGIN, (LEFT+DOWN)/2, (RIGHT+DOWN)/2, fill_opacity=1)

        lever = Line(3*LEFT, 3*RIGHT, color=BLUE)

        left_circle = Circle(0.3, color=BLUE, fill_opacity=1).move_to(3*LEFT)

        right_circle = Circle(0.15, color=BLUE, fill_opacity=1).move_to(3*RIGHT)

        center = Dot(color=BLUE)

        lever_and_all = VGroup(lever, left_circle, right_circle)

        fulcrum_and_lever = VGroup(fulcrum, center, lever_and_all)

        lever_law = Text("Law of Levers", font_size=20).to_corner(LEFT+UP)

        cup = VGroup(Line(LEFT+UP, (LEFT+DOWN)), Line((LEFT+DOWN), (RIGHT+DOWN)), Line((RIGHT+DOWN), RIGHT+UP))

        water_level = Line(LEFT, RIGHT)

        water_level_ = DashedVMobject(Line(LEFT, RIGHT))

        circle_ball = Circle(0.25, fill_opacity=1).move_to(UP)

        buoyance_law = Text("Law of Buoyancy", font_size=20).to_edge(LEFT)
        
        eureka = Text("Eureka!", slant=ITALIC, font_size=20).next_to(cup, LEFT)

        geometry_text = Text("Works on Geometry", font_size=20)

        cup_water_setup = VGroup(cup, water_level, water_level_, circle_ball, eureka)        

        self.play(Create(fulcrum), Create(center))

        # self.play(Create(lever), Create(center), Create(left_circle), Create(right_circle))

        self.play(Create(lever_and_all))

        self.play(lever_and_all.animate.rotate(PI/12, about_point=ORIGIN))

        self.play(lever_and_all.animate.shift(RIGHT + tan(PI/12)*UP))

        self.play(lever_and_all.animate.rotate(-PI/12, about_point=ORIGIN))

        self.play(Create(lever_law), fulcrum_and_lever.animate.shift((LEFT+UP)*2.25))

        self.play(Create(cup))

        self.play(Create(water_level), Create(water_level_), Create(circle_ball))

        self.play(circle_ball.animate.move_to(DOWN*3/4))

        self.play(water_level.animate.shift(UP*0.2))

        self.play(Create(eureka))

        self.play(Create(buoyance_law), cup_water_setup.animate.next_to(buoyance_law, DOWN*1.5 + 0.25*RIGHT))

        self.play(FadeIn(archimedes_works))

        self.play(archimedes_works.animate.to_corner(RIGHT+DOWN))

        geometry_text = geometry_text.next_to(archimedes_works, LEFT).shift(UP)

        self.play(Create(geometry_text))

        self.wait(2)